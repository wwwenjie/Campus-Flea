<template>
  <div>
    <van-nav-bar
      left-arrow
      @click-left="routerBack"
      :title="nav"
    />
    <van-checkbox-group class="card-goods" v-model="checkedGoods">
      <van-checkbox
        class="card-goods__item"
        v-for="item in goods"
        :key="item.id"
        :name="item.id"
      >
        <span class="card-goods__item-seller-name">{{item.sellerName}}</span>
        <van-swipe-cell>
          <van-card
            :title="item.title"
            :price="item.price"
            :thumb="item.url"
          >
            <template slot="num">
              <van-button @click.stop="" @click="onClickContact(item.id)" plain hairline round type="info" text="联系卖家"/>
            </template>
          </van-card>
          <template slot="right">
            <van-button @click="onClickRemove(item.id)" square type="danger" text="删除" class="cart-remove-button"/>
          </template>
        </van-swipe-cell>
      </van-checkbox>
    </van-checkbox-group>

    <van-submit-bar
      :loading="loading"
      :price="totalPrice"
      :disabled="!checkedGoods.length"
      :button-text="submitBarText"
      @submit="onSubmit"
      class="cart-submit-bar"
    >
      <van-checkbox v-model="checkedAll" @change="changeAllChecked()" class="cart-select-all">全选</van-checkbox>
    </van-submit-bar>
  </div>
</template>

<script>
import Vue from 'vue'
import { SwipeCell, Toast } from 'vant'
import mixins from '@/mixins'
import { Detail } from '@/api/goods'
import { CollectCart } from '@/api/collect'

Vue.use(SwipeCell, Toast)
export default {
  name: 'Cart',
  mixins: [mixins],
  data () {
    return {
      nav: '',
      checkedAll: false,
      checkedGoods: [],
      loading: false,
      goods: []
    }
  },
  computed: {
    submitBarText () {
      const count = this.checkedGoods.length
      return '结算' + (count ? `(${count})` : '')
    },
    totalPrice () {
      return this.goods.reduce((total, item) => total + (this.checkedGoods.indexOf(item.id) !== -1 ? item.price * 100 : 0), 0)
    }
  },
  methods: {
    onSubmit () {
      this.loading = true
    },
    onClickRemove () {
      this.goods.pop()
    },
    onClickContact () {
    },
    changeAllChecked () {
      if (this.checkedAll) {
        this.checkedGoods = []
        for (let item of this.goods) {
          this.checkedGoods.push(item.id)
        }
      } else {
        // dont remove all checked
        if (this.checkedGoods.length !== this.goods.length - 1) {
          this.checkedGoods = []
        }
      }
    }
  },
  watch: {
    checkedGoods: function () {
      this.checkedAll = this.checkedGoods.length === this.goods.length
    }
  },
  mounted () {
    if (this.$route.params.id) {
      this.nav = '创建订单'
      // get goods by goodId
      Detail({
        id: this.goodId
      }).then(res => {
        let item = {}
        item.id = this.goodId
        item.title = res.title
        item.price = res.price
        item.url = res.url
        item.sellerId = res.sellerId
        item.sellerName = res.sellerName
        this.goods.push(item)
      }).catch(err => {
        console.log(err)
      })
    } else {
      this.nav = '购物车'
      // get goods by uid
      CollectCart({
        goodsId: null,
        uid: this.uid,
        type: 1,
        operate: null
      }).then(res => {
        if (res.success) {
          console.log(res.data)
          this.goods = res.data
        } else {
          Toast.fail('购物车为空')
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  deactivated () {
    this.$destroy()
  }
}
</script>

<style lang="less">
  .cart {
    &-remove-button {
      height: 100%;
      margin-left: 10px;
    }

    &-select-all {
      margin-left: 15px;
    }

    &-submit-bar {
      border-top: #f2f3f5 solid 1px;
    }
  }

  .card-goods {
    padding: 10px 0;
    background-color: #fff;

    &__item {
      position: relative;
      background-color: #fafafa;
      margin-top: 2vh;
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
      transition: 0.3s;
      width: 100%;
      border-radius: 8px;
      margin-bottom: 20px;

      &-seller-name {
        font-weight: 500;
        padding-left: 15px;
      }

      .van-checkbox__label {
        width: 100%;
        height: auto; // temp
        padding-left: 15px;
        box-sizing: border-box;
      }

      .van-checkbox__icon {
        top: 50%;
        left: 10px;
        z-index: 1;
        position: absolute;
        margin-top: -10px;
      }

      /*remove border*/

      .van-card {
        background-color: rgba(0, 0, 0, 0);
      }

      .van-card__title {
        font-size: 1.5em;
        line-height: normal;
      }

      .van-card__price {
        position: absolute;
        bottom: 5px;
        font-size: 1.5em;
        color: #f44;
      }
    }
  }
</style>
