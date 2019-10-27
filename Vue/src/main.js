import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vueg from 'vueg'
import Vant from 'vant'
import 'vant/lib/index.css'

Vue.use(Vant)
Vue.use(vueg, router, {
  duration: '.3',
  enter: 'touchPoint',
  leave: 'fadeInLeft'
})

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
