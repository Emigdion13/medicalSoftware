import { useState, useEffect } from 'react';
import Badge from '../components/Badge';
import { getEmergencias, createEmergencia, updateEmergencia, deleteEmergencia } from '../services/api';
import type { Emergencia as EmergenciaType } from '../types/api';

type Emergency = Omit<EmergenciaType, 'equipo_responsable'>;

const severityConfig = {
  critical: { text: 'Crítico', variant: 'danger' as const, color: '#ef4444', pulse: true },
  high: { text: 'Alto', variant: 'warning' as const, color: '#f59e0b', pulse: false },
  medium: { text: 'Moderado', variant: 'info' as const, color: '#2563eb', pulse: false },
  low: { text: 'Leve', variant: 'success' as const, color: '#10b981', pulse: false },
};

const tipoAlertaMap: Record<string, { label: string; severity: 'critical' | 'high' | 'medium' | 'low' }> = {
  heart_attack: { label: 'Infarto Agudo', severity: 'critical' },
  stroke: { label: 'Accidente Vascular', severity: 'critical' },
  respiratory: { label: 'Problema Respiratorio', severity: 'high' },
  accident: { label: 'Trauma Contusivo', severity: 'medium' },
  allergic_reaction: { label: 'Reacción Alérgica', severity: 'medium' },
  other: { label: 'Otro', severity: 'low' },
};

function EmergenciaModal({ onClose, onSubmit }: { onClose: () => void; onSubmit: (data: Record<string, unknown>) => void }) {
  const [formData, setFormData] = useState({
    paciente: '',
    tipo_alerta: 'other',
    descripcion: '',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.paciente || !formData.descripcion) return;
    onSubmit(formData);
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <h3 style={{ marginBottom: 20 }}>🚨 Nueva Emergencia</h3>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="form-label">ID del Paciente</label>
            <input
              className="form-input"
              type="number"
              placeholder="Ej: 1"
              value={formData.paciente}
              onChange={(e) => setFormData({ ...formData, paciente: e.target.value })}
              required
            />
          </div>
          <div className="form-group">
            <label className="form-label">Tipo de Alerta</label>
            <select
              className="form-select"
              value={formData.tipo_alerta}
              onChange={(e) => setFormData({ ...formData, tipo_alerta: e.target.value })}
            >
              <option value="heart_attack">Infarto</option>
              <option value="accident">Accidente</option>
              <option value="stroke">Accidente Cerebrovascular</option>
              <option value="allergic_reaction">Reacción Alérgica</option>
              <option value="respiratory">Problema Respiratorio</option>
              <option value="other">Otro</option>
            </select>
          </div>
          <div className="form-group">
            <label className="form-label">Descripción</label>
            <textarea
              className="form-textarea"
              placeholder="Describe los síntomas y acciones tomadas..."
              value={formData.descripcion}
              onChange={(e) => setFormData({ ...formData, descripcion: e.target.value })}
              required
              rows={4}
            />
          </div>
          <div className="modal-actions">
            <button type="submit" className="btn btn-danger">🚨 Crear Emergencia</button>
            <button type="button" className="btn btn-secondary" onClick={onClose}>Cancelar</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default function Emergencias() {
  const [emergencies, setEmergencies] = useState<Emergency[]>([]);
  const [filter, setFilter] = useState('all');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    fetchEmergencies();
  }, []);

  const fetchEmergencies = async () => {
    try {
      setLoading(true);
      const data = await getEmergencias();
      setEmergencies(data as Emergency[]);
      setError(null);
    } catch (err) {
      console.error('Error loading emergencies:', err);
      setError('No se pudieron cargar las emergencias. Verifica que el backend esté corriendo.');
    } finally {
      setLoading(false);
    }
  };

  const activeCount = emergencies.filter(e => e.estado === 'active').length;
  const criticalCount = emergencies.filter(e => e.estado === 'active' && (e.tipo_alerta === 'heart_attack' || e.tipo_alerta === 'stroke')).length;
  const resolvedCount = emergencies.filter(e => e.estado === 'resolved').length;

  const filtered = filter === 'all' ? emergencies : emergencies.filter(e => e.estado === filter);

  const handleCreate = async (data: Record<string, unknown>) => {
    try {
      await createEmergencia(data);
      setShowModal(false);
      fetchEmergencies();
    } catch (err) {
      console.error('Error creating emergency:', err);
      alert('Error al crear la emergencia');
    }
  };

  const handleResolve = async (id: number) => {
    try {
      await updateEmergencia(id, { estado: 'resolved', resuelto_el: new Date().toISOString() });
      fetchEmergencies();
    } catch (err) {
      console.error('Error resolving emergency:', err);
      alert('Error al resolver la emergencia');
    }
  };

  const handleDelete = async (id: number) => {
    if (!confirm('¿Estás seguro de eliminar esta emergencia?')) return;
    try {
      await deleteEmergencia(id);
      fetchEmergencies();
    } catch (err) {
      console.error('Error deleting emergency:', err);
      alert('Error al eliminar la emergencia');
    }
  };

  const formatTimeAgo = (dateString: string): string => {
    const date = new Date(dateString);
    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    if (diffMins < 1) return 'Ahora mismo';
    if (diffMins < 60) return `Hace ${diffMins} min`;
    const diffHours = Math.floor(diffMins / 60);
    if (diffHours < 24) return `Hace ${diffHours} hora${diffHours > 1 ? 's' : ''}`;
    return `Hace ${Math.floor(diffHours / 24)} día${Math.floor(diffHours / 24) > 1 ? 's' : ''}`;
  };

  return (
    <div>
      {error && (
        <div style={{ background: '#fef2f2', border: '1px solid #fecaca', borderRadius: 8, padding: 16, marginBottom: 24, color: '#dc2626', fontSize: 14 }}>
          ⚠️ {error}
        </div>
      )}

      <div className="page-header">
        <div>
          <h2>Emergencias</h2>
          <p>Monitoreo y gestión de emergencias médicas en tiempo real</p>
        </div>
        <div className="page-header-actions">
          <button className="btn btn-danger" onClick={() => setShowModal(true)}>🚨 Nueva Emergencia</button>
        </div>
      </div>

      {/* Stats */}
      <div className="stats-grid" style={{ marginBottom: 28 }}>
        <StatCard icon="🚨" color="#ef4444" value={loading ? '-' : String(activeCount)} label="Emergencias Activas" />
        <StatCard icon="💀" color="#dc2626" value={loading ? '-' : String(criticalCount)} label="Críticas Activas" />
        <StatCard icon="✅" color="#10b981" value={loading ? '-' : String(resolvedCount)} label="Resueltas Hoy" />
        <StatCard icon="📊" color="#8b5cf6" value={loading ? '-' : String(emergencies.length)} label="Total del Día" />
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
        {loading ? (
          <div style={{ padding: 40, textAlign: 'center', color: '#94a3b8' }}>Cargando emergencias...</div>
        ) : filtered.length === 0 ? (
          <div className="empty-state">
            <div className="icon">🚨</div>
            <h3>No hay emergencias {filter !== 'all' ? `con estado "${filter}"` : ''}</h3>
            <p>Todas las emergencias están resueltas</p>
          </div>
        ) : (
          filtered.map((em, i) => {
            const tipoInfo = tipoAlertaMap[em.tipo_alerta as string] || { label: 'Otro', severity: 'low' };
            const sev = em.estado === 'active' && (em.tipo_alerta === 'heart_attack' || em.tipo_alerta === 'stroke')
              ? 'critical' as const
              : (tipoInfo.severity as 'high' | 'medium' | 'low');
            const sevConfig = severityConfig[sev];

            return (
              <div
                key={em.id}
                className="emergency-card"
                style={{
                  animationDelay: `${i * 0.1}s`,
                  borderLeftColor: sevConfig.color,
                  ...(sevConfig.pulse && em.estado === 'active' ? { animation: 'pulse 2s ease-in-out infinite' } : {}),
                }}
              >
                <div className="emergency-header">
                  <span className="emergency-type">{tipoInfo.label}</span>
                  <div style={{ display: 'flex', gap: 8 }}>
                    <Badge text={sevConfig.text} variant={sevConfig.variant} />
                    <Badge text={em.estado === 'active' ? 'Activa' : em.estado === 'resolved' ? 'Resuelta' : 'Ignorada'} variant={em.estado === 'active' ? 'danger' : em.estado === 'resolved' ? 'success' : 'info'} />
                  </div>
                </div>
                <div className="emergency-patient">👤 Paciente: {em.paciente_nombre}</div>
                <div className="emergency-desc">{em.descripcion}</div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 16, marginTop: 12, fontSize: 13, color: '#94a3b8', flexWrap: 'wrap' }}>
                  <span>🕐 {formatTimeAgo(em.creado_el)}</span>
                  <span>⏱ Respuesta: {em.tiempo_respuesta ? `${Math.round(em.tiempo_respuesta)} min` : 'Sin respuesta'}</span>
                </div>
                <div className="emergency-actions">
                  {em.estado === 'active' && (
                    <>
                      <button className="btn btn-success" style={{ padding: '8px 16px', fontSize: 13 }} onClick={() => handleResolve(Number(em.id))}>✅ Resolver</button>
                      <button className="btn btn-secondary" style={{ padding: '8px 16px', fontSize: 13 }}>📋 Ver Historia</button>
                      <button className="btn btn-danger" style={{ padding: '8px 16px', fontSize: 13 }} onClick={() => handleDelete(Number(em.id))}>🗑️ Eliminar</button>
                    </>
                  )}
                  {em.estado === 'resolved' && (
                    <div style={{ display: 'flex', gap: 8 }}>
                      <button className="btn btn-secondary" style={{ padding: '8px 16px', fontSize: 13 }}>📋 Ver Detalle</button>
                      <button className="btn btn-secondary" style={{ padding: '8px 16px', fontSize: 13, color: '#ef4444' }} onClick={() => handleDelete(Number(em.id))}>🗑️ Eliminar</button>
                    </div>
                  )}
                </div>
              </div>
            );
          })
        )}
      </div>

      {showModal && <EmergenciaModal onClose={() => setShowModal(false)} onSubmit={handleCreate} />}
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
