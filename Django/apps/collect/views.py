import json

from django.http import JsonResponse

# Create your views here.
from apps.collect.models import Collect, ShopCart


def search(request):
    r = json.loads(request.body)
    goods_id = r['goodsId']
    uid = r['uid']
    # 0收藏 1购物车
    judge_type = r['type']
    # 0删除，1添加
    operate = r['operate']
    # 为空时返回列表
    if goods_id is None:
        return JsonResponse({"data": get_data(uid, judge_type)})
    # 不为空时添加或者删除
    else:
        result = delete(uid, goods_id, judge_type) if operate == 0 else add(uid, goods_id, judge_type)
        return JsonResponse({"success": result['success'], 'msg': result['msg']})


def get_data(uid, judge_type):
    if judge_type == 0:
        result = Collect.objects.filter(user_id=uid)
    else:
        result = ShopCart.objects.filter(user_id=uid)
    data = []
    for item in result:
        data.append(item.goods_id)
    return data


def add(uid, goods_id, judge_type):
    if judge_type == 0:
        result = Collect.objects.filter(user_id=uid).filter(goods_id=goods_id)
        item = Collect()
    else:
        result = ShopCart.objects.filter(user_id=uid).filter(goods_id=goods_id)
        item = ShopCart()
    # 判断是否存在，防止添加重复数据
    if result.exists():
        return {'success': False, 'msg': '已经存在'}
    item.goods_id = goods_id
    item.user_id = uid
    item.save()
    return {'success': True, 'msg': '添加成功'}


def delete(uid, goods_id, judge_type):
    if judge_type == 0:
        item = Collect.objects.filter(user_id=uid).filter(goods_id=goods_id)
    else:
        item = ShopCart.objects.filter(user_id=uid).filter(goods_id=goods_id)
    item.delete()
    return {'success': True, 'msg': '删除成功'}
