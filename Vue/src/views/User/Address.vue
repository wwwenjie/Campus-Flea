<template>
  <div>
    <van-nav-bar
      left-arrow
      @click-left="routerBack"
      title="编辑收货地址"
    />
    <van-address-edit
      :area-list="areaList"
      show-postal
      show-delete
      show-set-default
      @save="onSave"
    />
  </div>
</template>

<script>
import areaList from '@/assets/area.js'
import mixins from '@/mixins'
import { Edit } from '@/api/user'
import Vue from 'vue'
import { Notify } from 'vant'

Vue.use(Notify)

export default {
  name: 'Address',
  mixins: [mixins],
  data () {
    return {
      areaList: areaList
    }
  },
  methods: {
    onSave (val) {
      console.log(val)
      Edit({
        uid: this.uid,
        type: 'address',
        content: JSON.stringify(val)
      }).then(res => {
        if (res.success) {
          Notify({ type: 'success', message: '保存成功' })
          setTimeout(() => {
            this.$router.back()
          }, 1000)
        } else {
          Notify('保存失败')
        }
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>

</style>
