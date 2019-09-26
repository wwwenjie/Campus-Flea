<!--<template>-->
<!--  <div>-->
<!--    <div class="user-poster">-->
<!--      <van-row>-->
<!--        <van-col offset="22" span="2">-->
<!--          <van-icon name="setting-o" size="1.5em" style="margin-top: 2vh;"/>-->
<!--        </van-col>-->
<!--      </van-row>-->
<!--      <van-row>-->
<!--        <van-col offset="1" span="4">-->
<!--          <img src="https://img.yzcdn.cn/vant/apple-1.jpg" alt="头像" style="height: 20vw;width: 20vw">-->
<!--        </van-col>-->
<!--        <van-col offset="2" span="17">-->
<!--          <div>-->
<!--            <p style="font-size: 10vw; margin: 0">用户名</p>-->
<!--            <p style="font-size: 5vw; margin: 0">预留文本</p>-->
<!--          </div>-->
<!--        </van-col>-->
<!--      </van-row>-->
<!--    </div>-->
<!--    <van-tabs v-model="active" swipeable animated>-->
<!--      <van-tab>-->
<!--        <div slot="title">-->
<!--          <van-icon name="more-o"/>-->
<!--          买家中心-->
<!--        </div>-->
<!--        <van-row class="user-links">-->
<!--          <van-col span="6">-->
<!--            <van-icon name="pending-payment"/>-->
<!--            待付款-->
<!--          </van-col>-->
<!--          <van-col span="6">-->
<!--            <van-icon name="logistics"/>-->
<!--            待发货-->
<!--          </van-col>-->
<!--          <van-col span="6">-->
<!--            <van-icon name="tosend"/>-->
<!--            待确认-->
<!--          </van-col>-->
<!--          <van-col span="6">-->
<!--            <van-icon name="logistics"/>-->
<!--            全部订单-->
<!--          </van-col>-->
<!--        </van-row>-->
<!--        <van-row class="user-links">-->
<!--          <van-col span="6">-->
<!--            <van-icon name="pending-payment"/>-->
<!--            我的收藏-->
<!--          </van-col>-->
<!--          <van-col span="6">-->
<!--            <van-icon name="records"/>-->
<!--            购物车-->
<!--          </van-col>-->
<!--          <van-col span="6">-->
<!--            <van-icon name="tosend"/>-->
<!--            待发货-->
<!--          </van-col>-->
<!--          <van-col span="6">-->
<!--            <van-icon name="logistics"/>-->
<!--            已发货-->
<!--          </van-col>-->
<!--        </van-row>-->

<!--        <van-cell-group>-->
<!--          <van-cell>更多功能，敬请期待。</van-cell>-->
<!--        </van-cell-group>-->
<!--      </van-tab>-->
<!--      <van-tab>-->
<!--        <div slot="title">-->
<!--          <van-icon name="more-o"/>-->
<!--          卖家中心-->
<!--        </div>-->
<!--      </van-tab>-->
<!--    </van-tabs>-->
<!--    <tabs></tabs>-->
<!--  </div>-->
<!--</template>-->

<template>
  <div>
    <img class="user-poster" src="https://img.yzcdn.cn/public_files/2017/10/23/8690bb321356070e0b8c4404d087f8fd.png">
    <van-row class="user-links">
      <van-col span="6">
        <van-icon name="pending-payment" />
        待付款
      </van-col>
      <van-col span="6">
        <van-icon name="records" />
        待接单
      </van-col>
      <van-col span="6">
        <van-icon name="tosend" />
        待发货
      </van-col>
      <van-col span="6">
        <van-icon name="logistics" />
        已发货
      </van-col>
    </van-row>

    <van-cell-group class="user-group">
      <van-cell icon="records" title="全部订单" is-link />
    </van-cell-group>

    <van-cell-group>
      <van-cell icon="points" title="我的积分" is-link />
      <van-cell icon="gold-coin-o" title="我的优惠券" is-link />
      <van-cell icon="gift-o" title="我收到的礼物" is-link />
    </van-cell-group>
    <tabs></tabs>
  </div>
</template>

<script>
export default {
  name: 'User',
  components: {
    tabs: () => import('@/components/Tabs.vue')
  }
}
</script>

<style lang="less">
  .user {
    &-poster {
      width: 100%;
      height: 53vw;
      display: block;
    }
    &-group {
      margin-bottom: 15px;
    }
    &-links {
      padding: 15px 0;
      font-size: 12px;
      text-align: center;
      background-color: #fff;
      .van-icon {
        display: block;
        font-size: 24px;
      }
    }
  }
</style>
