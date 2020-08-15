# 导包
from rest_framework import serializers
# 序列化的目的是把数据变成json类型
# 反序列化是把json类型数据转化成普通数据
# 导入需要序列化的表
from myapp.models import Carousel,Goods,Category,Image,Comment

#建立序列化类
class CommentSer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields = "__all__"
# 建立序列化类
class CarouselSer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = "__all__"

# 商品表序列化类
class GoodsSer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"

# 商品分类表序列化类
class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

# 商品小图序列化类
class ImageSer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"












