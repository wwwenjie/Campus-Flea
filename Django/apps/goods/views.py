from django.shortcuts import render
# 导入View抽象类post,get方法
from django.views.generic import View
from apps.goods.models import Goods
from django.http import JsonResponse
from apps.user.models import User
import json


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


# 商品上传
class GoodsUploadView(View):
    def get(self, request):
        pass

    def post(self, request):
        r = json.loads(request.body)
        title = r['title']
        detail = r['detail']
        category = r['category']
        # {url: url1, hash: hash1}
        # url通过 | 分割多个图片链接存在一个字段，hash同理
        url_array = r['url']
        seller_id = r['sellerId']
        price = r['price']
        express = r['express']
        area = r['area']
        url = ''
        for item in url_array:
            url = url + str(item['url']) + '|'
        img_hash = ''
        for item in url_array:
            img_hash = img_hash + str(item['hash']) + '|'
        goods = Goods()
        goods.status = 2
        goods.title = title
        goods.detail = detail
        goods.category = category
        # 去除最后多余的|
        goods.url = url[:-1]
        goods.img_hash = img_hash[:-1]
        goods.seller_id = seller_id
        goods.price = price
        goods.express = express
        # 去除最后多余的,
        goods.area = area[:-1]
        goods.save()
        return JsonResponse({'success': bool(True)})


# 商品详情页
class GoodsDetailView(View):
    def get(self, request):
        pass

    def post(self, request):
        r = json.loads(request.body)
        goods_id = r['id']
        try:
            goods = Goods.objects.get(id=goods_id)
            # 获取卖家名
            try:
                seller_name = User.objects.get(id=goods.seller_id).username
            except User.DoesNotExist:
                return JsonResponse({'success': bool(False)})
            # 分割图片url
            url = goods.url.split('|')
            print(url)
            return JsonResponse({
                'title': goods.title,
                'detail': goods.detail,
                'url': url,
                'price': goods.price,
                'express': goods.express,
                'sellerId': goods.seller_id,
                'sellerName': seller_name,
                'area': goods.area
            })
        except Goods.DoesNotExist:
            return JsonResponse({'success': bool(False)})
