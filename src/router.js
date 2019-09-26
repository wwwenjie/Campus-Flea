import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('@/views/Browse.vue')
    },
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
    }
  ]
})
