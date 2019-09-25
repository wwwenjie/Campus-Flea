<template>
  <van-tabbar route>
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
</template>

<script>
export default {
  name: 'Tabbar'
}
</script>

<style scoped>

</style>
