import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/index', redirect: '/Multiply' },
    { path: '/', redirect: '/Multiply' },
    {
      path: '/Multiply',
      name: 'Multiply',
      component: () => import('@/views/Multiply.vue')
    },
    {
      path: '/browse',
      name: 'browse',
      component: () => import('@/views/Browse.vue')
    },
    {
      path: '/browse/detail',
      name: 'detail',
      component: () => import('@/views/Browse/Detail.vue')
    },
    {
      path: '/sale',
      name: 'sale',
      component: () => import('@/views/Sale.vue')
    },
    {
      path: '/user',
      name: 'user',
      component: () => import('@/views/User.vue')
    },
    {
      path: '/user/address',
      name: 'address',
      component: () => import('@/views/User/Address.vue')
    },
    {
      path: '/user/edit',
      name: 'edit',
      component: () => import('@/views/User/Edit.vue')
    },
    {
      path: '/user/edit/userInfo',
      name: 'editUserInfo',
      component: () => import('@/views/User/EditUserInfo.vue')
    },
    {
      path: '/user/order',
      name: 'order',
      component: () => import('@/views/User/Order.vue')
    },
    {
      path: '/user/order/detail',
      name: 'orderDetail',
      component: () => import('@/views/User/OrderDetail.vue')
    },
    {
      path: '/account',
      name: 'account',
      component: () => import('@/views/Account.vue')
    },
    {
      path: '/cart',
      name: 'cart',
      component: () => import('@/views/Cart.vue')
    }
  ]
})
