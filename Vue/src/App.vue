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

export default {
  mounted () {
    Auth({
      uid: localStorage.getItem('uid'),
      token: localStorage.getItem('token')
    }).then(res => {
      if (res.data.success) {
        this.$store.commit('SET_LOGIN', {
          isLogin: true
        })
      }
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style>
</style>
