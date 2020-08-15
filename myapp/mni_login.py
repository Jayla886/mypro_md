# 导包
from selenium import webdriver
import base64,urllib,time,requests,cv2
from selenium.webdriver import ActionChains
# 建立浏览器对象
browser = webdriver.Chrome('C:/jiale/mydjango/chromedriver.exe')
# 打开网页
browser.get('http://localhost:8080/login/')
# 等待两秒钟后进行下一步
time.sleep(2)
# 定位到input输入框
input_user = browser.find_elements_by_tag_name("input")
# 输入用户名
time.sleep(2)
input_user[1].send_keys("jiale")
time.sleep(2)
input_user[2].send_keys("123")
time.sleep(2)
# 选取验证码图片
code_img = browser.find_element_by_class_name("imgcode")
# 截取验证码图片
code_img .screenshot("md2.png")

#获取token
res = requests.get("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=slClh1pWDzR9BDwxGioxU3FD&client_secret=KI9vqbVIZ9GbACtnT722THOdRYZfKUPV")
token = res.json()['access_token']
#接口地址
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token='+token
#定义头部信息
myheaders = {'Content-Type':'application/x-www-form-urlencoded'}
#读取图片
myimg = open('./md2.png','rb')
temp_img = myimg.read()
myimg.close()
img = cv2.imread('./md2.png',cv2.IMREAD_GRAYSCALE)

# 写图
cv2.imwrite('./touxiang1.jpg',img)

#进行base64编码
temp_data = {'image':base64.b64encode(temp_img)}

#对图片地址进行urlencode操作
temp_data = urllib.parse.urlencode(temp_data)

#请求视图接口
res = requests.post(url=url,data=temp_data,headers=myheaders)

code = res.json()['words_result'][0]['words']

code = str(code).replace(' ','')
print(code)
input_user[3].send_keys(code)
# 定位滑块选择器
button = browser.find_element_by_class_name("dv_handler")
# 建立动作对象
action = ActionChains(browser)
# 按住拖动
action.click_and_hold(button).perform()
# 释放
action.reset_actions()
# 拖动位置
action.move_by_offset(280,0).perform()
login_button = browser.find_element_by_class_name("h-btn")
login_button.click()





