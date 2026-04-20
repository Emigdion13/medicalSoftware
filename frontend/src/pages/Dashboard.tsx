import StatCardComponent from '../components/StatCard';

function Dashboard() {
  const stats = [
    { icon: '📅', iconColor: 'blue' as const, value: '24', label: 'Citas Hoy', trend: { value: 12, up: true } },
    { icon: '👥', iconColor: 'green' as const, value: '156', label: 'Pacientes Activos', trend: { value: 8, up: true } },
    { icon: '🚨', iconColor: 'red' as const, value: '3', label: 'Emergencias Activas', trend: { value: 2, up: false } },
    { icon: '💊', iconColor: 'orange' as const, value: '12', label: 'Stock Bajo', trend: { value: 5, up: false } },
  ];

  const appointments = [
    { time: '09:00', name: 'María González', doctor: 'Dr. Ramírez', reason: 'Consulta general', status: 'scheduled' as const },
    { time: '10:30', name: 'Carlos López', doctor: 'Dra. Martínez', reason: 'Seguimiento post-operatorio', status: 'scheduled' as const },
    { time: '11:00', name: 'Ana Torres', doctor: 'Dr. Ramírez', reason: 'Resultados de laboratorio', status: 'completed' as const },
    { time: '14:00', name: 'Pedro Sánchez', doctor: 'Dr. Fernández', reason: 'Revisión anual', status: 'scheduled' as const },
    { time: '15:30', name: 'Laura Díaz', doctor: 'Dra. Martínez', reason: 'Consulta de especialidad', status: 'cancelled' as const },
  ];

  const activities = [
    { text: '<strong>Dr. Ramírez</strong> completó la consulta de <strong>Ana Torres</strong>', time: 'Hace 15 min', color: '#10b981' },
    { text: '<strong>Dra. Martínez</strong> programó una cita para <strong>Laura Díaz</strong>', time: 'Hace 32 min', color: '#2563eb' },
    { text: 'Alerta de stock bajo: <strong>Paracetamol 500mg</strong>', time: 'Hace 1 hora', color: '#ef4444' },
    { text: '<strong>Enf. Patricia</strong> registró nueva emergencia cardíaca', time: 'Hace 2 horas', color: '#f59e0b' },
    { text: '<strong>Dr. Fernández</strong> prescribió medicamento para <strong>Pedro Sánchez</strong>', time: 'Hace 3 horas', color: '#8b5cf6' },
    { text: 'Nuevo paciente registrado: <strong>Roberto Méndez</strong>', time: 'Hace 4 horas', color: '#06b6d4' },
  ];

  const emergencies = [
    { type: '🫀 Infarto', patient: 'Juan Morales', time: 'Hace 25 min', severity: 'high' as const },
    { type: '🩸 Trauma', patient: 'Sofia Ruiz', time: 'Hace 1 hora', severity: 'medium' as const },
    { type: '🫁 Asma', patient: 'Diego Herrera', time: 'Hace 2 horas', severity: 'low' as const },
  ];

  return (
    <div className="dashboard">
      {/* Welcome Banner */}
      <div className="welcome-banner">
        <div className="welcome-text">
          <h2>¡Buenos días, Doctor! 👋</h2>
          <p>Tienes 24 citas programadas para hoy. Todo está en orden.</p>
        </div>
        <div className="welcome-icon">🏥</div>
      </div>

      {/* Stats Grid */}
      <div className="stats-grid">
        {stats.map((stat, index) => (
          <StatCardComponent key={index} {...stat} />
        ))}
      </div>

      {/* Main Grid */}
      <div className="dashboard-grid">
        {/* Left Column - Appointments & Emergencies */}
        <div>
          {/* Today's Appointments */}
          <div className="section-card" style={{ marginBottom: 24 }}>
            <div className="section-header">
              <h3>📅 Citas de Hoy</h3>
              <a href="/citas" className="see-all">Ver todas →</a>
            </div>
            <div className="appointment-list">
              {appointments.map((apt, i) => (
                <div className="appointment-card" key={i} style={{ animationDelay: `${i * 0.1}s` }}>
                  <div className="appointment-time-block">
                    <span className="time">{apt.time}</span>
                  </div>
                  <div className="appointment-info">
                    <div className="name">{apt.name}</div>
                    <div className="reason">{apt.reason} · {apt.doctor}</div>
                  </div>
                  <Badge status={apt.status} />
                </div>
              ))}
            </div>
          </div>

          {/* Quick Actions */}
          <div className="section-card">
            <div className="section-header">
              <h3>⚡ Acciones Rápidas</h3>
            </div>
            <div className="quick-actions">
              <button className="quick-action-btn">
                <span className="icon">📝</span>
                <span>Nueva Cita</span>
              </button>
              <button className="quick-action-btn">
                <span className="icon">👤</span>
                <span>Nuevo Paciente</span>
              </button>
              <button className="quick-action-btn">
                <span className="icon">💊</span>
                <span>Receta</span>
              </button>
            </div>
          </div>
        </div>

        {/* Right Column - Emergencies & Activity */}
        <div>
          {/* Active Emergencies */}
          <div className="section-card" style={{ marginBottom: 24 }}>
            <div className="section-header">
              <h3>🚨 Emergencias Activas</h3>
              <a href="/emergencias" className="see-all">Ver todas →</a>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
              {emergencies.map((em, i) => (
                <div className="emergency-card" key={i} style={{ animationDelay: `${i * 0.1}s`, borderLeftColor: em.severity === 'high' ? '#ef4444' : em.severity === 'medium' ? '#f59e0b' : '#10b981' }}>
                  <div className="emergency-header">
                    <span className="emergency-type">{em.type}</span>
                    <SeverityBadge text={em.severity === 'high' ? 'Crítico' : em.severity === 'medium' ? 'Moderado' : 'Leve'} variant={em.severity === 'high' ? 'danger' : em.severity === 'medium' ? 'warning' : 'success'} />
                  </div>
                  <div className="emergency-patient">Paciente: {em.patient}</div>
                  <div style={{ fontSize: 12, color: '#94a3b8' }}>⏱ {em.time}</div>
                </div>
              ))}
            </div>
          </div>

          {/* Activity Feed */}
          <div className="section-card">
            <div className="section-header">
              <h3>📋 Actividad Reciente</h3>
            </div>
            <ul className="activity-list">
              {activities.map((act, i) => (
                <li className="activity-item" key={i} style={{ animationDelay: `${i * 0.08}s` }}>
                  <div className="activity-dot" style={{ background: act.color }} />
                  <div className="activity-content">
                    <div className="activity-text" dangerouslySetInnerHTML={{ __html: act.text }} />
                    <div className="activity-time">{act.time}</div>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

function Badge({ status }: { status: 'scheduled' | 'completed' | 'cancelled' }) {
  const config = {
    scheduled: { text: 'Programada', variant: 'info' as const },
    completed: { text: 'Completada', variant: 'success' as const },
    cancelled: { text: 'Cancelada', variant: 'danger' as const },
  };
  return <span className={`badge badge-${config[status].variant}`}>{config[status].text}</span>;
}

function SeverityBadge({ text, variant }: { text: string; variant: 'success' | 'warning' | 'danger' | 'info' | 'purple' }) {
  return <span className={`badge badge-${variant}`}>{text}</span>;
}

export default Dashboard;
