import axios from 'axios';
import { API_BASE } from '../types/api';

const api = axios.create({
  baseURL: API_BASE,
  headers: { 'Content-Type': 'application/json' },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('auth_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// ── Citas API ────────────────────────────────────────────────
export const getCitas = () => api.get('/citas/').then(r => r.data);

export const getCitaById = (id: number) =>
  api.get(`/citas/${id}/`).then(r => r.data);

export const createCita = (data: Record<string, unknown>) =>
  api.post('/citas/create/', data).then(r => r.data);

export const updateCita = (id: number, data: Record<string, unknown>) =>
  api.put(`/citas/${id}/update/`, data).then(r => r.data);

export const deleteCita = (id: number) =>
  api.delete(`/citas/${id}/delete/`).then(r => r.data);

// ── Emergencias API ──────────────────────────────────────────
export const getEmergencias = () =>
  api.get('/emergencias/').then(r => r.data);

export const getEmergenciaById = (id: number) =>
  api.get(`/emergencias/${id}/`).then(r => r.data);

export const createEmergencia = (data: Record<string, unknown>) =>
  api.post('/emergencias/create/', data).then(r => r.data);

export const updateEmergencia = (id: number, data: Record<string, unknown>) =>
  api.put(`/emergencias/${id}/update/`, data).then(r => r.data);

export const deleteEmergencia = (id: number) =>
  api.delete(`/emergencias/${id}/delete/`).then(r => r.data);

export default api;
