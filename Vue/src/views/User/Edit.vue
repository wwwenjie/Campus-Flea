<template>
  <div>
    <van-cell is-link to="user/edit" class="user-info">
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
          src="https://img.yzcdn.cn/vant/cat.jpeg"
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
    <van-button type="danger" size="large">注销账号</van-button>
  </div>
</template>

<script>
import mixins from '@/mixins'
import { Info } from '@/api/user'

export default {
  name: 'Edit',
  mixins: [mixins],
  data () {
    return {
      data: {
        avatar: ['头像', null],
        username: ['用户名', null],
        lastLogin: ['上次登陆', null],
        bio: ['简介', null],
        email: ['邮箱', null],
        address: ['地址', null],
        sex: ['性别', null],
        bday: ['生日', null],
        qq: ['QQ', null],
        wechat: ['微信', null]
      }
    }
  },
  methods: {
    edit (type) {
      console.log(type)
      return type
    }
  },
  mounted () {
    Info({
      uid: this.uid
    }).then(res => {
      this.data.username[1] = res.username
      this.data.avatar[1] = res.avatar
      this.data.lastLogin[1] = res.lastLogin
      this.data.bio[1] = res.bio
      this.data.email[1] = res.email
      this.data.address[1] = res.address
      this.data.sex[1] = res.sex
      this.data.bday[1] = res.bday
      this.data.qq[1] = res.qq
      this.data.wechat[1] = res.wechat
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
</style>
