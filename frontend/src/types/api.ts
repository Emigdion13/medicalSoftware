export const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

// ── Cita types ───────────────────────────────────────────────
export interface Cita {
  id: number;
  paciente: number;
  paciente_nombre: string;
  doctor: number | null;
  doctor_nombre: string | null;
  fecha_cita: string;
  estado: 'scheduled' | 'completed' | 'cancelled';
  motivo: string;
  notas: string;
  creado_el: string;
  actualizado_el: string;
  esta_vencida: boolean;
}

// ── Emergencia types ────────────────────────────────────────
export interface Emergencia {
  id: number;
  paciente: number;
  paciente_nombre: string;
  tipo_alerta: 'heart_attack' | 'accident' | 'stroke' | 'allergic_reaction' | 'respiratory' | 'other';
  descripcion: string;
  estado: 'active' | 'resolved' | 'ignored';
  equipo_responsable: Record<string, unknown> | null;
  hora_respuesta: string | null;
  resuelto_el: string | null;
  tiempo_respuesta: number | null;
  creado_el: string;
}

// ── Dashboard stats types ───────────────────────────────────
export interface DashboardStats {
  totalCitas: number;
  citasHoy: number;
  emergenciasActivas: number;
  stockBajo: number;
}

export interface ActividadReciente {
  text: string;
  time: string;
  color: string;
}

export interface EmergenciaDashboard {
  type: string;
  patient: string;
  time: string;
  severity: 'high' | 'medium' | 'low';
}

export interface CitaDashboard {
  time: string;
  name: string;
  doctor: string;
  reason: string;
  status: 'scheduled' | 'completed' | 'cancelled';
}
