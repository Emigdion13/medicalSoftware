import { ReactNode } from 'react';

interface MainLayoutProps {
  children: ReactNode;
}

export default function MainLayout({ children }: MainLayoutProps) {
  return (
    <div className="app-layout">
      <nav className="sidebar">
        <div className="sidebar-header">
          <h1>MedicSystem</h1>
        </div>
        <ul className="sidebar-nav">
          <li><a href="/">Dashboard</a></li>
          <li><a href="/citas">Citas</a></li>
          <li><a href="/pacientes">Pacientes</a></li>
          <li><a href="/farmacia">Farmacia</a></li>
          <li><a href="/emergencias">Emergencias</a></li>
        </ul>
      </nav>
      <main className="main-content">
        {children}
      </main>
    </div>
  );
}
