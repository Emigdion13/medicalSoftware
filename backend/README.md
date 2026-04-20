# README del Sistema Médico Interno

Este proyecto está organizado en dos carpetas separadas: `backend/` y `frontend/`.

## Backend (Django)

El backend proporciona la API RESTful para gestionar el sistema médico.

### Instalación

1. Acceder a la carpeta backend:
   ```bash
   cd backend
   ```

2. Crear entorno virtual:
   ```bash
   python -m venv venv
   ```

3. Activar el entorno:
   ```bash
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

4. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. Configurar la base de datos (PostgreSQL):
   
   Usar Docker Compose (recomendado):
   ```bash
   docker-compose up -d
   ```
   
   O configurar manualmente en `medic_system/settings.py`.

6. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

7. Crear superusuario:
   ```bash
   python manage.py createsuperuser
   ```

8. Ejecutar servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

### Estructura del Backend

```
backend/
├── manage.py
├── medic_system/          # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
├── usuarios/              # Gestión de usuarios y roles
├── pacientes/             # Perfiles del personal
├── citas/                 # Citas médicas
├── emergencias/           # Alertas y emergencias médicas
├── farmacia/              # Medicamentos e inventario
└── requirements.txt
```

### Aplicaciones Disponibles

- **roles**: Gestión centralizada de roles y permisos
- **usuarios**: Usuarios del sistema con roles asociados
- **pacientes**: Perfiles del personal registrado como pacientes
- **citas**: Programación y gestión de citas médicas
- **emergencias**: Alertas y manejo de emergencias médicas
- **farmacia**: Catálogo de medicamentos, inventario y dispensación

### Endpoints Principales

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/admin/` | GET/POST | Panel de administración Django |
| `/api/usuarios/` | GET/POST | Lista y creación de usuarios |
| `/api/pacientes/` | GET/POST | Lista y creación de pacientes |
| `/api/citas/` | GET/POST | Lista y creación de citas |
| `/api/emergencias/` | GET/POST | Lista y creación de emergencias |
| `/api/farmacia/medicamentos/` | GET/POST | Catálogo de medicamentos |
| `/api/farmacia/inventario/` | GET/POST | Inventario de farmacia |

### Modelos Principales

**Usuarios**
- Usuario: Credenciales y datos personales con rol asociado
- Role: Roles del sistema con permisos personalizados

**Pacientes**
- Personal: Perfil completo del personal registrado como paciente

**Citas**
- Cita: Programación de citas médicas con doctor asignado

**Emergencias**
- Emergencia: Alertas médicas con seguimiento de respuesta

**Farmacia**
- Medicamento: Catálogo estandarizado
- InventarioFarmacia: Stock, precios y proveedores
- RegistroMedico: Historial clínico del paciente
- RecetaMedicamento: Relación medicamentos-con-registro
- DispensacionMedicamentos:Registro de entrega a pacientes

### Tecnologías Backend

- Python 3.10+
- Django 4.2+
- PostgreSQL 15+
- Docker & Docker Compose

---

## Frontend (React + TypeScript)

El frontend es una aplicación moderna construida con React y Vite.

### Instalación

1. Acceder a la carpeta frontend:
   ```bash
   cd frontend
   ```

2. Instalar dependencias:
   ```bash
   npm install
   ```

3. Ejecutar servidor de desarrollo:
   ```bash
   npm run dev
   ```

4. Construir para producción:
   ```bash
   npm run build
   ```

### Tecnologías Frontend

- React 19
- TypeScript 6.0+
- Vite 8.0+
- ESLint + Prettier (configurado)

---

## Docker

Para levantar todo el entorno con PostgreSQL:

```bash
cd backend
docker-compose up -d
```

El servicio estará disponible en `http://localhost:8000`.

## Licencia

Propietario - Sistema Médico Interno
