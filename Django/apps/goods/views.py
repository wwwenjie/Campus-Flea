from django.shortcuts import render
# 导入View抽象类post,get方法
from django.views.generic import View
from apps.goods.models import Goods
from django.http import JsonResponse
from apps.user.models import User


# Create your views here.

# 商品主页
class GoodsMainView(View):
    def get(self, request):
        pass

    def post(self, request):
        goodsType = request.POST.get('category')

        try:
            # 获取所有的数据
            result_goods = Goods.objects.filter(goods_type=goodsType)
        except Goods.DoesNotExist:
            result_goods = ''

        return JsonResponse({'data': result_goods})


# 商品推荐页
class GoodsRecommendView(View):
    def get(self, request):
        pass

    def post(self, request):
        try:
            # 获取所有的数据
            result_goods = Goods.objects.all()
        except Goods.DoesNotExist:
            result_goods = ''

        return JsonResponse({'data': result_goods})
