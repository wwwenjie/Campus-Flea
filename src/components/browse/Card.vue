<template>
  <div class="card">
    <van-image
      width="100%"
      lazy-load
      :src="thumb"
      class="min-height"
    >
      <template v-slot:loading>
        <van-loading type="spinner" size="30" />
      </template>
      <template v-slot:error>
          <van-icon name="photo-o" size="30" />
          暂无图片
      </template>
    </van-image>
    <div class="container">
      <h4><b>{{title}}</b></h4>
      <p>￥{{price}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: {
    thumb: {},
    title: {
      require: true
    },
    price: {
      require: true
    }
  }
}
</script>

<style scoped>
  .card {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 100%;
    border-radius: 8px;
  }

  .container {
    padding: 2px 16px;
  }

  .min-height{
    min-height: 20vh;
  }
</style>
