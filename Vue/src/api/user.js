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

export function Auth (data) {
  return request({
    url: '/user/auth',
    method: 'post',
    data: data
  })
}

export function Info (data) {
  return request({
    url: '/user/info',
    method: 'post',
    data: data
  })
}

export function Edit (data) {
  return request({
    url: '/user/edit',
    method: 'post',
    data: data
  })
}
