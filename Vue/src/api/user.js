import request from '@/api/axios'

export function Login (data) {
  return request({
    url: '/user/login',
    method: 'post',
    data: data
  })
}

export function Register (data) {
  return request({
    url: '/user/register',
    method: 'post',
    data: data
  })
}

export function Email (data) {
  return request({
    url: '/user/register/email',
    method: 'post',
    data: data
  })
}
