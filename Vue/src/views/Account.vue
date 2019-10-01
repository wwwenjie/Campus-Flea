<template>
  <van-row>
    <van-col offset="2" span="20">
      <h1 class="account-title">
        <img src="https://img.yzcdn.cn/vant/logo.png">
        <span>Vant</span>
      </h1>

      <span class="account-span">快捷登录注册</span>

      <van-field
        v-model="username"
        clearable
        size="large"
        placeholder="邮箱/手机号"
        class="account-input"
      >
        <van-button v-if="status!=='login'" slot="button" size="small" type="primary">发送验证码</van-button>
      </van-field>

      <transition name="van-slide-up">
        <van-field
          v-if="status!=='login'"
          v-model="sms"
          center
          clearable
          placeholder="请输入短信验证码"
          class="account-input"
        >
        </van-field>
      </transition>

      <van-field
        v-model="password"
        type="password"
        size="large"
        placeholder="密码"
        class="account-input"
      />

      <transition name="van-slide-up">
        <van-field
          v-if="status!=='login'"
          v-model="password"
          type="password"
          size="large"
          placeholder="确认密码"
          class="account-input"
        />
      </transition>

      <van-button
        v-bind:key="status"
        @click="handleButtonClick"
        size="large"
        color="linear-gradient(to right, #4bb0ff, #6149f6)"
        class="account-button"
      >
        {{buttonMessage}}
      </van-button>

      <transition name="van-fade">
        <p v-if="status==='login'">
          <span @click="setStatus('forget')" class="account-forget">忘记密码?</span>
          <span @click="setStatus('register')" class="account-register">立即注册</span>
        </p>
      </transition>
    </van-col>
  </van-row>
</template>

<script>
import store from '@/mixins.js'

export default {
  name: 'Account',
  mixins: [store],
  data () {
    return {
      status: 'login'
    }
  },
  computed: {
    buttonMessage: function () {
      switch (this.status) {
        case 'login':
          return '登陆'
        case 'register':
          return '注册'
        case 'forget':
          return '重置密码'
        default:
          return '未知错误'
      }
    }
  },
  methods: {
    setStatus: function (status) {
      this.status = status
    },
    handleButtonClick: function () {
      switch (this.status) {
        case 'login':
          // handle login
          this.setLogin()
          this.routerBack()
          break
        case 'register':
          // handle register
          this.status = 'login'
          break
        case 'forget':
          // handle forget
          this.status = 'login'
          break
        default:
          break
      }
    }
  }
}
</script>

<style lang="less" scoped>
  .account {
    &-title span {
      display: inline;
      margin-left: 16px;
      font-size: 15vw;
      vertical-align: top;
    }

    &-title img {
      width: 30vw;
    }

    &-span {
      font-size: 8vw;
      font-weight: bold;
    }

    &-input {
      margin-top: 5vh;
    }

    &-button {
      margin-top: 5vh;
    }

    &-forget {
      float: left;
      margin-top: 5px;
    }

    &-register {
      float: right;
      margin-top: 5px;
    }
  }
</style>
