import { useState } from 'react';

const emergencies = [
  { id: 1, patient: 'Juan Morales', age: 67, type: 'Infarto Agudo', description: 'Paciente presenta dolor torácico intenso con irradiación a brazo izquierdo. ECG muestra elevación del segmento ST.', status: 'active' as const, severity: 'critical' as const, time: '2025-04-19 14:35', team: ['Dr. Ramírez', 'Enf. Patricia'], resolved: false },
  { id: 2, patient: 'Sofia Ruiz', age: 34, type: 'Trauma Contusivo', description: 'Accidente de tráfico con trauma en región abdominal. Se requiere evaluación urgente y posible intervención quirúrgica.', status: 'active' as const, severity: 'high' as const, time: '2025-04-19 13:10', team: ['Dra. Martínez', 'Dr. Fernández'], resolved: false },
  { id: 3, patient: 'Diego Herrera', age: 22, type: 'Crisis Asmática', description: 'Paciente joven con crisis asmática moderada. Se administra broncodilatador y se monitorea saturación.', status: 'resolved' as const, severity: 'medium' as const, time: '2025-04-19 11:45', team: ['Dr. Ramírez'], resolved: true },
  { id: 4, patient: 'Carmen Flores', age: 55, type: 'Reacción Alérgica', description: 'Paciente presenta urticaria generalizada y prurito intenso tras administración de antibiótico. Se administra antihistamínico.', status: 'resolved' as const, severity: 'medium' as const, time: '2025-04-19 09:20', team: ['Dra. Martínez'], resolved: true },
  { id: 5, patient: 'Luis Paredes', age: 78, type: 'Accidente Vascular', description: 'Paciente geriátrico con signos de ACV. Se realiza tomografía y se inicia protocolo de trombólisis.', status: 'active' as const, severity: 'critical' as const, time: '2025-04-19 15:02', team: ['Dr. Fernández', 'Dra. Martínez', 'Enf. Patricia'], resolved: false },
];

const severityConfig = {
  critical: { text: 'Crítico', variant: 'danger' as const, color: '#ef4444', pulse: true },
  high: { text: 'Alto', variant: 'warning' as const, color: '#f59e0b', pulse: false },
  medium: { text: 'Moderado', variant: 'info' as const, color: '#2563eb', pulse: false },
  low: { text: 'Leve', variant: 'success' as const, color: '#10b981', pulse: false },
};

export default function Emergencias() {
  const [filter, setFilter] = useState('all');

  const activeCount = emergencies.filter(e => e.status === 'active').length;
  const criticalCount = emergencies.filter(e => e.severity === 'critical' && e.status === 'active').length;

  const filtered = filter === 'all' ? emergencies : emergencies.filter(e => e.status === filter);

  return (
    <div>
      <div className="page-header">
        <div>
          <h2>Emergencias</h2>
          <p>Monitoreo y gestión de emergencias médicas en tiempo real</p>
        </div>
        <div className="page-header-actions">
          <button className="btn btn-danger">🚨 Nueva Emergencia</button>
        </div>
      </div>

      {/* Stats */}
      <div className="stats-grid" style={{ marginBottom: 28 }}>
        <StatCard icon="🚨" color="#ef4444" value={activeCount} label="Emergencias Activas" />
        <StatCard icon="💀" color="#dc2626" value={criticalCount} label="Críticas Activas" />
        <StatCard icon="✅" color="#10b981" value={emergencies.filter(e => e.status === 'resolved').length} label="Resueltas Hoy" />
        <StatCard icon="📊" color="#8b5cf6" value={emergencies.length} label="Total del Día" />
      </div>

      {/* Filters */}
      <div className="filter-bar">
        {['all', 'active', 'resolved'].map(f => (
          <button
            key={f}
            className={`btn ${filter === f ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setFilter(f)}
          >
            {f === 'all' ? 'Todas' : f === 'active' ? 'Activas' : 'Resueltas'}
          </button>
        ))}
      </div>

      {/* Emergency Cards */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
        {filtered.map((em, i) => (
          <div 
            className="emergency-card" 
            key={em.id} 
            style={{ 
              animationDelay: `${i * 0.1}s`,
              borderLeftColor: severityConfig[em.severity].color,
              ...(severityConfig[em.severity].pulse && em.status === 'active' ? { animation: 'pulse 2s ease-in-out infinite' } : {})
            }}
          >
            <div className="emergency-header">
              <span className="emergency-type">{em.type}</span>
              <div style={{ display: 'flex', gap: 8 }}>
                <Badge text={severityConfig[em.severity].text} variant={severityConfig[em.severity].variant} />
                <Badge text={em.status === 'active' ? 'Activa' : 'Resuelta'} variant={em.status === 'active' ? 'danger' : 'success'} />
              </div>
            </div>
            <div className="emergency-patient">👤 Paciente: {em.patient} ({em.age} años)</div>
            <div className="emergency-desc">{em.description}</div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 16, marginTop: 12, fontSize: 13, color: '#94a3b8' }}>
              <span>🕐 {em.time}</span>
              <span>👨‍⚕️ Equipo: {em.team.join(', ')}</span>
            </div>
            <div className="emergency-actions">
              {em.status === 'active' && (
                <>
                  <button className="btn btn-success" style={{ padding: '8px 16px', fontSize: 13 }}>✅ Resolver</button>
                  <button className="btn btn-secondary" style={{ padding: '8px 16px', fontSize: 13 }}>📋 Ver Historia</button>
                  <button className="btn btn-secondary" style={{ padding: '8px 16px', fontSize: 13 }}>📞 Contactar</button>
                </>
              )}
              {em.status === 'resolved' && (
                <button className="btn btn-secondary" style={{ padding: '8px 16px', fontSize: 13 }}>📋 Ver Detalle</button>
              )}
            </div>
          </div>
        ))}
      </div>

      {filtered.length === 0 && (
        <div className="empty-state">
          <div className="icon">🚨</div>
          <h3>No hay emergencias {filter !== 'all' ? `con estado "${filter}"` : ''}</h3>
          <p>Todas las emergencias están resueltas</p>
        </div>
      )}
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
