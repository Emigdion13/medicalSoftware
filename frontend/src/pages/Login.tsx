import { useState } from 'react';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setTimeout(() => setIsLoading(false), 1500);
  };

  return (
    <div className="login-page">
      <div className="login-left">
        <h1>Centro Médico<br />Integral</h1>
        <p>Sistema de gestión médica moderno y seguro. Administra citas, pacientes, farmacia y emergencias desde un solo lugar.</p>
        <div className="login-features">
          <div className="login-feature">
            <div className="login-feature-icon">📅</div>
            <span>Gestión de Citas</span>
          </div>
          <div className="login-feature">
            <div className="login-feature-icon">👥</div>
            <span>Pacientes</span>
          </div>
          <div className="login-feature">
            <div className="login-feature-icon">💊</div>
            <span>Farmacia</span>
          </div>
        </div>
      </div>
      <div className="login-right">
        <div className="login-form-card">
          <h2>Bienvenido</h2>
          <p className="subtitle">Ingresa tus credenciales para continuar</p>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label className="form-label">Correo electrónico</label>
              <input
                type="email"
                className="form-input"
                placeholder="doctor@centromedico.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="form-group">
              <label className="form-label">Contraseña</label>
              <input
                type="password"
                className="form-input"
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <button type="submit" className="btn btn-primary" disabled={isLoading}>
              {isLoading ? 'Ingresando...' : 'Iniciar Sesión'}
            </button>
          </form>
          <p className="login-footer">© 2025 Centro Médico Integral</p>
        </div>
      </div>
    </div>
  );
}
