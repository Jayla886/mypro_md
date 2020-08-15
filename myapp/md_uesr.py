import hashlib,re,requests,redis,os
# 导入又拍云模块
import upyun
from django.db.models import F,Q
from django.shortcuts import redirect
import jwt
from myapp.models import User,Carousel
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# 导入图片库
# 绘画库
from PIL import ImageDraw
# 字体库
from PIL import ImageFont
# 图片库
from PIL import Image
# 随即库
import random
# 文件流
import io
# 从settings中导入文件上传的位置
from mydjango.settings import UPLOAD_ROOT
import time
import hmac
import base64
from hashlib import sha256
import urllib
import json
from myapp.myser import CarouselSer
from django.utils.deprecation import MiddlewareMixin

# 轮播图接口
class GetCarousel(APIView):

	def get(self,request):
		# 读库
		carousels = Carousel.objects.all()

		# 序列化操作
		carousels_ser = CarouselSer(carousels,many=True)
		return Response(carousels_ser.data)


# 自定义中间件
class MyMiddleware(MiddlewareMixin):

	def process_request(self,request):
		print('过滤中间件')
		pass
		# return HttpResponse(json.dumps({'message':'你篡改了id'},
		# ensure_ascii = False,indent=4),content_type='application/json'
		# 					)
		pass
	def process_view(self,request,view_func,view_args,view_kwargs):
		pass
	def process_exception(self,request,exception):
		pass
	def process_reqponse(self,request,response):
		return response

# 定义redis的ip和端口
host = 'localhost'
port = 6379
# 建立连接
r = redis.Redis(host=host,port=port)
AK = 'V6pHMttEYhLB3FkmpEkecHZrxeAjLBydFGj86EHl'
SK = 'ygI47eOmBAZbJvmEyruedjzGeeQZjGiQCl5ptznA'

from django.utils.decorators import method_decorator
# 定义权限检测装饰器
def my_decorator(func):
	def wrapper(request,*args,**kwargs):
		# 接收参数
		uid = request.GET.get("uid", None)
		myjwt = request.GET.get("jwt", None)
		print(uid)
		print(jwt)
		# 验证用户合法性
		decode_jwt = jwt.decode(myjwt, 'qwe123', algorithms=['HS256'])
		#  比对
		if int(uid) != int(decode_jwt['uid']):
			return Response({'code': 401, 'message': '你的密钥无权限'})
		return func(request,*args,**kwargs)
	return wrapper


# 获取用户信息

class UserInfo(APIView):
	@method_decorator(my_decorator)
	def get(self,request):
		# 接收参数
		uid = request.GET.get("uid",None)
		myjwt= request.GET.get("jwt",None)
		print(uid)
		print(myjwt)
		# 验证用户合法性
		decode_jwt = jwt.decode(myjwt,'qwe123', algorithms=['HS256'])
		#  比对
		if int(uid) != int(decode_jwt['uid']):
			return Response({'code':401,'message':'你的密钥无权限'})

		# 查询数据库
		user = User.objects.get(id=int(uid))
		if user.img == '':
			user.img = "touxiang1.png"

		# 返回
		return Response({'img':user.img,'phone':user.phone})


# 定义又拍云文件上传类
class UPYUpload(APIView):
	def post(self, request):
		# 获取文件
		file = request.FILES.get('file')
		# 新建又拍云实例
		up = upyun.UpYun('jiale-meiduo', 'fanjiale', 'SjFkpfCt94p7rIp1DlIdznP1v2NWmcFp')
		# 声明头部信息
		headers = {'x-gmkerl-rotate': 'auto'}

		# 上传图片
		for chunk in file.chunks():
			res = up.put('/touxiang_test1.jpg', chunk, checksum=True, headers=headers)

		return Response({'filename': file.name})

# 构造顶顶登录接口
def ding_login(request):
	appid = 'dingoayj23de23gty1libw'
	redirect_uri = 'http://localhost:8000/ding_login/'
	return redirect(
		'https://oapi.dingtalk.com/connect/qrconnect?appid=' + appid + '&response_type=code&scope=snsapi_login&state=STATE&redirect_uri=' + redirect_uri)

#构造钉钉回调方法
def ding_back(request):
    #获取code
    code = request.GET.get("code")
    t = time.time()
    #时间戳
    timestamp = str((int(round(t * 1000))))
    appSecret ='6DY6w9VYytiGRIceuX7GlvPw8mm4DIpJxag5cUF_nH1fFjXTcYzHg-KVX1W8FhwX'
    #构造签名
    signature = base64.b64encode(hmac.new(appSecret.encode('utf-8'),timestamp.encode('utf-8'), digestmod=sha256).digest())
    #请求接口，换取钉钉用户名
    payload = {'tmp_auth_code':code}
    headers = {'Content-Type': 'application/json'}
    res = requests.post('https://oapi.dingtalk.com/sns/getuserinfo_bycode?signature='+urllib.parse.quote(signature.decode("utf-8"))+"&timestamp="+timestamp+"&accessKey=dingoaukgkwqknzjvamdqh",data=json.dumps(payload),headers=headers)

    res_dict = json.loads(res.text)
    print(res_dict)
    return HttpResponse(res.text)

from qiniu import Auth
# 七牛云
class Qiniu(APIView):
	def get(self,request):
		# 声明认证对象
		q = Auth('V6pHMttEYhLB3FkmpEkecHZrxeAjLBydFGj86EHl',
				 'ygI47eOmBAZbJvmEyruedjzGeeQZjGiQCl5ptznA')
		# 获取token
		token = q.upload_token('jialeupload')
		return Response({'token':token})

# 文件上传通用类
class UploadFile(APIView):

	def post(self,request):
		#接收参数
		myfile = request.FILES.get('file')
		uid = request.POST.get('uid',None)
		#建立文件流对象
		f = open(os.path.join(UPLOAD_ROOT,'',myfile.name.replace('"','')),'wb')
		#写入
		for chunk in myfile.chunks():
			f.write(chunk)
		f.close()
		# 修改头像地址
		user = User.objects.get(id=int(uid))
		user.img = myfile.name.replace('"','')
		user.save()

		return Response({'filename':myfile.name.replace('"',''),'u_img':''})

# 构造钉钉登录url
def ding_url(request):
    appid = 'dingoaukgkwqknzjvamdqh'
    redirect_uri = 'http://localhost:8000/dingding_back/'

    return redirect('https://oapi.dingtalk.com/connect/qrconnect?appid='+appid+'&response_type=code&scope=snsapi_login&state=STATE&redirect_uri='+redirect_uri)

#新浪微博回调方法
def wb_back(request):
	#接收参数
	code = request.GET.get('code',None)

	#定义token接口地址
	url = "https://api.weibo.com/oauth2/access_token"

	#定义参数
	re = requests.post(url,data={
		"client_id":"2949825616",
		"client_secret":"efcf35e94890965ae1d71eb7b971c693",
		"grant_type":"authorization_code",
		"code":code,
		"redirect_uri":"http://127.0.0.1:8000/md_admin/weibo"
	})

	print(re.json())

	#换取新浪微博用户昵称
	res = requests.get('https://api.weibo.com/2/users/show.json',params={'access_token':re.json()['access_token'],'uid':re.json()['uid']})

	print(res.json())
	sina_id = ''
	user_id = ''

	# 判断是否用新浪微博登录过
	user = User.objects.filter(username=str(res.json()['name'])).first()

	if user:
		# 代表曾经用该账号登录过
		sina_id = user.username
		user_id = user.id
	else:
		# 首次登录，入库新浪微博账号
		user = User(username=str(res.json()['name']), password='')
		user.save()
		user = User.objects.filter(username=str(res.json()['name'])).first()
		sina_id = user.username
		user_id = user.id

	print(sina_id, user_id)
	# 重定向
	return redirect("http://localhost:8080?sina_id=" + str(sina_id) + "&uid=" + str(user_id))
	# return HttpResponse("回调成功")


# 自定义图片验证码
class Mycode(View):
	# 定义rgb随机颜色
	def get_random_color(self):
		R = random.randrange(255)
		G = random.randrange(255)
		B = random.randrange(255)
		return (R,G,B)
	# 定义图片视图
	def get(self, request):
		# 画布
		img_size = (120, 50)
		# 定义图片对象
		image = Image.new('RGB', img_size, 'white')
		# 定义画笔
		draw = ImageDraw.Draw(image, 'RGB')
		source = '0123456789abcdefghijk'
		# 接收容器
		code_str = ''
		# 进入循环绘制
		for i in range(4):
			# 获取字母颜色
			text_color = self.get_random_color()
			# 获取随机下标
			tmp_num = random.randrange(len(source))
			# 随机字符串
			random_str = source[tmp_num]
			# 装入容器
			code_str += random_str
			# 绘制字符串
			draw.text((10 + 30 * i, 20), random_str, text_color)
		# 获取缓存区
		buf = io.BytesIO()
		# 将临时图片保存到缓冲
		image.save(buf, 'png')
		# 保存随机码
		r.set('code', code_str)
		o_code = r.get('code')
		print(o_code)
		n_code = o_code.decode("utf-8")
		print(n_code)
		# print(type(n_code))
		return HttpResponse(buf.getvalue(), 'image/png')

def make_password(mypass):

    # 生成md5对象
    md5 = hashlib.md5()

    # 转码
    mypass_utf8 = str(mypass).encode(encoding="utf-8")

    # 加密
    md5.update(mypass_utf8)

    # 返回密文
    return md5.hexdigest()

#登录接口
class Login(APIView):

	def get(self,request):

		#接收参数
		username = request.GET.get('username',None)
		password = request.GET.get('password',None)
		code = request.GET.get('code',None)

		# 比对验证码
		redis_code = r.get("code")
		# 转码
		redis_code = redis_code.decode("utf-8")
		# 从session中取值
		session_code = request.session.get("code",None)
		print(session_code)

		if code != redis_code:
			return Response({'code':'403','msssage':'你输入的验证码有误'})
		#查询数据 .get
		user = User.objects.filter(Q(username=username) | Q(phone=username),Q(password=make_password(password))).first()

		if user:
			# 生成用户token
			encode_jwt = jwt.encode({'uid':user.id}, 'qwe123', algorithm='HS256')
			print(encode_jwt)
			# 转码
			encode_str = str(encode_jwt, 'utf-8')
			print(encode_str)
			return Response({'code':200,'message':'登陆成功','uid':user.id,
							 'username':user.username,'jwt':encode_str})

		else:

			return Response({'code':403,'message':'您的用户名或者密码错误'})

# 注册接口
class Register(APIView):
	def get(self,request):

		# 接收参数
		username = request.GET.get('username',None)
		password = request.GET.get('password',None)
		phone = request.GET.get('phone',None)


		# 排重操作
		user = User.objects.filter(username=username).first()

		if user:
			return Response({'code':403,'message':'该用户名已经存在'})

		# 入库
		user = User(username=username,password=make_password(password),phone=phone)

		# 保存结果
		user.save()

		return Response({'code':200,'message':'恭喜注册成功'})

	def post(self,request):

		# 接收参数
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)

		# 排重操作
		user = User.objects.filter(username=username).first()

		if user:
			return Response({'code':403,'message':'该用户名已经存在'})

		# 入库
		user = User(username=username,password=make_password(password))

		# 保存结果
		user.save()

		return Response({'code':200,'message':'恭喜注册成功'})

