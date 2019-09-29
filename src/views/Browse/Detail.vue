<template>
  <div class="goods">
    <div>
      <van-button @click="back" icon="arrow-left" class="goods-button"/>
    </div>
    <van-swipe class="goods-swipe" :autoplay="3000">
      <van-swipe-item v-for="thumb in goods.thumb" :key="thumb">
        <img :src="thumb">
      </van-swipe-item>
    </van-swipe>

    <van-cell-group>
      <van-cell>
        <div class="goods-title">{{ goods.title }}</div>
        <div class="goods-price">{{ formatPrice(goods.price) }}</div>
      </van-cell>
      <van-cell class="goods-express">
        <van-col span="10">运费：{{ goods.express }}</van-col>
      </van-cell>
    </van-cell-group>

    <van-cell-group class="goods-cell-group">
      <van-cell title="卖家用户" icon="shop-o">
        <van-icon
          slot="right-icon"
          name="location-o"
          style="line-height: inherit;"
        >
          成都大学
        </van-icon>
      </van-cell>
    </van-cell-group>

    <van-cell-group class="goods-cell-group">
      <van-cell title="商品介绍" class="goods-intro"></van-cell>
      <van-cell
        title="之前去旅游的时候多买了一支，打算送给表姐作为生日礼物，结果撞衫了就没有送出手，送了其他，所以这个便宜卖了，非常好看的一款番茄色，我自己也在用，东西是本人亲自带回，绝对正品，如假包退，有免税店的购买记录，可以同时寄出，别问我价格为什么这么低，闲置价格出，出给有缘的小姐姐！！！！罗湖区可以见面交易，其他地方邮寄！"/>
    </van-cell-group>

    <van-goods-action>
      <van-goods-action-icon icon="cart-o" @click="openCart">
        购物车
      </van-goods-action-icon>
      <van-goods-action-icon icon="star-o" @click="addToFavorite">
        收藏
      </van-goods-action-icon>
      <van-goods-action-button type="warning" @click="addToCart">
        加入购物车
      </van-goods-action-button>
      <van-goods-action-button type="danger" @click="buy">
        立即购买
      </van-goods-action-button>
    </van-goods-action>
  </div>
</template>

<script>
import Vue from 'vue'
import { Toast } from 'vant'
import store from '@/mixins.js'

Vue.use(Toast)

export default {
  name: 'Detail',
  mixins: [store],
  data () {
    return {
      goods: {
        title: '美国伽力果（约680g/3个）',
        price: 2680,
        express: '仅面交',
        remain: 19,
        thumb: [
          'https://img.yzcdn.cn/public_files/2017/10/24/e5a5a02309a41f9f5def56684808d9ae.jpeg',
          'https://img.yzcdn.cn/public_files/2017/10/24/1791ba14088f9c2be8c610d0a6cc0f93.jpeg'
        ]
      }
    }
  },
  methods: {
    formatPrice () {
      return '¥' + (this.goods.price / 100).toFixed(2)
    },
    openCart () {
      this.$router.push({ name: 'cart' })
    },
    addToFavorite () {
      Toast.success('收藏成功')
    },
    addToCart () {
      Toast.success('已加入购物车')
    },
    buy () {
      this.$router.push({
        name: 'cart',
        params: {
          id: this.id
        }
      })
    },
    back () {
      this.$router.go(-1)
    }
  },
  mounted () {
    console.log(this.uid)
  }
}
</script>

<style lang="less">
  .goods {
    padding-bottom: 50px;

    &-swipe {
      img {
        width: 100%;
        display: block;
      }
    }

    &-title {
      font-size: 20px;
    }

    &-price {
      color: #f44;
      font-size: 20px;
      margin-top: 10px;
    }

    &-express {
      color: #999;
      font-size: 12px;
      padding: 5px 15px;
    }

    &-cell-group {
      margin: 15px 0;

      .van-cell__value {
        color: #999;
      }
    }

    &-tag {
      margin-left: 5px;
    }

    &-button {
      position: absolute;
      z-index: 2;
      margin: 5vw;
      color: white;
      background-color: #4D4D4D;
      border: 1px solid #4D4D4D;
      border-radius: 50%;
      opacity: .7;
    }

    &-intro {
      font-size: 16px;
    }
  }
</style>
