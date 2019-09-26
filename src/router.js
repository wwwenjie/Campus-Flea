import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/index', redirect: '/browse' },
    { path: '/', redirect: '/browse' },
    {
      path: '/browse',
      name: 'browse',
      component: () => import('@/views/Browse.vue')
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
      path: '/browse/detail',
      name: 'detail',
      component: () => import('@/views/Browse/Detail.vue')
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
