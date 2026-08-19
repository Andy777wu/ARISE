import { request, type ApiResponse } from './request'

export const getHealth = () =>
  request.get<ApiResponse<{ status: string }>>('/v1/health')
