<template>
  <div>
    <van-nav-bar
      left-arrow
      @click-left="routerBack"
      title="编辑信息"
    />
    <van-cell is-link class="user-info">
      <!--left-->
      <template slot="title">
        <h1>{{data.username[1]}}</h1>
        <h5>上次登陆：{{data.lastLogin[1]}}</h5>
        <h5 v-if="data.bio[1]">{{data.bio[1]}}</h5>
        <h5 v-else>你的简介空空如也，快来补充吧</h5>
      </template>
      <!--right-->
      <template slot="right-icon">
        <van-image
          round
          :src="avatarUrl"
          class="user-img"
        />
      </template>
    </van-cell>
    <van-cell-group class="user-group">
      <van-cell v-for="(item, index) in data" :key="item[0]" @click="edit(index)" is-link>
        <template slot="title">
          <span>{{item[0]}}</span>
          <span class="span">{{item[1]}}</span>
        </template>
      </van-cell>
    </van-cell-group>
    <van-button @click="removeAccount" type="danger" class="user-button">注销账号</van-button>
    <van-overlay :show="loading"/>
    <van-loading v-if="loading" color="#1989fa" size="3rem" vertical class="loading">上传中...</van-loading>
    <!--input to upload avatar-->
    <input v-show="false" ref="avatar" @change="avatarUpload($event)" type="file" accept="image/*">
    <van-popup v-model="showSexPicker" position="bottom">
      <van-picker
        show-toolbar
        :columns="sexPicker"
        @cancel="showSexPicker = false"
        @confirm="onSexConfirm"
      />
    </van-popup>
    <van-popup v-model="showDatePicker" position="bottom">
      <van-datetime-picker
        v-model="currentDate"
        type="date"
        :min-date="minDate"
        @cancel="showDatePicker = false"
        @confirm="onDateConfirm"
      />
    </van-popup>
  </div>
</template>

<script>
import mixins from '@/mixins'
import { Info, Edit } from '@/api/user'
import { ImgUpload } from '@/api/goods'
import Vue from 'vue'
import { Notify } from 'vant'

Vue.use(Notify)

export default {
  name: 'Edit',
  mixins: [mixins],
  data () {
    return {
      data: {
        avatar: ['头像', '点击更换头像'],
        username: ['名称', null],
        lastLogin: ['上次登陆', null],
        bio: ['简介', null],
        email: ['邮箱', null],
        address: ['地址', null],
        sex: ['性别', null],
        bday: ['生日', null],
        qq: ['QQ', null],
        wechat: ['微信', null]
      },
      avatarUrl: null,
      loading: false,
      showSexPicker: false,
      sexPicker: ['男', '女'],
      showDatePicker: false,
      currentDate: new Date(),
      minDate: new Date('1900-01-17T03:24:00')
    }
  },
  methods: {
    edit (type) {
      if (['username', 'bio', 'email', 'qq', 'wechat'].indexOf(type) !== -1) {
        this.$router.push({ name: 'editUserInfo', params: { content: this.data[type], type: type } })
      } else {
        switch (type) {
          case 'avatar':
            this.$refs.avatar.click()
            break
          case 'address':
            this.$router.push({ name: 'address' })
            break
          case 'sex':
            this.showSexPicker = true
            break
          case 'bday':
            this.showDatePicker = true
            break
        }
      }
    },
    avatarUpload (e) {
      // upload img to sm.ms server
      let data = new FormData()
      data.append('smfile', e.target.files[0])
      this.loading = true
      ImgUpload(data).then((res) => {
        if (res.success) {
          Notify({ type: 'success', message: '上传成功' })
          this.loading = false
          this.uploadInfo('avatar', res.data.url)
          this.$set(this.data.avatar, 1, res.data.url)
        } else {
          Notify({ type: 'danger', message: res.message })
          this.loading = false
        }
      }).catch(err => {
        console.log(err)
      })
    },
    onSexConfirm (sex) {
      this.data.sex[1] = sex
      this.showSexPicker = false
      this.uploadInfo('sex', this.data.sex[1])
    },
    onDateConfirm (date) {
      this.data.bday[1] = date.toLocaleDateString()
      this.showDatePicker = false
      this.uploadInfo('bday', date.toISOString())
    },
    removeAccount () {
      console.log(this.data.username[1])
    },
    uploadInfo (type, content) {
      Edit({
        uid: this.uid,
        type: type,
        content: content
      }).then(res => {
        if (res.success) {
          Notify({ type: 'success', message: '保存成功' })
        } else {
          Notify('保存失败')
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  activated () {
    Info({
      uid: this.uid
    }).then(res => {
      this.$set(this.data.username, 1, res.username)
      // this.$set(this.data.avatar, 1, res.avatar)
      this.avatarUrl = res.avatar
      this.$set(this.data.lastLogin, 1, new Date(res.lastLogin).toLocaleString())
      this.$set(this.data.bio, 1, res.bio)
      this.$set(this.data.email, 1, res.email)
      let address = JSON.parse(res.address)
      this.$set(this.data.address, 1, address.province + ' ' + address.city + ' ' + address.county)
      this.$set(this.data.sex, 1, res.sex)
      this.$set(this.data.bday, 1, new Date(res.bday).toLocaleDateString())
      this.$set(this.data.qq, 1, res.qq)
      this.$set(this.data.wechat, 1, res.wechat)
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style scoped>
  .span {
    position: absolute;
    left: 25vw;
    color: #999999;
  }

  .loading {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
  }
</style>
