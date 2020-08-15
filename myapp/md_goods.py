import hashlib,re,requests,redis,os
# 导入又拍云模块
import upyun
from django.db.models import F,Q
from django.shortcuts import redirect
import jwt
from myapp.models import User,Carousel,Category
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
from myapp.myser import CarouselSer,GoodsSer,CategorySer,ImageSer,CommentSer
from django.utils.deprecation import MiddlewareMixin
from myapp.models import Goods,Image,Comment
from django.db import connection
import redis

host = "localhost"
port = 6379

# 建立连接
r = redis.Redis(host=host,port=port)
#商品评论获取
class CommentList(APIView):

	def get(self,request):

		gid = request.GET.get("gid",None)

		#查询数据
		comments = Comment.objects.filter(gid=gid).order_by("-id")

		#序列化
		comments_ser = CommentSer(comments,many=True)

		return Response(comments_ser.data)

#格式化结果集
def dictfetch(cursor):

	#声明描述符
	desc = cursor.description

	return [ dict( zip([col[0] for col in desc ],row) )

			for row in cursor.fetchall()
	]

#搜索接口
class Search(APIView):

	def get(self,request):

		#检索字段
		text = request.GET.get('text',None)

		#转换数据类型
		text = json.loads(text)


		sql = ""
		#动态拼接
		for val in text:
			sql += "or name like '%%%s%%' " % val

		sql = sql.lstrip("or")

		sql_cursor = "select name,id,img,price from goods where id != 0 and ( " + sql + ")"

		#建立游标对象
		cursor = connection.cursor()

		#执行sql
		cursor.execute(sql_cursor)

		#查询
		#result_tuple = cursor.fetchall()
		result = dictfetch(cursor)


		return Response({'data':result})


# 商品小图
class ImageList(APIView):
    def get(self,request):
        images = Image.objects.all()
        image_ser = ImageSer(images,many=True)
        return Response(image_ser.data)

# 商品详情页
class GoodInfo(APIView):
    def get(self,request):
        # 接收参数
        id = request.GET.get("id",None)
        # 查询
        good = Goods.objects.get(id=id)
        good_ser = GoodsSer(good)
        return Response(good_ser.data)


# 商品评论
class CommentInsert(APIView):

    def post(self, request):

        # 获取客户端ip
        if 'HTTP_X_FORWARDED_FOR' in request.META:

            ip = request.META.get('HTTP_X_FORWARDED_FOR')

        else:

            ip = request.META.get('REMOTE_ADDR')

        # if r.get(ip):

        if r.llen(ip) > 3:
            return Response({'code': 403, 'message': '您评论的过快，请歇一歇'})

        # 初始化参数
        comment = CommentSer(data=request.data)

        # 验证字段
        if comment.is_valid():
            # 进行入库
            comment.save()

            # 设置评论间隔时间
            # r.set(ip,"123")

            r.lpush(ip, 1)
            r.expire(ip, 30)

        return Response({'code': 200, 'message': '评论成功'})


# 商品入库
class InsertGoods(APIView):
    def get(self,request):
        # 接收参数
        name = request.GET.get("name",None)
        price = request.GET.get("price",None)
        params = request.GET.get("params",None)
        cid = request.GET.get("cid",None)
        print(cid)
        # 排重操作
        goods = Goods.objects.filter(name=name).first()
        if goods:
            return Response({'code':403,'message':'您已添加过该商品'})
        # 入库
        goods = Goods(name=name,price=price,params=params,cid = cid)
        goods.save()
        return Response({'code':200,'message':'商品添加成功'})

class CategoryList(APIView):
    def get(self,request):
        category = Category.objects.all()
        categoryser = CategorySer(category,many=True)
        return Response(categoryser.data)

#商品列表页
class GoodsList(APIView):

	def get(self,request):



		#检索字段
		text = request.GET.get('text',None)

		print(text)

		#排序字段
		coloum = request.GET.get('coloum',None)

		#排序方案
		sort_order = request.GET.get('order','')

		#当前页
		page = request.GET.get('page',1)

		#一页显示个数
		size = request.GET.get('size',1)

		#计算从哪儿开始切
		data_start = (int(page)-1) * int(size)

		#计算切到哪儿
		data_end = int(page) * int(size)

		#查询 切片操作

		if coloum:

			goods = Goods.objects.all().order_by(sort_order+coloum)[data_start:data_end]

		else:

			goods = Goods.objects.all()[data_start:data_end]

		#判断是否进行模糊查询
		if text:

			goods = Goods.objects.filter(Q(name__contains=text)  | Q(desc__contains=text) )[data_start:data_end]

			count = Goods.objects.filter(Q(name__contains=text) | Q(desc__contains=text)).count()
		else:

			#查询所有商品个数
			count = Goods.objects.count()

		#序列化
		goods_ser = GoodsSer(goods,many=True)

		return Response({'data':goods_ser.data,'total':count})





































































































































































































































































































































































