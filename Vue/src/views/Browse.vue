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
      <van-cell v-for="item of searchList" :key="item" :title="item"/>
    </van-cell-group>
    <van-swipe :autoplay="3000">
      <van-swipe-item v-for="(image, index) in images" :key="index">
        <img v-lazy="image"/>
      </van-swipe-item>
    </van-swipe>
    <van-tabs @change="tabsChange" sticky animated swipeable>
      <van-tab v-for="tab in tabs" :key="tab.name" :title="tab.title" :name="tab.name">
        <van-list
          v-model="loading"
          :finished="finished"
          finished-text="没有更多了"
          :immediate-check="false"
          @load="onLoad"
        >
          <van-grid :gutter="10" :column-num="2" :border="false" class="grid">
            <van-grid-item
              @click="goToDetail(item.id)"
              v-for="item in goods"
              :key="item.id">
              <card :thumb="item.thumb" :title="item.title" :price="item.price"></card>
            </van-grid-item>
          </van-grid>
        </van-list>
      </van-tab>
    </van-tabs>
    <tabs></tabs>
  </div>
</template>

<script>
import store from '@/mixins.js'

export default {
  name: 'Browse',
  mixins: [store],
  components: {
    card: () => import('@/components/browse/Card.vue'),
    tabs: () => import('@/components/Tabs.vue')
  },
  data () {
    return {
      show: false,
      dropdown: false,
      searchList: [],
      loading: false,
      finished: false,
      images: [
        'https://img.yzcdn.cn/vant/apple-1.jpg',
        'https://img.yzcdn.cn/vant/apple-2.jpg',
        'https://img.yzcdn.cn/vant/apple-3.jpg',
        'https://img.yzcdn.cn/vant/apple-4.jpg'
      ],
      tabs: [
        {
          title: '最新',
          name: 'newest'
        },
        {
          title: '书籍',
          name: 'book'
        },
        {
          title: '生活用品',
          name: 'daily'
        },
        {
          title: '3C数码',
          name: '3c'
        },
        {
          title: '鞋服美妆',
          name: 'dress'
        },
        {
          title: '求助',
          name: 'help'
        }
      ],
      goods: [
        {
          id: 1,
          thumb: 'https://img.yzcdn.cn/vant/apple-1.jpg',
          title: '免押金出租索尼E口24 1.4 GM大师定焦镜头全画幅 免押金出',
          price: 1200
        },
        {
          id: 2,
          thumb: 'https://img.yzcdn.cn/vant/apple-1.jpg',
          title: 'sss',
          price: 50
        }
      ],
      searchitem: null
    }
  },
  methods: {
    onSearch: function () {
      // onSearch
    },
    searchLive (value) {
      this.searchList.push(value)
    },
    dropdownShow () {
      this.show = !this.show
      this.dropdown = !this.dropdown
      this.searchList = []
    },
    onLoad () {
      // axios
      this.loading = false
      // if r = null
      this.finished = true
    },
    goToDetail (id = 1) {
      this.setGoodId(id)
      this.$router.push({ name: 'detail' })
    },
    tabsChange (name, title) {
      // refresh data
      console.log(name)
      console.log(title)
    }
  }
}
</script>

<style scoped>
  img {
    width: 100%;
    height: 240px;
  }

  .grid {
    margin-bottom: 100px;
  }

  .search-list {
    z-index: 2;
    position: fixed;
    width: 100vw;
  }
</style>
