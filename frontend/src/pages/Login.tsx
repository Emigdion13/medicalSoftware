import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { login, register } from '../services/auth';

export default function Login() {
  const [isRegister, setIsRegister] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);

    try {
      if (isRegister) {
        if (password !== confirmPassword) {
          setError('Las contraseñas no coinciden');
          setIsLoading(false);
          return;
        }
        if (!fullName.trim()) {
          setError('El nombre completo es requerido');
          setIsLoading(false);
          return;
        }
        await register({
          username: email,
          password,
          nombre_completo: fullName,
          correo_electronico: email,
        });
        await login(email, password);
        navigate('/');
      } else {
        await login(email, password);
        navigate('/');
      }
    } catch (err: unknown) {
      if (err && typeof err === 'object' && 'response' in err) {
        const response = (err as { response: { data?: { error?: string } } }).response;
        setError(response.data?.error || 'Error de autenticación');
      } else {
        setError('No se pudo conectar con el servidor');
      }
    } finally {
      setIsLoading(false);
    }
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
          <div className="login-feature">
            <div className="login-feature-icon">🚨</div>
            <span>Emergencias</span>
          </div>
        </div>
      </div>
      <div className="login-right">
        <div className="login-form-card">
          <h2>{isRegister ? 'Crear Cuenta' : 'Bienvenido'}</h2>
          <p className="subtitle">{isRegister ? 'Regístrate para acceder al sistema' : 'Ingresa tus credenciales para continuar'}</p>
          <form onSubmit={handleSubmit}>
            {isRegister && (
              <div className="form-group">
                <label className="form-label">Nombre completo</label>
                <input
                  type="text"
                  className="form-input"
                  placeholder="Dr. Juan Pérez"
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                />
              </div>
            )}
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
            {isRegister && (
              <div className="form-group">
                <label className="form-label">Confirmar contraseña</label>
                <input
                  type="password"
                  className="form-input"
                  placeholder="••••••••"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                />
              </div>
            )}
            {error && <p style={{ color: '#ef4444', fontSize: 13, margin: '8px 0' }}>{error}</p>}
            <button type="submit" className="btn btn-primary" disabled={isLoading}>
              {isLoading ? 'Procesando...' : isRegister ? 'Registrarse' : 'Iniciar Sesión'}
            </button>
          </form>
          <p className="login-footer">© 2025 Centro Médico Integral</p>
          <div style={{ textAlign: 'center', marginTop: 16 }}>
            <button
              type="button"
              className="btn btn-link"
              onClick={() => { setIsRegister(!isRegister); setError(''); }}
            >
              {isRegister ? '¿Ya tienes cuenta? Inicia sesión' : '¿No tienes cuenta? Regístrate'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
