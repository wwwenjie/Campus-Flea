<template>
  <div>
    <van-nav-bar
      left-arrow
      @click-left="onClickLeft"
      title="编辑收货地址"
    />
    <van-address-edit
      :area-list="areaList"
      show-postal
      show-delete
      show-set-default
      show-search-result
      :search-result="searchResult"
      tel-validator
      postal-validator
      @save="onSave"
      @delete="onDelete"
      @change-detail="onChangeDetail"
    />
  </div>
</template>

<script>
import areaList from '@/assets/area.js'
export default {
  name: 'Address',
  data () {
    return {
      areaList: areaList,
      searchResult: []
    }
  },
  methods: {
    onSave () {
      Toast('save')
    },
    onDelete () {
      Toast('delete')
    },
    onChangeDetail (val) {
      if (val) {
        this.searchResult = [{
          name: '黄龙万科中心',
          address: '杭州市西湖区'
        }]
      } else {
        this.searchResult = []
      }
    },
    onClickLeft () {
      this.$router.back()
    }
  }
}
</script>

<style scoped>

</style>
