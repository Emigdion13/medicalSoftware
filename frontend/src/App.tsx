import { BrowserRouter, Routes, Route, Navigate, Outlet } from 'react-router-dom';
import MainLayout from './layouts/MainLayout';
import Dashboard from './pages/Dashboard';
import Citas from './pages/Citas';
import Pacientes from './pages/Pacientes';
import Farmacia from './pages/Farmacia';
import Emergencias from './pages/Emergencias';
import Login from './pages/Login';

function LayoutWrapper() {
  return (
    <MainLayout>
      <Outlet />
    </MainLayout>
  );
}

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const token = localStorage.getItem('auth_token');
  if (!token) return <Navigate to="/login" replace />;
  return <>{children}</>;
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <LayoutWrapper />
            </ProtectedRoute>
          }
        >
          <Route index element={<Dashboard />} />
          <Route path="citas" element={<Citas />} />
          <Route path="pacientes" element={<Pacientes />} />
          <Route path="farmacia" element={<Farmacia />} />
          <Route path="emergencias" element={<Emergencias />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
