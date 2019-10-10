import mixins from '@/mixins'
import axios from 'axios'

// 创建一个 axios 实例
const service = axios.create({
  baseURL: process.env.VUE_APP_API,
  timeout: 10000, // 请求超时时间
  // 给后端发Json格式数据
  headers: {
    'Content-type': 'application/json'
  }
})

// 请求拦截器
service.interceptors.request.use(
  config => {
    // 让每个请求携带token-- ['X-Token']为自定义key 请根据实际情况自行修改
    config.headers['X-Token'] = mixins.token
    return config
  },
  error => {
    // 发送失败
    console.log(error)
    Promise.reject(error)
  }
)

export default service
