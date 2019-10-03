import request from '@/api/axios'

export function Login (data) {
  return request({
    url: '/user/login',
    method: 'post',
    data: data
  })
}
