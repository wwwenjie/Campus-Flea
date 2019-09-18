import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// eslint-disable-next-line import/no-duplicates
import Vant from 'vant'
// eslint-disable-next-line import/no-duplicates
import { Lazyload } from 'vant'
import 'vant/lib/index.css'

Vue.use(Vant)
Vue.use(Lazyload)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
