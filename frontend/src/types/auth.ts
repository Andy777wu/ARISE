export interface User {
  id: number
  phone: string | null
  email: string | null
}

export interface LoginData {
  token: string
  expires_in: number
  user: User
  is_new_user: boolean
}

export interface CaptchaData {
  captcha_id: string
  image_base64: string
}
