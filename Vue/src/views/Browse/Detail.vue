<template>
  <div class="goods">
    <div>
      <van-button @click="routerBack" icon="arrow-left" class="goods-button"/>
    </div>
    <van-swipe class="goods-swipe" :autoplay="3000">
      <van-swipe-item v-for="urlItem in url" :key="urlItem">
        <van-image
          lazy-load
          :src="urlItem"
          class="img"
        >
          <template v-slot:loading>
            <van-loading type="spinner" size="30"/>
          </template>
          <template v-slot:error>
            <van-icon name="photo-o" size="30"/>
            暂无图片
          </template>
        </van-image>
      </van-swipe-item>
    </van-swipe>

    <van-cell-group>
      <van-cell>
        <div class="goods-title">{{ title }}</div>
        <div class="goods-price">￥{{ price }}</div>
      </van-cell>
      <van-cell class="goods-express">
        <van-col span="10">运费：{{ express }}</van-col>
      </van-cell>
    </van-cell-group>

    <van-cell-group class="goods-cell-group">
      <van-cell :title="sellerName" icon="shop-o">
        <van-icon
          slot="right-icon"
          name="location-o"
          style="line-height: inherit;"
        >
          {{area}}
        </van-icon>
      </van-cell>
    </van-cell-group>

    <van-cell-group class="goods-cell-group">
      <van-cell title="商品介绍" class="goods-intro"></van-cell>
      <van-cell>
        <span class="span">{{detail}}</span>
      </van-cell>
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
import mixins from '@/mixins'
import { Detail } from '@/api/goods'
import { CollectCart } from '@/api/collect'

Vue.use(Toast)

export default {
  name: 'Detail',
  mixins: [mixins],
  data () {
    return {
      title: '',
      detail: '',
      url: [],
      price: '',
      express: '',
      sellerId: null,
      sellerName: '',
      area: ''
    }
  },
  methods: {
    openCart () {
      this.$router.push({ name: 'cart' })
    },
    addToFavorite () {
      CollectCart({
        goodsId: this.goodId,
        uid: this.uid,
        type: 0,
        operate: 1
      }).then(res => {
        if (res.success) {
          Toast.success(res.msg)
        } else {
          Toast.fail(res.msg)
        }
      }).catch(err => {
        console.log(err)
      })
    },
    addToCart () {
      CollectCart({
        goodsId: this.goodId,
        uid: this.uid,
        type: 1,
        operate: 1
      }).then(res => {
        if (res.success) {
          Toast.success(res.msg)
        } else {
          Toast.fail(res.msg)
        }
      }).catch(err => {
        console.log(err)
      })
    },
    buy () {
      // add goodId to change cart's style to buy
      this.$router.push({ name: 'cart', params: { id: this.goodId.toString() } })
    }
  },
  mounted () {
    // get detail by goodId
    Detail({
      id: this.goodId
    }).then(res => {
      this.title = res.title
      this.detail = res.detail
      this.url = res.url
      this.price = res.price
      this.express = res.express
      this.sellerId = res.sellerId
      this.sellerName = res.sellerName
      this.area = res.area
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style lang="less">
  .goods {
    padding-bottom: 50px;

    &-swipe {
      .img {
        display: block;
        width: 100%;
        height: auto;
        min-height: 35vh;
        max-height: 70vh;
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

      .span {
        white-space: pre-line;
        color: #000000;
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
