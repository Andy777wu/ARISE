import { useCallback, useEffect, useState } from 'react'
import { getCaptcha, getCurrentUser, login, sendLoginCode } from '../api/auth'
import { useAuthStore } from '../store/authStore'
import type { CaptchaData } from '../types/auth'

const messageFrom = (error: unknown) => {
  const response = error as { response?: { data?: { message?: string } } }
  return response.response?.data?.message ?? '操作失败，请稍后重试'
}

export function useAuth() {
  const setSession = useAuthStore((state) => state.setSession)
  const token = useAuthStore((state) => state.token)
  const [captcha, setCaptcha] = useState<CaptchaData | null>(null)
  const [error, setError] = useState('')
  const [sending, setSending] = useState(false)
  const [codeCooldown, setCodeCooldown] = useState(0)

  const refreshCaptcha = useCallback(async () => {
    const response = await getCaptcha()
    setCaptcha(response.data.data)
  }, [])

  useEffect(() => {
    void refreshCaptcha().catch(() => setError('验证码加载失败'))
  }, [refreshCaptcha])

  useEffect(() => {
    if (codeCooldown === 0) return

    const timer = window.setInterval(() => {
      setCodeCooldown((seconds) => Math.max(seconds - 1, 0))
    }, 1000)

    return () => window.clearInterval(timer)
  }, [codeCooldown])

  const sendCode = async (contact: string, captchaCode: string) => {
    if (!captcha) return
    setSending(true)
    setError('')
    try {
      await sendLoginCode({
        contact,
        captcha_id: captcha.captcha_id,
        captcha_code: captchaCode,
      })
      setCodeCooldown(60)
    } catch (requestError) {
      setError(messageFrom(requestError))
      await refreshCaptcha()
      throw requestError
    } finally {
      setSending(false)
    }
  }

  const loginWithCode = async (contact: string, code: string) => {
    setError('')
    try {
      const response = await login({ contact, code })
      setSession(response.data.data.token, response.data.data.user)
      return response.data.data
    } catch (requestError) {
      setError(messageFrom(requestError))
      throw requestError
    }
  }

  const restoreSession = async () => {
    if (!token) return
    try {
      const response = await getCurrentUser()
      setSession(token, response.data.data.user)
    } catch {
      useAuthStore.getState().clearSession()
    }
  }

  return {
    captcha,
    error,
    sending,
    codeCooldown,
    refreshCaptcha,
    sendCode,
    loginWithCode,
    restoreSession,
  }
}
