import { request, type ApiResponse } from './request'
import type { CaptchaData, LoginData, User } from '../types/auth'

export const getCaptcha = () =>
  request.get<ApiResponse<CaptchaData>>('/v1/auth/captcha/image')

export const sendLoginCode = (payload: {
  contact: string
  captcha_id: string
  captcha_code: string
}) =>
  request.post<ApiResponse<Record<string, never>>>(
    '/v1/auth/code/send',
    payload,
  )

export const login = (payload: { contact: string; code: string }) =>
  request.post<ApiResponse<LoginData>>('/v1/auth/login', payload)

export const getCurrentUser = () =>
  request.get<ApiResponse<{ user: User }>>('/v1/auth/me')

export const logout = () =>
  request.post<ApiResponse<Record<string, never>>>('/v1/auth/logout')
