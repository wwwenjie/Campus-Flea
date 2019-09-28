<template>
  <div>
    <van-nav-bar
      left-arrow
      @click-left="onClickLeft"
      title="订单信息"
    />
    <div class="container">
      <van-steps :active="active">
        <van-step>买家下单</van-step>
        <van-step>商家接单</van-step>
        <van-step>买家提货</van-step>
        <van-step>交易完成</van-step>
      </van-steps>
      <p class="price">1700.00<span>元</span></p>
      <van-cell-group>
        <van-cell title="见面交易，无需物流" is-link value="物流详情" class="cell"/>
        <van-cell is-link title="iphone 6s plus 国行 64g" value="联系卖家" class="cell"/>
      </van-cell-group>
      <p class="info">
        <span class="info-left">
          买家名称
        </span>
        <span class="info-right">
          kingravvit
        </span>
      </p>
      <p class="info"><span class="info-left">订单编号</span><span class="info-right">21356156123035165</span></p>
      <p class="info"><span class="info-left">交易号</span><span class="info-right">145218651561351864681</span></p>
      <p class="info"><span class="info-left">交易时间</span><span class="info-right">1531.15.12 11:37:15</span></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrderDetail',
  data () {
    return {
      active: 1
    }
  },
  methods: {
    onClickLeft () {
      this.$router.back()
    }
  }
}
</script>

<style lang="less" scoped>
  .container {
    padding: 14px 16px;
  }

  .price {
    text-align: center;
    color: red;
    font-size: 10vw;

    span {
      font-size: 5vw
    }
  }

  .cell {
    padding: 20px;
  }

  .info {
    color: #999999;
    padding: 0 5px;

    &-left {
      absolute: left;
    }

    &-right {
      float: right;
    }
  }
</style>
