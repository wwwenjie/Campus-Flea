<template>
  <div>
    <van-nav-bar
      left-arrow
      @click-left="onClickLeft"
      title="购物车"
    />
    <van-checkbox-group class="card-goods" v-model="checkedGoods">
      <van-checkbox
        class="card-goods__item"
        v-for="item in goods"
        :key="item.id"
        :name="item.id"
      >
        <van-swipe-cell>
          <van-card
            :title="item.title"
            :desc="item.desc"
            :num="item.num"
            :price="formatPrice(item.price)"
            :thumb="item.thumb"
          >
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

Vue.use(SwipeCell)
export default {
  name: 'Cart',
  data () {
    return {
      checkedAll: false,
      checkedGoods: [],
      loading: false,
      goods: [{
        id: '1',
        title: '进口香蕉',
        desc: '约250g，2根',
        price: 200,
        num: 1,
        thumb: 'https://img.yzcdn.cn/public_files/2017/10/24/2f9a36046449dafb8608e99990b3c205.jpeg'
      }, {
        id: '2',
        title: '陕西蜜梨',
        desc: '约600g',
        price: 690,
        num: 1,
        thumb: 'https://img.yzcdn.cn/public_files/2017/10/24/f6aabd6ac5521195e01e8e89ee9fc63f.jpeg'
      }, {
        id: '3',
        title: '美国伽力果',
        desc: '约680g/3个',
        price: 2680,
        num: 1,
        thumb: 'https://img.yzcdn.cn/public_files/2017/10/24/320454216bbe9e25c7651e1fa51b31fd.jpeg'
      }]
    }
  },
  computed: {
    submitBarText () {
      const count = this.checkedGoods.length
      return '结算' + (count ? `(${count})` : '')
    },
    totalPrice () {
      return this.goods.reduce((total, item) => total + (this.checkedGoods.indexOf(item.id) !== -1 ? item.price : 0), 0)
    }
  },
  methods: {
    formatPrice (price) {
      return (price / 100).toFixed(2)
    },
    onSubmit () {
      this.loading = true
    },
    onClickLeft () {
      this.$router.back()
    },
    onClickRemove () {
      this.goods.pop()
    },
    changeAllChecked () {
      if (this.checkedAll) {
        this.checkedGoods = []
        for (let item of this.goods) {
          this.checkedGoods.push(item.id)
        }
      } else {
        this.checkedGoods = []
      }
    }
  },
  watch: {
    checkedGoods: function () {
      if (this.checkedGoods.length === this.goods.length) {
        this.checkedAll = true
      } else {
        this.checkedAll = false
      }
    }
  }
}
</script>

<style lang="less">
  .cart {
    &-remove-button {
      height: 100%;
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

      .van-card__price {
        color: #f44;
      }
    }

    .removeButton {
      height: 100%;
    }
  }
</style>
