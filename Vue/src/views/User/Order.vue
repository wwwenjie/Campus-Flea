<template>
  <div>
    <van-nav-bar
      left-arrow
      @click-left="onClickLeft"
      title="我的订单"
    />
    <div class="container">
      <van-card
        @click="onClickCard(id)"
        num="1"
        price="2.00"
        title="商品标题"
        desc="描述信息"
        url="https://img.yzcdn.cn/vant/t-thirt.jpg"
        class="card"
      >
        <div slot="tags">
          <van-tag plain type="danger">待付款</van-tag>
        </div>
      </van-card>
      <van-card
        num="1"
        price="2.00"
        title="商品标题"
        desc="描述信息"
        url="https://img.yzcdn.cn/vant/t-thirt.jpg"
        class="card"
      >
        <div slot="tags">
          <van-tag plain type="danger">待付款</van-tag>
        </div>
      </van-card>
      <van-card
        num="1"
        price="2.00"
        title="商品标题"
        desc="描述信息"
        url="https://img.yzcdn.cn/vant/t-thirt.jpg"
        class="card"
      >
        <div slot="tags">
          <van-tag plain type="danger">待付款</van-tag>
        </div>
      </van-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Order',
  data () {
    return {}
  },
  methods: {
    onClickLeft () {
      this.$router.back()
    },
    onClickCard (id) {
      this.$router.push({ name: 'orderDetail' })
    }
  }
}
</script>

<style scoped>
  .card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
    width: 100%;
    border-radius: 8px;
    margin-bottom: 20px;
  }

  .container {
    padding: 14px 16px;
  }
</style>
