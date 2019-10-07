<template>
  <div id="app">
    <keep-alive>
      <transition name="van-slide-left">
        <router-view/>
      </transition>
    </keep-alive>
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
      if (res.data.success) {
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
