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
        placeholder="设置价格"
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

      <van-field
        readonly
        clickable
        label="发货地"
        :value="area"
        placeholder="选择发货地"
        @click="showAreaListPicker = true"
      />

      <van-popup v-model="showAreaListPicker" position="bottom">
        <van-area
          :area-list="areaList"
          @cancel="showAreaListPicker = false"
          @confirm="onAreaConfirm"
        />
      </van-popup>

      <van-field
        readonly
        clickable
        clearable
        label="运费"
        :value="express"
        placeholder="设置运费 0为包邮"
        @touchstart.native.stop="showExpressInput = true"
      />

      <van-number-keyboard
        :show="showExpressInput"
        extra-key="."
        theme="custom"
        close-button-text="完成"
        v-model="express"
        @blur="showExpressInput = false"
      />

      <van-button
        @click="onConfirm"
        size="large"
        color="linear-gradient(to right, #4bb0ff, #6149f6)"
      >
        确认发布
      </van-button>
    </van-cell-group>
    <tabs></tabs>
  </div>
</template>

<script>
import { ImgUpload, Upload } from '@/api/goods'
import Vue from 'vue'
import { Notify, Toast } from 'vant'
import areaList from '@/assets/area.js'

Vue.use(Notify)
Vue.use(Toast)

export default {
  name: 'Sale',
  components: {
    tabs: () => import('@/components/Tabs.vue')
  },
  data () {
    return {
      title: '',
      detail: '',
      category: '',
      url: [],
      price: '',
      express: '',
      area: '',
      // for preview pics, unused
      fileList: [],
      showAreaListPicker: false,
      areaList: areaList,
      showCatPicker: false,
      categories: ['书籍', '生活用品', '3C数码', '鞋服美妆', '求助', '其他'],
      showPriceInput: false,
      showExpressInput: false
    }
  },
  methods: {
    // upload file to server
    afterRead (file) {
      // upload img to sm.ms server
      let data = new FormData()
      data.append('smfile', file.file)
      ImgUpload(data).then((res) => {
        if (res.success) {
          Notify({ type: 'success', message: '上传成功' })
          this.url.push({ url: res.data.url, hash: res.data.hash })
        } else {
          Notify({ type: 'danger', message: res.message })
          this.fileList.pop()
        }
      }).catch(err => {
        console.log(err)
      })
    },
    // category selected
    onCatConfirm (value) {
      this.category = value
      this.showCatPicker = false
    },
    // area selected
    onAreaConfirm (value) {
      console.log(value)
      for (let item of value) {
        // get the name of the area
        this.area += item.name + ','
      }
      this.showAreaListPicker = false
    },
    // add a new goods to server
    onConfirm () {
      Upload({
        title: this.title,
        detail: this.detail,
        category: this.category,
        url: this.url,
        sellerId: this.$store.state.uid,
        price: this.price,
        express: this.express,
        area: this.area
      }).then(res => {
        if (res.success) {
          Toast.success('发布成功')
        } else {
          Toast.fail('发布失败')
        }
      }).catch(err => {
        console.log(err)
        Toast.fail('服务器内部错误')
      })
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
