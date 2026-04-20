from django.test import TestCase, Client
from django.urls import reverse


class FrontendBackendIntegrationTest(TestCase):
    """Tests to verify frontend-backend connection and API endpoints."""

    def setUp(self):
        self.client = Client()

    # --- Root / Health check endpoints ---

    def test_root_returns_200(self):
        """Root URL should return 200."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin_accessible(self):
        """Admin panel URL should be reachable (redirects to login for unauthenticated)."""
        response = self.client.get('/admin/')
        # Admin redirects to login for unauthenticated users (302) is expected behavior
        self.assertIn(response.status_code, [200, 302])

    # --- Usuarios endpoints ---

    def test_usuarios_list(self):
        """Usuarios list page should return 200."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_usuarios_nuevo(self):
        """Nuevo usuario page should return 200."""
        response = self.client.get('/nuevo/')
        self.assertEqual(response.status_code, 200)

    # --- Pacientes endpoints ---

    def test_pacientes_list(self):
        response = self.client.get('/pacientes/')
        self.assertEqual(response.status_code, 200)

    def test_pacientes_nuevo(self):
        response = self.client.get('/pacientes/nuevo/')
        self.assertEqual(response.status_code, 200)

    # --- Citas endpoints ---

    def test_citas_list(self):
        response = self.client.get('/citas/')
        self.assertEqual(response.status_code, 200)

    def test_citas_nueva(self):
        response = self.client.get('/citas/nueva/')
        self.assertEqual(response.status_code, 200)

    # --- Emergencias endpoints ---

    def test_emergencias_list(self):
        response = self.client.get('/emergencias/')
        self.assertEqual(response.status_code, 200)

    def test_emergencias_nueva(self):
        response = self.client.get('/emergencias/nueva/')
        self.assertEqual(response.status_code, 200)

    # --- Farmacia endpoints ---

    def test_farmacia_inventario(self):
        response = self.client.get('/farmacia/inventario/')
        self.assertEqual(response.status_code, 200)

    def test_farmacia_dispensacion(self):
        response = self.client.get('/farmacia/dispensacion/')
        self.assertEqual(response.status_code, 200)

    def test_farmacia_dispensacion_nueva(self):
        response = self.client.get('/farmacia/dispensacion/nueva/')
        self.assertEqual(response.status_code, 200)

    # --- CORS verification ---

    def test_cors_headers_present(self):
        """CORS headers should be present for frontend-backend communication."""
        response = self.client.get('/', HTTP_ORIGIN='http://localhost:3000')
        # With CORS_ALLOW_ALL_ORIGINS = True, Access-Control-Allow-Origin should be set
        self.assertIn('Access-Control-Allow-Origin', response.headers)

    def test_cors_options_request(self):
        """OPTIONS requests should be handled properly."""
        response = self.client.options('/', HTTP_ORIGIN='http://localhost:3000')
        self.assertEqual(response.status_code, 200)
