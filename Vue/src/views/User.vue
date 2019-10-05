<template>
  <div>
    <img class="user-poster" src="https://img.yzcdn.cn/public_files/2017/10/23/8690bb321356070e0b8c4404d087f8fd.png">
    <van-row class="user-links">
      <van-col span="6">
        <van-icon name="records"/>
        我买到的
      </van-col>
      <van-col span="6">
        <van-icon name="tosend"/>
        我卖出的
      </van-col>
      <van-col span="6">
        <van-icon name="pending-payment"/>
        待付款
      </van-col>
      <van-col span="6">
        <van-icon name="logistics"/>
        已完成
      </van-col>
    </van-row>

    <van-cell-group class="user-group">
      <van-cell icon="records" title="全部订单" is-link to="user/order"/>
    </van-cell-group>

    <van-cell-group class="user-group">
      <van-cell icon="gold-coin-o" title="购物车" is-link to="cart"/>
      <van-cell icon="gift-o" title="我收藏的" is-link/>
    </van-cell-group>
    <van-cell-group class="user-group">
      <van-cell @click="logout" icon="gold-coin-o" title="退出登陆" is-link to="account"/>
    </van-cell-group>
    <tabs></tabs>
  </div>
</template>

<script>
import mixins from '@/mixins'

export default {
  name: 'User',
  mixins: [mixins],
  components: {
    tabs: () => import('@/components/Tabs.vue')
  },
  methods: {
    logout () {
      localStorage.removeItem('token')
      localStorage.removeItem('uid')
      this.setLogin({ isLogin: false })
    }
  },
  mounted () {
    if (!this.$store.state.is_login) {
      this.$router.push('account')
    }
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
