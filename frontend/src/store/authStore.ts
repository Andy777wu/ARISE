import { create } from 'zustand'
import type { User } from '../types/auth'

interface AuthState {
  token: string | null
  user: User | null
  setSession: (token: string, user: User) => void
  clearSession: () => void
}

export const useAuthStore = create<AuthState>((set) => ({
  token: localStorage.getItem('arise_token'),
  user: null,
  setSession: (token, user) => {
    localStorage.setItem('arise_token', token)
    set({ token, user })
  },
  clearSession: () => {
    localStorage.removeItem('arise_token')
    set({ token: null, user: null })
  },
}))
