import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    is_login: false,
    uid: null,
    good_id: null
  },
  mutations: {
    SET_UID (state, id) {
      state.uid = id
    },
    SET_LOGIN (state) {
      state.is_login = !state.is_login
    },
    SET_GOOD_ID (state, id) {
      state.good_id = id
    }
  },
  actions: {}
})
