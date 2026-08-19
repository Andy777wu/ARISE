import axios from 'axios'

export interface ApiResponse<T> {
  code: number
  message: string
  data: T
  request_id: string
}

export const request = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 10_000,
})

request.interceptors.request.use((config) => {
  const token = localStorage.getItem('arise_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

request.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('arise_token')
    }
    return Promise.reject(error)
  },
)
