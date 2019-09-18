<template>
  <div class="card">
    <van-image
      width="100%"
      lazy-load
      :src="url"
      class="image">
      <template v-slot:loading>
        <van-loading type="spinner" size="20" />
      </template>
      <template v-slot:error>
          <van-icon name="photo-o" size="30" />
          暂无图片
      </template>
    </van-image>
    <div class="container">
      <h4><b>{{name}}</b></h4>
      <p>￥{{price}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: {
    url: {
      default: 'https://www.w3schools.com/howto/img_avatar.png'
    },
    name: {
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
  /* Add shadows to create the "card" effect */
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
  width: 100%;
}

/* On mouse-over, add a deeper shadow */
.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

/* Add some padding inside the card container */
.container {
  padding: 2px 16px;
}

.image{
  min-height: 120px;
}
</style>
