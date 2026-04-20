import { useState } from 'react';

const appointments = [
  { id: 1, patient: 'María González', doctor: 'Dr. Ramírez', date: '2025-04-19', time: '09:00', type: 'Consulta general', status: 'scheduled' as const, priority: 'normal' as const },
  { id: 2, patient: 'Carlos López', doctor: 'Dra. Martínez', date: '2025-04-19', time: '10:30', type: 'Post-operatorio', status: 'scheduled' as const, priority: 'high' as const },
  { id: 3, patient: 'Ana Torres', doctor: 'Dr. Ramírez', date: '2025-04-19', time: '11:00', type: 'Resultados de laboratorio', status: 'completed' as const, priority: 'normal' as const },
  { id: 4, patient: 'Pedro Sánchez', doctor: 'Dr. Fernández', date: '2025-04-19', time: '14:00', type: 'Revisión anual', status: 'scheduled' as const, priority: 'normal' as const },
  { id: 5, patient: 'Laura Díaz', doctor: 'Dra. Martínez', date: '2025-04-19', time: '15:30', type: 'Especialidad', status: 'cancelled' as const, priority: 'normal' as const },
  { id: 6, patient: 'Roberto Méndez', doctor: 'Dr. Ramírez', date: '2025-04-19', time: '16:00', type: 'Consulta general', status: 'scheduled' as const, priority: 'low' as const },
  { id: 7, patient: 'Sofia Ruiz', doctor: 'Dr. Fernández', date: '2025-04-20', time: '09:30', type: 'Consulta general', status: 'scheduled' as const, priority: 'normal' as const },
  { id: 8, patient: 'Diego Herrera', doctor: 'Dra. Martínez', date: '2025-04-20', time: '11:00', type: 'Seguimiento', status: 'scheduled' as const, priority: 'normal' as const },
];

const statusConfig = {
  scheduled: { text: 'Programada', variant: 'info' as const, dot: '#2563eb' },
  completed: { text: 'Completada', variant: 'success' as const, dot: '#10b981' },
  cancelled: { text: 'Cancelada', variant: 'danger' as const, dot: '#ef4444' },
};

const priorityConfig = {
  high: { text: 'Alta', variant: 'danger' as const },
  normal: { text: 'Normal', variant: 'info' as const },
  low: { text: 'Baja', variant: 'success' as const },
};

export default function Citas() {
  const [filter, setFilter] = useState('all');

  const filtered = filter === 'all' ? appointments : appointments.filter(a => a.status === filter);

  return (
    <div>
      <div className="page-header">
        <div>
          <h2>Gestión de Citas</h2>
          <p>Administra las citas médicas del centro</p>
        </div>
        <div className="page-header-actions">
          <button className="btn btn-secondary">📥 Exportar</button>
          <button className="btn btn-primary">➕ Nueva Cita</button>
        </div>
      </div>

      {/* Stats */}
      <div className="stats-grid" style={{ marginBottom: 28 }}>
        <StatCard icon="📅" color="#2563eb" value="8" label="Total Citas" />
        <StatCard icon="✅" color="#10b981" value="1" label="Completadas" />
        <StatCard icon="⏳" color="#f59e0b" value="5" label="Pendientes" />
        <StatCard icon="❌" color="#ef4444" value="1" label="Canceladas" />
      </div>

      {/* Filters */}
      <div className="filter-bar">
        {['all', 'scheduled', 'completed', 'cancelled'].map(f => (
          <button
            key={f}
            className={`btn ${filter === f ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setFilter(f)}
          >
            {f === 'all' ? 'Todas' : f === 'scheduled' ? 'Programadas' : f === 'completed' ? 'Completadas' : 'Canceladas'}
          </button>
        ))}
      </div>

      {/* Table */}
      <div className="section-card" style={{ overflowX: 'auto' }}>
        <table className="data-table">
          <thead>
            <tr>
              <th>Paciente</th>
              <th>Médico</th>
              <th>Fecha</th>
              <th>Hora</th>
              <th>Tipo</th>
              <th>Prioridad</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map(apt => (
              <tr key={apt.id} style={{ animation: 'fadeInUp 0.4s ease-out both' }}>
                <td style={{ fontWeight: 600 }}>{apt.patient}</td>
                <td>{apt.doctor}</td>
                <td>{new Date(apt.date).toLocaleDateString('es-ES')}</td>
                <td><span style={{ fontWeight: 600, fontFamily: 'monospace' }}>{apt.time}</span></td>
                <td>{apt.type}</td>
                <td><Badge text={priorityConfig[apt.priority].text} variant={priorityConfig[apt.priority].variant} /></td>
                <td><Badge text={statusConfig[apt.status].text} variant={statusConfig[apt.status].variant} /></td>
                <td>
                  <div style={{ display: 'flex', gap: 6 }}>
                    <button className="btn btn-secondary" style={{ padding: '6px 12px', fontSize: 12 }}>✏️ Editar</button>
                    <button className="btn btn-secondary" style={{ padding: '6px 12px', fontSize: 12, color: '#ef4444' }}>🗑️</button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function StatCard({ icon, color, value, label }: { icon: string; color: string; value: string | number; label: string }) {
  return (
    <div className="stat-card" style={{ borderTop: `4px solid ${color}` }}>
      <div className="stat-icon">{icon}</div>
      <div className="stat-info">
        <span className="stat-value">{value}</span>
        <span className="stat-label">{label}</span>
      </div>
    </div>
  );
}

function Badge({ text, variant }: { text: string; variant: 'success' | 'warning' | 'danger' | 'info' | 'purple' }) {
  return <span className={`badge badge-${variant}`}>{text}</span>;
}
