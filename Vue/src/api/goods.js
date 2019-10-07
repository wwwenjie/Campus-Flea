import request from '@/api/axios'

export function ImgUpload (data) {
  return request({
    // for dev mode, use cors-anywhere
    baseURL: 'https://cors-anywhere.herokuapp.com/https://sm.ms',
    url: '/api/v2/upload',
    method: 'post',
    data: data,
    headers: {
      'Content-type': 'multipart/form-data',
      // API key
      'Authorization': 'OWS2NyimHVGp75WX9hO2eu1WPDmiqkgN'
    }
  })
}

export function Upload (data) {
  return request({
    url: '/goods/upload',
    method: 'post',
    data: data
  })
}

export function Detail (data) {
  return request({
    url: '/goods/detail',
    method: 'post',
    data: data
  })
}

export function Browse (data) {
  return request({
    url: '/goods/browse',
    method: 'post',
    data: data
  })
}
