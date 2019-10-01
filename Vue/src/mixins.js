import {
  mapState,
  mapMutations
} from 'vuex'

import tmp from '@/store.js'

export default {
  store: tmp,
  computed: mapState({
    isLogin: state => state.is_login,
    uid: state => state.uid,
    goodId: state => state.good_id
  }),
  methods: {
    ...mapMutations({
      setLogin: 'SET_LOGIN',
      setUid: 'SET_UID',
      setGoodId: 'SET_GOOD_ID'
    }),
    routerBack () {
      this.$router.back()
    }
  }
}
