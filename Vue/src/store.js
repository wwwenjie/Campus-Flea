import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    is_login: false,
    uid: null,
    token: null,
    good_id: null
  },
  mutations: {
    SET_LOGIN (state, isLogin) {
      state.is_login = isLogin
    },
    SET_UID (state, id) {
      state.uid = id
    },
    SET_TOKEN (state, token) {
      state.token = token
    },
    SET_GOOD_ID (state, id) {
      state.good_id = id
    }
  },
  actions: {}
})
