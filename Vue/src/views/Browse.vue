<template>
  <div>
    <van-overlay
      :show="show"
      style="margin-top: 54px"
      :z-index=2
    />
    <form action="/">
      <van-search
        v-model="searchitem"
        placeholder="请输入搜索关键词"
        shape="round"
        @search="onSearch"
        @focus="dropdownShow"
        @blur="dropdownShow"
        @input="searchLive"
      >
      </van-search>
    </form>
    <van-cell-group v-if="dropdown" class="search-list">
      <van-cell v-for="item of searchList" @click="onSearch(item)" :key="item" :title="item"/>
    </van-cell-group>
    <van-swipe :autoplay="3000">
      <van-swipe-item v-for="(image, index) in images" :key="index">
        <img v-lazy="image" class="img"/>
      </van-swipe-item>
    </van-swipe>
    <van-tabs @change="tabsChange" sticky animated swipeable>
      <van-tab v-for="tab in tabs" :key="tab" :title="tab">
        <van-list
          v-model="loading"
          :finished="finished"
          finished-text="没有更多了"
          @load="onLoad"
          class="show-text"
        >
          <van-grid :gutter="10" :column-num="2" :border="false">
            <van-grid-item
              @click="goToDetail(item.id)"
              v-for="item in goods"
              :key="item.id">
              <card :url="item.url" :title="item.title" :price="item.price"></card>
            </van-grid-item>
          </van-grid>
        </van-list>
      </van-tab>
    </van-tabs>
    <tabs></tabs>
  </div>
</template>

<script>
import mixins from '@/mixins'
import { Browse, Search } from '@/api/goods'
import { Lazyload } from 'vant'
import Vue from 'vue'

Vue.use(Lazyload)

export default {
  name: 'Browse',
  mixins: [mixins],
  components: {
    card: () => import('@/components/browse/Card.vue'),
    tabs: () => import('@/components/Tabs.vue')
  },
  data () {
    return {
      show: false,
      dropdown: false,
      searchList: [],
      loading: null,
      finished: null,
      images: [
        'https://img.yzcdn.cn/vant/apple-1.jpg',
        'https://img.yzcdn.cn/vant/apple-2.jpg',
        'https://img.yzcdn.cn/vant/apple-3.jpg',
        'https://img.yzcdn.cn/vant/apple-4.jpg'
      ],
      tabs: ['最新', '书籍', '生活用品', '3C数码', '鞋服美妆', '兼职', '求助', '其他'],
      currentTab: '最新',
      page: 1,
      goods: [],
      searchitem: null
    }
  },
  methods: {
    onSearch: function (content = this.searchitem) {
      // onSearch
      Search({
        title: content
      }).then(res => {
        if (res.data) {
          this.goods = []
          for (let item of res.data) {
            this.goods.push(item)
          }
        }
      }).catch(err => {
        console.log(err)
      })
    },
    searchLive (value) {
      Search({
        title: value
      }).then(res => {
        if (res.data) {
          this.searchList = []
          for (let item of res.data) {
            this.searchList.push(item.title)
          }
        }
      }).catch(err => {
        console.log(err)
      })
    },
    dropdownShow () {
      this.show = !this.show
      this.dropdown = !this.dropdown
      this.searchList = []
    },
    onLoad () {
      // request data
      this.loading = true
      this.finished = false
      Browse({
        category: this.currentTab,
        page: this.page
      }).then(res => {
        if (res.data) {
          for (let item of res.data) {
            this.goods.push(item)
          }
          this.loading = false
          this.page++
        } else {
          this.finished = true
          this.loading = false
        }
      }).catch(err => {
        console.log(err)
      })
    },
    goToDetail (id) {
      this.setGoodId(id)
      this.$router.push({ name: 'detail' })
    },
    tabsChange (name, title) {
      this.currentTab = title
      this.page = 1
      this.goods = []
      this.onLoad()
    }
  }
}
</script>

<style scoped>
  .img {
    width: 100%;
    height: 240px;
  }

  .show-text {
    padding-bottom: 50px;
  }

  .search-list {
    z-index: 2;
    position: fixed;
    width: 100vw;
  }
</style>
