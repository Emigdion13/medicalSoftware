import { useState, useEffect } from 'react';
import StatCardComponent from '../components/StatCard';
import BadgeComponent from '../components/Badge';
import { getCitas, getEmergencias } from '../services/api';
import type { Cita, Emergencia } from '../types/api';

function Dashboard() {
  const [stats, setStats] = useState<Array<{ icon: string; iconColor: 'blue' | 'green' | 'red' | 'orange' | 'purple' | 'cyan'; value: string; label: string; trend?: { value: number; up: boolean } }>>([]);
  const [appointments, setAppointments] = useState<Array<{ time: string; name: string; doctor: string; reason: string; status: 'scheduled' | 'completed' | 'cancelled' }>>([]);
  const [activities, setActivities] = useState<Array<{ text: string; time: string; color: string }>>([]);
  const [emergencies, setEmergencies] = useState<Array<{ type: string; patient: string; time: string; severity: 'high' | 'medium' | 'low' }>>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [citasData, emergenciasData] = await Promise.all([
          getCitas(),
          getEmergencias(),
        ]);

        const citas = citasData as Record<string, unknown>[];
        const emergencias = emergenciasData as Record<string, unknown>[];

        // Stats
        const today = new Date().toISOString().split('T')[0];
        const citasHoy = citas.filter((c: Record<string, unknown>) => c.fecha_cita && (c.fecha_cita as string).startsWith(today));
        const emergenciasActivas = emergencias.filter((e: Record<string, unknown>) => e.estado === 'active');

        setStats([
          { icon: '📅', iconColor: 'blue' as const, value: String(citasHoy.length), label: 'Citas Hoy', trend: { value: 12, up: true } },
          { icon: '👥', iconColor: 'green' as const, value: String(citas.length), label: 'Pacientes Activos', trend: { value: 8, up: true } },
          { icon: '🚨', iconColor: 'red' as const, value: String(emergenciasActivas.length), label: 'Emergencias Activas', trend: { value: 2, up: false } },
          { icon: '💊', iconColor: 'orange' as const, value: '12', label: 'Stock Bajo', trend: { value: 5, up: false } },
        ]);

        // Appointments - today's scheduled/completed
        const todayAppointments = citasHoy
          .filter((c: Record<string, unknown>) => c.estado === 'scheduled' || c.estado === 'completed')
          .slice(0, 5)
          .map((c: Record<string, unknown>) => ({
            time: c.fecha_cita ? (c.fecha_cita as string).substring(11, 16) : '',
            name: c.paciente_nombre as string,
            doctor: c.doctor_nombre as string,
            reason: c.motivo as string,
            status: (c.estado as 'scheduled' | 'completed' | 'cancelled') || 'scheduled',
          }));
        setAppointments(todayAppointments);

        // Active emergencies for dashboard
        const activeEmergencies = emergencias.filter((e: Record<string, unknown>) => e.estado === 'active') as Record<string, unknown>[];
        const severityMap: Record<string, string> = { heart_attack: 'high', stroke: 'high', respiratory: 'medium', allergic_reaction: 'medium', accident: 'medium', other: 'low' };
        const typeLabels: Record<string, string> = { heart_attack: '🫀 Infarto', accident: '🩸 Trauma', stroke: '🧠 ACV', allergic_reaction: '⚡ Alergia', respiratory: '🫁 Asma', other: '❓ Otro' };

        const formattedEmergencies = activeEmergencies.slice(0, 3).map((e: Record<string, unknown>) => ({
          type: (typeLabels[e.tipo_alerta as string] || '❓ Otro') + ' ' + ((e.tipo_alerta === 'heart_attack' ? 'Infarto' : e.tipo_alerta === 'accident' ? 'Trauma' : e.tipo_alerta === 'stroke' ? 'ACV' : e.tipo_alerta === 'allergic_reaction' ? 'Alergia' : e.tipo_alerta === 'respiratory' ? 'Asma' : 'Otro')),
          patient: e.paciente_nombre as string,
          time: formatTimeAgo(e.creado_el as string),
          severity: (severityMap[e.tipo_alerta as string] || 'low') as 'high' | 'medium' | 'low',
        }));
        setEmergencies(formattedEmergencies);

        // Activity feed - combine citas and emergencias
        const activities: Array<{ text: string; time: string; color: string }> = [];
        
        citas.slice(0, 3).forEach((c: Record<string, unknown>) => {
          const statusText = c.estado === 'completed' ? `completó la consulta de ${c.paciente_nombre}` : 
                           c.estado === 'cancelled' ? `canceló la cita de ${c.paciente_nombre}` :
                           `programó una cita para ${c.paciente_nombre}`;
          activities.push({
            text: `<strong>${c.doctor_nombre}</strong> ${statusText}`,
            time: formatTimeAgo(c.creado_el as string),
            color: c.estado === 'completed' ? '#10b981' : c.estado === 'cancelled' ? '#ef4444' : '#2563eb',
          });
        });

        emergencias.slice(0, 2).forEach((e: Record<string, unknown>) => {
          activities.push({
            text: `Alerta de emergencia: <strong>${e.paciente_nombre}</strong> - ${tipoAlertaLabel(e.tipo_alerta as string)}`,
            time: formatTimeAgo(e.creado_el as string),
            color: e.estado === 'active' ? '#f59e0b' : '#10b981',
          });
        });

        setActivities(activities.slice(0, 6));
        setError(null);
      } catch (err) {
        console.error('Error loading dashboard data:', err);
        setError('No se pudieron cargar los datos del dashboard. Verifica que el backend esté corriendo en localhost:8000.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const greeting = getGreeting();

  return (
    <div className="dashboard">
      {error && (
        <div style={{ background: '#fef2f2', border: '1px solid #fecaca', borderRadius: 8, padding: 16, marginBottom: 24, color: '#dc2626', fontSize: 14 }}>
          ⚠️ {error}
        </div>
      )}

      {/* Welcome Banner */}
      <div className="welcome-banner">
        <div className="welcome-text">
          <h2>¡{greeting}, Doctor! 👋</h2>
          <p>Tienes {appointments.length} citas programadas para hoy. Todo está en orden.</p>
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
        {/* Left Column - Appointments & Quick Actions */}
        <div>
          {/* Today's Appointments */}
          <div className="section-card" style={{ marginBottom: 24 }}>
            <div className="section-header">
              <h3>📅 Citas de Hoy</h3>
              <a href="/citas" className="see-all">Ver todas →</a>
            </div>
            {loading ? (
              <div style={{ padding: 24, textAlign: 'center', color: '#94a3b8' }}>Cargando citas...</div>
            ) : appointments.length === 0 ? (
              <div style={{ padding: 24, textAlign: 'center', color: '#94a3b8' }}>No hay citas para hoy</div>
            ) : (
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
                    <BadgeComponent text={apt.status === 'scheduled' ? 'Programada' : apt.status === 'completed' ? 'Completada' : 'Cancelada'} variant={apt.status === 'scheduled' ? 'info' : apt.status === 'completed' ? 'success' : 'danger'} />
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Quick Actions */}
          <div className="section-card">
            <div className="section-header">
              <h3>⚡ Acciones Rápidas</h3>
            </div>
            <div className="quick-actions">
              <button className="quick-action-btn" onClick={() => window.location.href = '/citas'}>
                <span className="icon">📝</span>
                <span>Nueva Cita</span>
              </button>
              <button className="quick-action-btn" onClick={() => window.location.href = '/pacientes'}>
                <span className="icon">👤</span>
                <span>Nuevo Paciente</span>
              </button>
              <button className="quick-action-btn" onClick={() => window.location.href = '/emergencias'}>
                <span className="icon">🚨</span>
                <span>Emergencia</span>
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
            {loading ? (
              <div style={{ padding: 24, textAlign: 'center', color: '#94a3b8' }}>Cargando emergencias...</div>
            ) : emergencies.length === 0 ? (
              <div style={{ padding: 24, textAlign: 'center', color: '#94a3b8' }}>No hay emergencias activas</div>
            ) : (
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
            )}
          </div>

          {/* Activity Feed */}
          <div className="section-card">
            <div className="section-header">
              <h3>📋 Actividad Reciente</h3>
            </div>
            {loading ? (
              <div style={{ padding: 24, textAlign: 'center', color: '#94a3b8' }}>Cargando actividad...</div>
            ) : activities.length === 0 ? (
              <div style={{ padding: 24, textAlign: 'center', color: '#94a3b8' }}>No hay actividad reciente</div>
            ) : (
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
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

function getGreeting(): string {
  const hour = new Date().getHours();
  if (hour < 12) return 'Buenos días';
  if (hour < 18) return 'Buenas tardes';
  return 'Buenas noches';
}

function formatTimeAgo(dateString: string): string {
  const date = new Date(dateString);
  const now = new Date();
  const diffMs = now.getTime() - date.getTime();
  const diffMins = Math.floor(diffMs / 60000);
  
  if (diffMins < 1) return 'Ahora mismo';
  if (diffMins < 60) return `Hace ${diffMins} min`;
  const diffHours = Math.floor(diffMins / 60);
  if (diffHours < 24) return `Hace ${diffHours} hora${diffHours > 1 ? 's' : ''}`;
  const diffDays = Math.floor(diffHours / 24);
  return `Hace ${diffDays} día${diffDays > 1 ? 's' : ''}`;
}

function tipoAlertaLabel(tipo: string): string {
  const labels: Record<string, string> = {
    heart_attack: 'Infarto',
    accident: 'Accidente',
    stroke: 'ACV',
    allergic_reaction: 'Reacción Alérgica',
    respiratory: 'Problema Respiratorio',
    other: 'Otro',
  };
  return labels[tipo] || tipo;
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
