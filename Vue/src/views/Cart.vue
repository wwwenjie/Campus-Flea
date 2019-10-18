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
        <span class="card-goods__item-seller-name">{{item.seller}}</span>
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
import { SwipeCell } from 'vant'
import { Toast } from 'vant'
import mixins from '@/mixins'
import { Detail } from '@/api/goods'
import { CollectCart } from '@/api/collect'

Vue.use(Toast)

Vue.use(SwipeCell)
export default {
  name: 'Cart',
  mixins: [mixins],
  data () {
    return {
      nav: '',
      checkedAll: false,
      checkedGoods: [],
      loading: false,
      goods: [{
        id: '1',
        title: '进口香蕉',
        seller: '卖家',
        sellerId: '卖家',
        price: 200,
        url: 'https://img.yzcdn.cn/public_files/2017/10/24/2f9a36046449dafb8608e99990b3c205.jpeg'
      }, {
        id: '2',
        title: '陕西蜜梨',
        seller: '卖家',
        sellerId: '卖家',
        price: 690.05,
        url: 'https://img.yzcdn.cn/public_files/2017/10/24/f6aabd6ac5521195e01e8e89ee9fc63f.jpeg'
      }, {
        id: '3',
        title: '美国伽力果',
        seller: '卖家',
        sellerId: '卖家',
        price: 2680,
        url: 'https://img.yzcdn.cn/public_files/2017/10/24/320454216bbe9e25c7651e1fa51b31fd.jpeg'
      }]
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
        item.seller = res.seller
        this.goods.push(item)
      }).catch(err => {
        console.log(err)
      })
    } else {
      this.nav = '购物车'
      // get goods by uid
      CollectCart({
        uid: this.uid,
        type: 1
      }).then(res => {
        if (res.success) {
          res.data = this.goods
        } else {

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
