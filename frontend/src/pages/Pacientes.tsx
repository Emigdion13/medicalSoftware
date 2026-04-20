import { useState } from 'react';

const patients = [
  { id: 'P-001', name: 'María González', age: 34, blood: 'A+', phone: '+591 706-8234', lastVisit: '2025-04-15', doctor: 'Dr. Ramírez', avatarColor: 'blue' as const },
  { id: 'P-002', name: 'Carlos López', age: 58, blood: 'O-', phone: '+591 723-4561', lastVisit: '2025-04-18', doctor: 'Dra. Martínez', avatarColor: 'green' as const },
  { id: 'P-003', name: 'Ana Torres', age: 27, blood: 'B+', phone: '+591 745-1238', lastVisit: '2025-04-10', doctor: 'Dr. Ramírez', avatarColor: 'purple' as const },
  { id: 'P-004', name: 'Pedro Sánchez', age: 65, blood: 'AB+', phone: '+591 789-3456', lastVisit: '2025-04-19', doctor: 'Dr. Fernández', avatarColor: 'orange' as const },
  { id: 'P-005', name: 'Laura Díaz', age: 42, blood: 'A-', phone: '+591 712-6789', lastVisit: '2025-04-12', doctor: 'Dra. Martínez', avatarColor: 'blue' as const },
  { id: 'P-006', name: 'Roberto Méndez', age: 31, blood: 'O+', phone: '+591 734-9012', lastVisit: '2025-04-19', doctor: 'Dr. Ramírez', avatarColor: 'green' as const },
  { id: 'P-007', name: 'Sofia Ruiz', age: 53, blood: 'B-', phone: '+591 756-3456', lastVisit: '2025-04-17', doctor: 'Dr. Fernández', avatarColor: 'purple' as const },
  { id: 'P-008', name: 'Diego Herrera', age: 19, blood: 'AB-', phone: '+591 778-7890', lastVisit: '2025-04-16', doctor: 'Dra. Martínez', avatarColor: 'orange' as const },
];

export default function Pacientes() {
  const [search, setSearch] = useState('');
  const filtered = patients.filter(p => 
    p.name.toLowerCase().includes(search.toLowerCase()) || 
    p.id.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <div className="page-header">
        <div>
          <h2>Pacientes</h2>
          <p>Gestión del registro de pacientes</p>
        </div>
        <div className="page-header-actions">
          <button className="btn btn-secondary">📥 Exportar</button>
          <button className="btn btn-primary">➕ Nuevo Paciente</button>
        </div>
      </div>

      {/* Stats */}
      <div className="stats-grid" style={{ marginBottom: 28 }}>
        <StatCard icon="👥" color="#2563eb" value="156" label="Total Pacientes" />
        <StatCard icon="🆕" color="#10b981" value="23" label="Nuevos este mes" />
        <StatCard icon="🔄" color="#8b5cf6" value="45" label="Seguimiento activo" />
        <StatCard icon="🩸" color="#f59e0b" value="12" label="Tipo O- (Universal)" />
      </div>

      {/* Search */}
      <div className="filter-bar">
        <input 
          className="form-input" 
          placeholder="🔍 Buscar paciente por nombre o ID..."
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
      </div>

      {/* Patient Grid */}
      <div className="patient-grid">
        {filtered.map((p, i) => (
          <div className="patient-card" key={p.id} style={{ animationDelay: `${i * 0.08}s` }}>
            <div className="patient-card-header">
              <div className={`patient-avatar ${p.avatarColor}`}>👤</div>
              <div style={{ flex: 1 }}>
                <div className="patient-name">{p.name}</div>
                <div className="patient-id">{p.id}</div>
              </div>
            </div>
            <div className="patient-details">
              <PatientDetail icon="🎂" label={`${p.age} años`} />
              <PatientDetail icon="🩸" label={`Tipo: ${p.blood}`} />
              <PatientDetail icon="📱" label={p.phone} />
              <PatientDetail icon="👨‍⚕️" label={`Dr. ${p.doctor.replace('Dr. ', '')}`} />
              <PatientDetail icon="📅" label={`Última visita: ${new Date(p.lastVisit).toLocaleDateString('es-ES')}`} />
            </div>
            <div style={{ display: 'flex', gap: 8, marginTop: 16 }}>
              <button className="btn btn-primary" style={{ flex: 1, justifyContent: 'center', padding: '8px 12px', fontSize: 13 }}>📋 Historia Clínica</button>
              <button className="btn btn-secondary" style={{ padding: '8px 12px', fontSize: 13 }}>✏️</button>
            </div>
          </div>
        ))}
      </div>

      {filtered.length === 0 && (
        <div className="empty-state">
          <div className="icon">🔍</div>
          <h3>No se encontraron pacientes</h3>
          <p>Intenta con otro término de búsqueda</p>
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

function PatientDetail({ icon, label }: { icon: string; label: string }) {
  return (
    <div className="patient-detail-row">
      <span className="icon">{icon}</span>
      <span>{label}</span>
    </div>
  );
}
