import { useState, useEffect } from 'react';

interface StatCard {
  title: string;
  value: number | string;
  icon: string;
  color: string;
}

function Dashboard() {
  const [stats, setStats] = useState<StatCard[]>([
    { title: 'Citas Hoy', value: 0, icon: '📅', color: '#4a90d9' },
    { title: 'Pacientes Activos', value: 0, icon: '👥', color: '#50c878' },
    { title: 'Emergencias Activas', value: 0, icon: '🚨', color: '#e74c3c' },
    { title: 'Medicamentos Stock Bajo', value: 0, icon: '💊', color: '#f39c12' },
  ]);

  return (
    <div className="dashboard">
      <h2>Dashboard</h2>
      <p className="subtitle">Resumen del sistema médico</p>

      <div className="stats-grid">
        {stats.map((stat, index) => (
          <div key={index} className="stat-card" style={{ borderTop: `4px solid ${stat.color}` }}>
            <div className="stat-icon">{stat.icon}</div>
            <div className="stat-info">
              <span className="stat-value">{stat.value}</span>
              <span className="stat-title">{stat.title}</span>
            </div>
          </div>
        ))}
      </div>

      <div className="dashboard-sections">
        <div className="section-card">
          <h3>Citas de Hoy</h3>
          <p className="empty-state">No hay citas programadas para hoy.</p>
        </div>

        <div className="section-card">
          <h3>Emergencias Activas</h3>
          <p className="empty-state">No hay emergencias activas.</p>
        </div>

        <div className="section-card">
          <h3>Inventario - Stock Bajo</h3>
          <p className="empty-state">Todo el inventario está por encima del nivel mínimo.</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
