import json
from typing import Dict, Any

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from apps.collect.models import Collect


def hello(request):
    all = Collect.objects.all()
    if all is None:
        return HttpResponse("我是空的")
    else:
        for item in all:
            print(item.goods_id)
            print(item.user_id)
            print(item.user)
            print(item.goods)
    return HttpResponse(all)


def search(request):
    if request.method == "GET":
        return HttpResponse("不接受get方法！")
    elif request.method == "POST":
        # 获取传来的json信息
        r = json.loads(request.body)
        goodsName = r['goodsId']
        userId = r['userId']
        judgeType = r['type']
        # 收藏表
        if judgeType == 1:
            # 为空时返回收藏列表
            if goodsName is None:
                data = []
                # 获取到该用户的收藏的商品
                collects = collects = Collect.objects.filter(user_id=userId)
                # 遍历循环添加数据到
                for item in collects:
                    goods = item.goods
                    goodsDic = {
                        "id": goods.id,
                        "goods_name": goods.goods_name,
                        "is_delete": goods.goods_status,
                        "goods_price": goods.goods_price,
                        "goods_image": str(goods.goods_images),
                        "goods_type": goods.goods_type,
                        "create_time": goods.create_time,
                        "update_time": goods.update_time
                    }
                    data.append(goodsDic)
                return JsonResponse({"goods": data})
            # 不为空时查询收藏
            elif goodsName is not None:
                pass
        # 购物车表
        elif judgeType == 2:
            pass
        else:
            # 处理错误信息
            return HttpResponse("error")


def index(request):
    return render(request, 'test.html')
