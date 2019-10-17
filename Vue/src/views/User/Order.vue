<template>
  <div>
    <van-nav-bar
      left-arrow
      @click-left="onClickLeft"
      :title="this.$route.params.nav"
    />
    <div class="container">
      <van-card
        v-for="item in goods"
        :key="item.id"
        :title="item.title"
        :price="item.price"
        :thumb="item.url"
        @click="onClickCard(item.id)"
      >
        <div slot="tags">
          <van-tag plain size="large" type="danger">{{item.status}}</van-tag>
        </div>
        <template slot="num">
          <van-button @click.stop="" @click="onClickContact(item.id)" plain hairline round type="info" text="联系卖家"/>
        </template>
      </van-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Order',
  data () {
    return {
      goods: [{
        id: '1',
        title: '进口香蕉',
        status: '卖家',
        price: 200,
        url: 'https://img.yzcdn.cn/public_files/2017/10/24/2f9a36046449dafb8608e99990b3c205.jpeg'
      }, {
        id: '2',
        title: '陕西蜜梨',
        status: '卖家',
        price: 690.05,
        url: 'https://img.yzcdn.cn/public_files/2017/10/24/f6aabd6ac5521195e01e8e89ee9fc63f.jpeg'
      }, {
        id: '3',
        title: '美国伽力果',
        status: '卖家',
        price: 2680,
        url: 'https://img.yzcdn.cn/public_files/2017/10/24/320454216bbe9e25c7651e1fa51b31fd.jpeg'
      }]
    }
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

<style lang="less" scoped>
  .container {
    padding: 14px 16px;
  }

  .van-card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
    width: 100%;
    border-radius: 8px;
    margin-bottom: 20px;

    .van-card__title {
      font-size: 1.5em;
      line-height: normal;
    }

    .van-card__price {
      position: absolute;
      bottom: 5px;
      font-size: 1.5em;
      color: #f44;
    }
  }
</style>
