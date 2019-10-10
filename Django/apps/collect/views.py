import json
from typing import Dict, Any

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from apps.collect.models import Collect, ShopCart


def search(request):

    data = []
    if request.method == "GET":
        return HttpResponse("不接受get方法！")
    elif request.method == "POST":
        # 获取传来的json信息
        r = json.loads(request.body)
        goodsID = r['goodsId']
        userId = r['userId']
        judgeType = r['type']
        operate = r['operate']
        # 收藏表
        if judgeType == 1:
            # 为空时返回收藏列表
            if goodsID is None:
                # 获取到该用户的收藏的商品
                collects = Collect.objects.filter(user_id=userId)
                # start
                ary = []
                for item in collects:
                    goods = item.goods
                    # 序列化必须是可迭代对象哦！所以加入到数组里面
                    ary.append(goods)
                data = json.loads(serialize("json", ary))
                # end
                return JsonResponse({"goods": data})
            # 不为空时添加或者删除收藏的信息
            elif goodsID is not None:
                # 删除
                if operate == 0:
                    try:
                        goods = Collect.objects.filter(user_id=userId).filter(goods_id=goodsID)
                        goods.delete()
                        return JsonResponse({"seccess": True})
                    except RuntimeError:
                        return JsonResponse({"seccess": False})

                # 添加
                if operate == 1:
                    try:
                        result = Collect.objects.filter(user_id=userId).filter(goods_id=goodsID)
                        # 判断是否存在，防止添加重复数据
                        if result.exists():
                            print("已经存在")
                            return JsonResponse({"seccess": False})
                        goods = Collect()
                        goods.goods_id = goodsID
                        goods.user_id = userId
                        goods.save()
                    except RuntimeError:
                        return JsonResponse({"seccess": False})
                    return JsonResponse({"seccess": True})

        # 购物车表
        elif judgeType == 2:
            if goodsID is None:
                shopCarts = ShopCart.objects.filter(user_id=userId, goods_id=goodsID)

                ary = []
                for item in shopCarts:
                    goods = item.goods
                    # 序列化必须是可迭代对象哦！所以加入到数组里面
                    ary.append(goods)
                data = json.loads(serialize("json", ary))
                return JsonResponse({"goods": data})
            elif goodsID is not None:
                # 删除
                if operate == 0:
                    try:
                        goods = ShopCart.objects.filter(user_id=userId).filter(goods_id=goodsID)
                        goods.delete()
                        return JsonResponse({"seccess": True})
                    except RuntimeError:
                        return JsonResponse({"seccess": False})

                # 添加
                if operate == 1:
                    try:
                        result = ShopCart.objects.filter(user_id=userId).filter(goods_id=goodsID)
                        # 判断是否存在，防止添加重复数据
                        if result.exists():
                            print("已经存在")
                            return JsonResponse({"seccess": False})
                        goods = ShopCart()
                        goods.goods_id = goodsID
                        goods.user_id = userId
                        goods.save()
                        print("保存成功")
                    except RuntimeError:
                        return JsonResponse({"seccess": False})
                    return JsonResponse({"seccess": True})
        else:
            # 处理错误信息
            return HttpResponse("error")


def index(request):
    return render(request, 'test.html')
