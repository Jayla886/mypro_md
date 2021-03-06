# # 图像处理
import cv2

img = cv2.imread('../code.png',cv2.IMREAD_GRAYSCALE)

# 写图
cv2.imwrite('../code1.png',img)

from PIL import Image,ImageDraw
# 读图
im = Image.open('./touxiang.png')
print(im.format,im.size,im.mode)

# 生成画笔
draw = ImageDraw.Draw(im)

# 绘制
draw.text((0,0),'1907',fill=(76,234,124,180))
# (600,308)
im.show()

# 图像压缩
img = cv2.imread('./touxiang.png')

# 压缩  0-9
cv2.imwrite('./touxiang1.png',img,[cv2.IMWRITE_PNG_COMPRESSION,5])


# jpj
cv2.imwrite('./touxiang.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,50])














