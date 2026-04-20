import { ReactNode } from 'react';
import { useLocation } from 'react-router-dom';

interface MainLayoutProps {
  children: ReactNode;
}

const navItems = [
  { path: '/', label: 'Dashboard', icon: '📊' },
  { path: '/citas', label: 'Citas', icon: '📅' },
  { path: '/pacientes', label: 'Pacientes', icon: '👥' },
  { path: '/farmacia', label: 'Farmacia', icon: '💊' },
  { path: '/emergencias', label: 'Emergencias', icon: '🚨' },
];

export default function MainLayout({ children }: MainLayoutProps) {
  const location = useLocation();

  return (
    <div className="app-layout">
      <nav className="sidebar">
        <div className="sidebar-header">
          <div className="sidebar-logo">
            <div className="sidebar-logo-icon">🏥</div>
            <div>
              <h1>Centro Médico</h1>
              <span>Sistema Integral v2.0</span>
            </div>
          </div>
        </div>
        <ul className="sidebar-nav">
          {navItems.map(item => (
            <li key={item.path}>
              <a href={item.path} className={location.pathname === item.path ? 'active' : ''}>
                <span className="nav-icon">{item.icon}</span>
                <span>{item.label}</span>
              </a>
            </li>
          ))}
        </ul>
        <div className="sidebar-footer">
          <div className="sidebar-footer-avatar">👨‍⚕️</div>
          <div className="sidebar-footer-info">
            <div className="name">Dr. Ramírez</div>
            <div className="role">Médico General</div>
          </div>
        </div>
      </nav>
      <main className="main-content">
        {children}
      </main>
    </div>
  );
}
