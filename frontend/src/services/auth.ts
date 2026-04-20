import api from './api';

export interface LoginResponse {
  token: string;
  user: {
    id: number;
    username: string;
    nombre_completo: string;
    correo_electronico: string;
    esta_activo: boolean;
  };
}

export interface RegisterData {
  username: string;
  password: string;
  nombre_completo: string;
  correo_electronico: string;
}

export const login = async (emailOrUsername: string, password: string) => {
  const response = await api.post<LoginResponse>('/login/', {
    username: emailOrUsername,
    password,
  });
  localStorage.setItem('auth_token', response.data.token);
  localStorage.setItem('user', JSON.stringify(response.data.user));
  return response.data;
};

export const register = async (data: RegisterData) => {
  const response = await api.post('/register/', data);
  return response.data;
};

export const logout = () => {
  localStorage.removeItem('auth_token');
  localStorage.removeItem('user');
};

export const getCurrentUser = () => {
  const userStr = localStorage.getItem('user');
  if (userStr) return JSON.parse(userStr);
  return null;
};

export const isAuthenticated = () => {
  return !!localStorage.getItem('auth_token');
};
