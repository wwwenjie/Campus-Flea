import store from '@/mixins.js'
import axios from 'axios'

// 创建一个 axios 实例
const service = axios.create({
  baseURL: process.env.VUE_APP_API,
  timeout: 5000, // 请求超时时间
  // 给后端发Json格式数据
  headers: {
    'Content-type': 'application/json'
  }
})

// 请求拦截器
service.interceptors.request.use(
  config => {
    // 在请求发送之前做一些处理
    const token = store.token
    // 让每个请求携带token-- ['X-Token']为自定义key 请根据实际情况自行修改
    config.headers['X-Token'] = token
    return config
  },
  error => {
    // 发送失败
    console.log(error)
    Promise.reject(error)
  }
)

export default service
