import request from '@/api/axios'

export function CollectCart (data) {
  return request({
    url: '/collect/cart',
    method: 'post',
    data: data
  })
}
