import { createStore } from 'vuex'



export const store = createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: {
      access_token: '',
      refresh_token: ''
    },
    user: {
      id: '',
      username: '',

    }
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token_access')) {
        state.token.access_token = localStorage.getItem('token_access')
        state.token.refresh_token = localStorage.getItem('token_refresh')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('username')
        state.user.id = localStorage.getItem('userid')

      } else {
        state.token.access_token = ''
        state.token.refresh_token = ''
        state.isAuthenticated = false
        state.user.id = 0
        state.user.username = ''

      }
    },
    LOGIN_SUCCESS(state, response) {
      state.token.access_token = response.data.access_token
      state.token.refresh_token = response.data.refresh_token
      state.isAuthenticated = true
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    removeToken(state) {
      state.token.access_token = ''
      state.token.refresh_token = ''
      state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
  },
  actions: {},
  modules: {
  }
})
