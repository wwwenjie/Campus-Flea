<template>
  <div>
    <van-cell is-link to="user/edit" class="user-info">
      <!--left-->
      <template slot="title">
        <h1>{{username}}</h1>
        <h5>上次登陆：{{lastLogin}}</h5>
        <h5 v-if="bio">{{bio}}</h5>
        <h5 v-else>你的简介空空如也，快来补充吧</h5>
      </template>
      <!--right-->
      <template slot="right-icon">
        <van-image
          round
          :src="avatar"
          class="user-img"
        />
        <van-icon name="arrow" class="user-icon"/>
      </template>
    </van-cell>
    <van-row class="user-links">
      <van-col v-for="item in links" :key="item.name" @click="goToOrder(item.name)" span="6">
        <van-icon :name="item.icon"/>
        {{item.name}}
      </van-col>
    </van-row>

    <van-cell-group class="user-group">
      <van-cell icon="records" title="全部订单" is-link to="user/order"/>
    </van-cell-group>

    <van-cell-group class="user-group">
      <van-cell icon="cart-o" title="购物车" is-link to="cart"/>
      <van-cell icon="gift-o" title="我收藏的" is-link to="cart"/>
      <van-cell icon="contact" title="我的账号" is-link to="user/edit"/>
    </van-cell-group>
    <van-cell-group class="user-group">
      <van-cell @click="logout" icon="close" title="退出登陆" is-link to="account"/>
    </van-cell-group>
    <tabs></tabs>
  </div>
</template>

<script>
import mixins from '@/mixins'
import { Info } from '@/api/user'

export default {
  name: 'User',
  mixins: [mixins],
  components: {
    tabs: () => import('@/components/Tabs.vue')
  },
  data () {
    return {
      links: [
        {
          icon: 'records',
          name: '我买到的'
        },
        {
          icon: 'tosend',
          name: '我卖出的'
        },
        {
          icon: 'pending-payment',
          name: '待付款'
        },
        {
          icon: 'logistics',
          name: '已完成'
        }
      ],
      avatar: null,
      username: null,
      lastLogin: null,
      bio: null
    }
  },
  methods: {
    logout () {
      localStorage.removeItem('token')
      localStorage.removeItem('uid')
      this.setLogin({ isLogin: false })
    },
    goToOrder (nav) {
      this.$router.push({ name: 'order', params: { nav: nav } })
    }
  },
  activated () {
    if (!this.$store.state.is_login) {
      this.$router.push('account')
    }
    Info({
      uid: this.uid
    }).then(res => {
      this.username = res.username
      this.avatar = res.avatar
      this.lastLogin = new Date(res.lastLogin).toLocaleString()
      this.bio = res.bio
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style lang="less">
  .user {
    &-button{
      margin: 2vh 5vw;
      width: 90vw;
    }
    &-img {
      position: absolute;
      right: 10vw;
      top: 50%;
      transform: translate(0, -50%);
      width: 100px;
      height: 100px;
    }

    &-icon {
      position: absolute;
      top: 50%;
      left: 90%;
    }

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
