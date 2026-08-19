import { Button, Input, Toast } from 'antd-mobile'
import { useState } from 'react'
import { useAuth } from '../../hooks/useAuth'
import '../../styles/login.css'

export function LoginPage() {
  const { captcha, error, sending, refreshCaptcha, sendCode, loginWithCode } =
    useAuth()
  const [contact, setContact] = useState('')
  const [captchaCode, setCaptchaCode] = useState('')
  const [code, setCode] = useState('')

  const requestCode = async () => {
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
      <section className="login-card">
        <p className="eyebrow">ARISE</p>
        <h1>家庭资产账本</h1>
        <p className="subtitle">使用手机号或邮箱验证码登录</p>
        <Input
          placeholder="手机号或邮箱"
          value={contact}
          onChange={setContact}
          clearable
        />
        <div className="captcha-row">
          <Input
            placeholder="图片验证码"
            value={captchaCode}
            onChange={setCaptchaCode}
            clearable
          />
          {captcha && (
            <img
              alt="图片验证码"
              className="captcha-image"
              src={`data:image/svg+xml;base64,${captcha.image_base64}`}
              onClick={() => void refreshCaptcha()}
            />
          )}
        </div>
        <Button
          block
          color="primary"
          loading={sending}
          onClick={() => void requestCode()}
        >
          发送验证码
        </Button>
        <Input
          placeholder="短信或邮件验证码"
          value={code}
          onChange={setCode}
          clearable
        />
        {error && <p className="form-error">{error}</p>}
        <Button block color="primary" onClick={() => void submit()}>
          登录 / 自动注册
        </Button>
      </section>
    </main>
  )
}
