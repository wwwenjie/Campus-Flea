<template>
  <van-row>
    <van-col offset="2" span="20">
      <h1 class="account-title">
        <img src="https://img.yzcdn.cn/vant/logo.png">
        <span>Vant</span>
      </h1>
      <van-cell-group>
        <h1>快捷登录注册</h1>
        <van-field
          v-model="username"
          clearable
          size="large"
          placeholder="邮箱/手机号"
          class="account-input"
        />

        <van-field
          v-model="password"
          type="password"
          size="large"
          placeholder="密码"
          class="account-input"
        />

      </van-cell-group>
      <van-button
        size="large"
        color="linear-gradient(to right, #4bb0ff, #6149f6)"
        class="account-button"
      >
        登录
      </van-button>
      <span class="account-forget">忘记密码?</span>
      <span class="account-register">立即注册</span>
    </van-col>
  </van-row>
</template>

<script>
export default {
  name: 'Account'
}
</script>

<style lang="less" scoped>
  .account {
    &-title span{
      display: inline;
      margin-left: 16px;
      font-size: 15vw;
      vertical-align: top;
    }
    &-title img {
      width: 30vw;
    }
    &-input{
      margin-top: 5vh;
    }
    &-button{
      margin-top: 5vh;
    }
    &-forget{
      float: left;
      margin-top: 5px;
    }
    &-register{
      float: right;
      margin-top: 5px;
    }
  }
</style>
