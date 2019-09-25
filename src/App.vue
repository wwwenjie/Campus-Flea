<template>
  <div id="app">
    <keep-alive>
      <transition name="van-slide-left">
        <router-view />
      </transition>
    </keep-alive>
  </div>
</template>

<style>
</style>
