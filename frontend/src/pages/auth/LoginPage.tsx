import { useState } from 'react'
import { Toast } from 'antd-mobile'
import { useAuth } from '../../hooks/useAuth'
import '../../styles/login.css'

export function LoginPage() {
  const {
    captcha,
    error,
    sending,
    codeCooldown,
    refreshCaptcha,
    sendCode,
    loginWithCode,
  } = useAuth()
  const [contact, setContact] = useState('')
  const [captchaCode, setCaptchaCode] = useState('')
  const [code, setCode] = useState('')

  const requestCode = async () => {
    if (sending || codeCooldown > 0) return

    try {
      await sendCode(contact, captchaCode)
      Toast.show('验证码已发送，请查看开发服务日志')
    } catch {
      // The hook exposes a user-facing error message below the form.
    }
  }

  const submit = async () => {
    try {
      const result = await loginWithCode(contact, code)
      Toast.show(result.is_new_user ? '欢迎加入 ARISE' : '登录成功')
    } catch {
      // The hook exposes a user-facing error message below the form.
    }
  }

  return (
    <main className="login-page">
      <div className="login-container">
        <header className="login-header">
          <div className="brand-icon" aria-hidden="true">▰</div>
          <h1>ARISE</h1>
          <p>家庭资产管理</p>
        </header>

        <section className="login-card" aria-label="登录">
          <form
            className="login-form"
            onSubmit={(event) => {
              event.preventDefault()
              void submit()
            }}
          >
            <label className="input-field">
              <input
                autoComplete="username"
                placeholder="请输入手机号或邮箱"
                value={contact}
                onChange={(event) => setContact(event.target.value)}
              />
            </label>
            <div className="input-field captcha-field">
              <input
                placeholder="请输入图形验证码"
                value={captchaCode}
                onChange={(event) => setCaptchaCode(event.target.value)}
              />
              <button
                className="captcha-action"
                type="button"
                aria-label="刷新图形验证码"
                onClick={() => void refreshCaptcha()}
              >
                {captcha && (
                  <img
                    alt="图形验证码"
                    src={`data:image/svg+xml;base64,${captcha.image_base64}`}
                  />
                )}
              </button>
            </div>
            <div className="input-field code-field">
              <input
                autoComplete="one-time-code"
                inputMode="numeric"
                placeholder="请输入验证码"
                value={code}
                onChange={(event) => setCode(event.target.value)}
              />
              <button
                className="send-code-button"
                type="button"
                disabled={sending || codeCooldown > 0}
                onClick={() => void requestCode()}
              >
                {sending
                  ? '发送中…'
                  : codeCooldown > 0
                    ? `${codeCooldown}s 后重发`
                    : '获取验证码'}
              </button>
            </div>
            {error && <p className="form-error">{error}</p>}
            <button className="login-submit" type="submit">
              登录
            </button>
          </form>
        </section>

        <footer className="login-footer">
          <p>首次登录将自动注册，登录即代表同意</p>
          <p>
            <a href="#agreement">《用户协议》</a> 和 <a href="#privacy">《隐私政策》</a>
          </p>
        </footer>
      </div>
    </main>
  )
}
