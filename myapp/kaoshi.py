from rest_framework.views import APIView
from myapp.models import *
from rest_framework.response import Response
from myapp.myser import *
from django.db.models import F,Q

# 商品列表
class Shop(APIView):
    def get(self,request):
        # 接收前端参数
        text = request.GET.get('text',None)
        print(text)
        # 当前页
        page = request.GET.get('page', 1)
        # # 一页显示个数
        size = request.GET.get('size', 2)
        # # 计算从哪儿开始切
        data_start = (int(page) - 1) * int(size)
        # # 计算切到哪儿
        data_end = int(page) * int(size)
        # 查询 切片操作
        goods = Goods.objects.all().order_by("price","id")[data_start:data_end]
        if text:
            goods = Goods.objects.filter(name__contains=text)
        else:
            pass
        # 查询所有商品个数
        count = Goods.objects.count()
        # 序列化
        goods_ser = GoodsSer(goods, many=True)
        return Response({'data': goods_ser.data, 'total': count})