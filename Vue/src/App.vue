<template>
  <div id="app">
<!--    <transition name="van-slide-left">-->
      <keep-alive>
        <router-view v-transition style="min-height: 100vh"></router-view>>
      </keep-alive>
<!--    </transition>-->
  </div>
</template>

<script>
import { Auth } from '@/api/user'
import mixins from '@/mixins'

export default {
  mixins: [mixins],
  mounted () {
    Auth({
      uid: localStorage.getItem('uid'),
      token: localStorage.getItem('token')
    }).then(res => {
      if (res.success) {
        this.setUid(localStorage.getItem('uid'))
        this.setToken(localStorage.getItem('token'))
        this.setLogin({ isLogin: true })
      }
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style>
</style>
