<template>
  <div id="app">
    <keep-alive>
      <transition name="van-slide-left">
        <router-view />
      </transition>
    </keep-alive>
    <van-tabbar v-if="showTab" route>
      <van-tabbar-item
        replace
        to="/browse"
        icon="browsing-history-o"
      >
        首页
      </van-tabbar-item>
      <van-tabbar-item
        replace
        to="/sale"
        icon="after-sale"
      >
        出售
      </van-tabbar-item>
      <van-tabbar-item
        replace
        to="/user"
        icon="user-o"
      >
        我的
      </van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
export default {
  computed: {
    showTab: function () {

    }
  }
}
</script>

<style>
</style>
