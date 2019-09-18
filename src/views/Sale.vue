<template>
  <div>
    <van-nav-bar title="发布物品"/>
    <van-uploader
      v-model="fileList"
      :after-read="afterRead"
      :max-count="7"
      :preview-size="100">
    </van-uploader>
  </div>
</template>

<script>
export default {
  name: 'Sale',
  data () {
    return {
      fileList: [
        { url: 'https://img.yzcdn.cn/vant/cat.jpeg' },
        // Uploader 根据文件后缀来判断是否为图片文件
        // 如果图片 URL 中不包含类型信息，可以添加 isImage 标记来声明
        { url: 'https://cloud-image', isImage: true }
      ]
    }
  },
  methods: {
    afterRead (file) {
      // 此时可以自行将文件上传至服务器
      console.log(file)
    }
  }
}
</script>

<style scoped>

</style>
