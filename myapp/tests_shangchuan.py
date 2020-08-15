from rest_framework.views import APIView
import os
from mydjango.settings import UPLOAD_ROOT
from rest_framework.response import Response
import cv2
from PIL import Image,ImageDraw
# 文件上传类
class Upload(APIView):
    def post(self,request):
        # 接收参数
        myfile =  request.FILES.get('file')
        # 建立文件对象
        f = open(os.path.join(UPLOAD_ROOT,'',myfile.name.replace('"','')),'wb')
        # 写文件
        for chunk in myfile.chunks():
            f.write(chunk)
        f.close()
        return Response({'filename':myfile.name.replace('"','')})

# 图像压缩
# 找大要编辑的图片
img = cv2.imread('./360wallpaper.jpg')
#jpg 360wallpaper.jpg
cv2.imwrite('./360wallpaper.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,50])
# 添加水印
im = Image.open('./360wallpaper.jpg')
print(im.format,im.size,im.mode)

# 生成画笔
draw = ImageDraw.Draw(im)

# 绘制
draw.text((520,680),'django2.0.4',fill=(76,234,124,180))

im.show()
















