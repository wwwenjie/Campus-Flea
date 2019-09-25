<template>
  <div>
    <form action="/">
      <van-search
        v-model="searchValue"
        placeholder="请输入搜索关键词"
        shape="round"
        @search="onSearch"></van-search>
    </form>
    <van-swipe :autoplay="3000">
      <van-swipe-item v-for="(image, index) in images" :key="index">
        <img v-lazy="image"/>
      </van-swipe-item>
    </van-swipe>
    <van-tabs v-model="activeTab" sticky animated swipeable>
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
              @click="detail(id)"
              v-for="value in data"
              :key="value.id">
              <card :url="value.url" :name="value.name" :price="value.price"></card>
            </van-grid-item>
          </van-grid>
        </van-list>
      </van-tab>
      <van-tab title="求助" name="b">内容 2</van-tab>
      <van-tab title="书本" name="c">内容 3</van-tab>
      <van-tab title="服装" name="d">内容 3</van-tab>
      <van-tab title="服装" name="e">内容 3</van-tab>
    </van-tabs>
    <tabs></tabs>
  </div>
</template>

<script>
export default {
  name: 'browse',
  components: {
    card: () => import('@/components/browse/Card.vue'),
    tabs: () => import('@/components/Tabs.vue')
  },
  data () {
    return {
      loading: false,
      finished: false,
      tabs: [
        {
          title: '测试',
          name: 'a'
        },
        {
          title: '测试b',
          name: 'b'
        },
        {
          title: '测试c',
          name: 'c'
        }
      ],
      data: [
        {
          id: 1,
          url: 'https://www.w3schools.com/howto/img_avatar.png',
          name: '免押金出租索尼E口24 1.4 GM大师定焦镜头全画幅 免押金出',
          price: 1200
        },
        {
          id: 2,
          url: 'https://img.yzcdn.cn/vant/apple-1.jpg',
          name: 'sss',
          price: 50
        },
        {
          id: 3,
          url: 'https://www.w3schools.com/howto/img_avatar.png',
          name: 'ss',
          price: 30
        },
        {
          id: 4,
          url: 'https://www.w3schools.com/howto/img_avatar.png',
          name: 'asdsadasd',
          price: 10
        },
        {
          id: 5,
          url: 'https://img.yzcdn.cn/vant/apple-1.jpg',
          name: 'sss',
          price: 50
        },
        {
          id: 6,
          url: 'https://www.w3schools.com/howto/img_avatar.png',
          name: 'ss',
          price: 30
        },
        {
          id: 20,
          url: 'https://www.w3schools.com/howto/img_avatar.png',
          name: 'asdsadasd',
          price: 10
        },
        {
          id: 12,
          url: 'https://img.yzcdn.cn/vant/apple-1.jpg',
          name: 'sss',
          price: 50
        },
        {
          id: 13,
          url: 'https://www.w3schools.com/howto/img_avatar.png',
          name: 'ss',
          price: 30
        },
        {
          id: 7,
          url: 'https://www.w3schools.com/howto/img_avatar.png',
          name: 'asdsadasd',
          price: 10
        },
        {
          id: 8,
          url: 'https://img.yzcdn.cn/vant/apple-1.jpg',
          name: 'sss',
          price: 50
        },
        {
          id: 9,
          url: 'https://www.w3schools.com/howto/img_avatar.png',
          name: 'ss',
          price: 30
        },
        {
          id: 10,
          url: 'https://www.w3schools.com/howto/img_avatar.png',
          name: 'asdsadasd',
          price: 10
        }
      ],
      searchValue: null,
      images: [
        'https://img.yzcdn.cn/vant/apple-1.jpg',
        'https://img.yzcdn.cn/vant/apple-2.jpg',
        'https://img.yzcdn.cn/vant/apple-3.jpg',
        'https://img.yzcdn.cn/vant/apple-4.jpg'
      ],
      activeTab: 'a'
    }
  },
  methods: {
    onSearch: function () {

    },
    onLoad () {
      // axios
      this.loading = false
      // if r = null
      this.finished = true
    },
    detail (id = 1) {
      this.$router.push({ name: 'detail', params: { id } })
    }
  },
  mount: {
    fisrtLoad () {
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
</style>
