import { request } from './request'

export interface ApiResponse<T> {
  code: number
  message: string
  data: T
  request_id: string
}

export const getHealth = () =>
  request.get<ApiResponse<{ status: string }>>('/v1/health')
