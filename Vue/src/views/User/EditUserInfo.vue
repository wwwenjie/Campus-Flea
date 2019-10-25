<template>
  <div>
    <van-nav-bar
      left-arrow
      @click-left="routerBack"
      :title="title"
    />
    <van-cell-group>
      <van-field
        v-model="content"
        rows="4"
        autosize
        type="textarea"
        maxlength="50"
        :placeholder="content"
        show-word-limit
      >
      </van-field>
    </van-cell-group>
    <van-button @click="save" type="info" class="user-button">保存</van-button>
  </div>
</template>

<script>
import mixins from '@/mixins'
import { Edit } from '@/api/user'
import Vue from 'vue'
import { Notify } from 'vant'

Vue.use(Notify)

export default {
  name: 'EditUserInfo',
  mixins: [mixins],
  data () {
    return {
      title: null,
      content: null,
      type: null
    }
  },
  methods: {
    save () {
      Edit({
        uid: this.uid,
        type: this.type,
        content: this.content
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
  },
  activated () {
    if (this.$route.params.content[1]) {
      this.content = this.$route.params.content[1]
    } else {
      this.content = ''
    }
    if (this.$route.params.content[0]) {
      this.title = this.$route.params.content[0]
    } else {
      this.title = ''
    }
    this.type = this.$route.params.type
  }
}
</script>

<style scoped>

</style>
