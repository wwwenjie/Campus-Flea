<template>
  <div>
    <div class="user-poster">
      <van-row>
        <van-col offset="22" span="2">
          <van-icon name="setting-o" size="1.5em" style="margin-top: 2vh;"/>
        </van-col>
      </van-row>
      <van-row>
        <van-col offset="1" span="4">
          <img src="https://img.yzcdn.cn/vant/apple-1.jpg" alt="头像" style="height: 20vw;width: 20vw">
        </van-col>
        <van-col offset="2" span="17">
          <div>
            <p style="font-size: 10vw; margin: 0">用户名</p>
            <p style="font-size: 5vw; margin: 0">预留文本</p>
          </div>
        </van-col>
      </van-row>
    </div>
    <van-tabs v-model="active" swipeable animated>
      <van-tab>
        <div slot="title">
          <van-icon name="more-o"/>
          买家中心
        </div>
        <van-row class="user-links">
          <van-col span="6">
            <van-icon name="pending-payment"/>
            待付款
          </van-col>
          <van-col span="6">
            <van-icon name="logistics"/>
            待发货
          </van-col>
          <van-col span="6">
            <van-icon name="tosend"/>
            待确认
          </van-col>
          <van-col span="6">
            <van-icon name="logistics"/>
            全部订单
          </van-col>
        </van-row>
        <van-row class="user-links">
          <van-col span="6">
            <van-icon name="pending-payment"/>
            我的收藏
          </van-col>
          <van-col span="6">
            <van-icon name="records"/>
            购物车
          </van-col>
          <van-col span="6">
            <van-icon name="tosend"/>
            待发货
          </van-col>
          <van-col span="6">
            <van-icon name="logistics"/>
            已发货
          </van-col>
        </van-row>

        <van-cell-group>
          <van-cell>更多功能，敬请期待。</van-cell>
        </van-cell-group>
      </van-tab>
      <van-tab>
        <div slot="title">
          <van-icon name="more-o"/>
          卖家中心
        </div>
      </van-tab>
    </van-tabs>
  </div>
</template>

<script>
export default {
  name: 'User'
}
</script>

<style lang="less">
.user {
  &-poster {
    width: 100%;
    height: 25vh;
    display: block;
    background: -webkit-linear-gradient(#1989fa, #4cc4fa); /* Safari 5.1 - 6.0 */
    background: -o-linear-gradient(#1989fa, blue); /* Opera 11.1 - 12.0 */
    background: -moz-linear-gradient(#1989fa, blue); /* Firefox 3.6 - 15 */
    background: linear-gradient(#2e87fa, #4cc4fa); /* 标准的语法 */
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
