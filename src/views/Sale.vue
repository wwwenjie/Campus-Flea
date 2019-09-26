<template>
  <div>
    <van-nav-bar
      title="发布新的物品"
    />
    <van-cell-group>
      <van-field
        v-model="title"
        clearable
        placeholder="标题 品类品牌型号都是卖家喜欢搜索的"
      />

      <van-field
        v-model="detail"
        :border="false"
        :autosize="{ maxHeight: 200, minHeight: 150 }"
        placeholder="描述宝贝的转手原因，入手渠道和使用感受"
        type="textarea"
      />

      <van-uploader
        v-model="fileList"
        :after-read="afterRead"
        :max-count="7"
        :preview-size="100">
      </van-uploader>
    </van-cell-group>

    <van-cell-group>
      <van-field
        readonly
        clickable
        clearable
        label="价格"
        :value="price"
        @touchstart.native.stop="showPriceInput = true"
      />

      <van-number-keyboard
        :show="showPriceInput"
        extra-key="."
        theme="custom"
        close-button-text="完成"
        v-model="price"
        @blur="showPriceInput = false"
      />

      <van-field
        readonly
        clickable
        label="分类"
        :value="category"
        placeholder="选择分类"
        @click="showCatPicker = true"
      />

      <van-popup v-model="showCatPicker" position="bottom">
        <van-picker
          show-toolbar
          :columns="categories"
          @cancel="showCatPicker = false"
          @confirm="onCatConfirm"
        />
      </van-popup>

      <van-button @click="onConfirm" type="info" size="large">确认发布</van-button>
    </van-cell-group>
    <tabs></tabs>
  </div>
</template>

<script>
export default {
  name: 'Sale',
  components: {
    tabs: () => import('@/components/Tabs.vue')
  },
  data () {
    return {
      title: '',
      detail: '',
      fileList: [
        { url: 'https://img.yzcdn.cn/vant/cat.jpeg' },
        // Uploader 根据文件后缀来判断是否为图片文件
        // 如果图片 URL 中不包含类型信息，可以添加 isImage 标记来声明
        { url: 'https://cloud-image', isImage: true }
      ],
      category: '',
      showCatPicker: false,
      categories: ['杭州', '宁波', '温州', '嘉兴', '湖州'],
      showPriceInput: false,
      price: ''
    }
  },
  methods: {
    // upload file to server
    afterRead (file) {
      // 此时可以自行将文件上传至服务器
      console.log(file)
    },
    // category selected
    onCatConfirm (value) {
      this.category = value
      this.showCatPicker = false
    },
    // add a new item to server
    onConfirm () {
      console.log()
    }
  },
  mounted () {
    if (!this.$store.state.is_login) {
      this.$router.push('account')
    }
  }
}
</script>

<style scoped>

</style>
