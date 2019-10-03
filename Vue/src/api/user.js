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

export function Verify (data) {
  return request({
    url: '/user/register/verify',
    method: 'post',
    data: data
  })
}
