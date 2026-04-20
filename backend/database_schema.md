# Database Schema - Sistema Médico Interno

## Tablas Principales

### 0. roles
**Descripción:** Tabla centralizada para gestionar los roles del sistema.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| nombre | VARCHAR(50) UNIQUE NOT NULL | Nombre del rol (ej: staff, doctor, admin, paciente) |
| descripcion | TEXT | Descripción del rol y sus responsabilidades |
| permisos | JSONB DEFAULT '[]' | Lista de permisos asociados al rol |
| creado_el | TIMESTAMP DEFAULT NOW() | Fecha de creación |
| actualizado_el | TIMESTAMP | Última actualización |

---

### 1. usuarios
**Descripción:** Tabla central de autenticación para todo el personal médico y administrativo.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| usuario | VARCHAR(50) UNIQUE | Nombre de usuario |
| correo_electronico | VARCHAR(100) UNIQUE | Correo electrónico |
| contraseña_hash | VARCHAR(255) | Hash de la contraseña (Django lo maneja automáticamente) |
| nombre_completo | VARCHAR(100) | Nombre completo |
| numero_telefono | VARCHAR(20) | Número de teléfono |
| rol_id | INTEGER (FK) | Referencia a tabla de roles |
| esta_activo | BOOLEAN DEFAULT TRUE | Estado de la cuenta |
| creado_el | TIMESTAMP | Fecha de registro |
| actualizado_el | TIMESTAMP | Última actualización |

**Relaciones:** 
- N→1 con roles
- 1→1 con personal (si el usuario es paciente)
- 1→N con citas (como doctor)
- 1→N con registros_medicos
- 1→N con emergencias
- 1→N con registros_acceso

---

### 2. personal
**Descripción:** Perfil del personal registrado como paciente (cuando el empleado necesita atención médica).

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| usuario_id | INTEGER UNIQUE (FK) | Vínculo con usuarios (UNIQUE = 1 persona = 1 usuario) |
| codigo_empleado | VARCHAR(20) UNIQUE | Código de empleado/ID interno |
| fecha_nacimiento | DATE | Fecha de nacimiento |
| tipo_sangre | VARCHAR(3) | Tipo de sangre (A+, B-, etc.) |
| nombre_contacto_emergencia | VARCHAR(100) | Nombre del contacto de emergencia |
| telefono_contacto_emergencia | VARCHAR(20) | Teléfono de emergencia |
| notas_medicas | TEXT | Notas médicas generales |

**Relaciones:**
- 1→N con citas
- 1→N con registros_medicos
- 1→N con emergencias
- 1→N con dispensacion_medicamentos

---

### 3. citas
**Descripción:** Gestión de citas médicas.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| paciente_id | INTEGER (FK) | Persona que cita (referencia a personal) |
| doctor_id | INTEGER (FK) | Médico que atiende (referencia a usuarios) |
| fecha_cita | TIMESTAMP | Fecha y hora de la cita |
| estado | VARCHAR(20) DEFAULT 'scheduled' | Estado: scheduled, completed, cancelled |
| motivo | TEXT | Motivo de la consulta |
| notas | TEXT | Notas adicionales del médico |

**Estados:** scheduled → completed/cancelled

---

### 4. registros_medicos
**Descripción:** Historial clínico completo del paciente.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| paciente_id | INTEGER (FK) | Paciente al que pertenece el registro |
| fecha_registro | DATE | Fecha del registro |
| diagnostico | TEXT | Diagnóstico médico |
| tratamiento | TEXT | Tratamiento prescrito |
| doctor_id | INTEGER (FK) | Médico que registra |
| enfermera | VARCHAR(100) NULLABLE | Nombre de la enfermera atendiente (opcional, cliente específico) |
| datos_custom | JSONB DEFAULT '{}' | Campo flexible para campos personalizados por cliente |
| seguimiento_requerido | BOOLEAN DEFAULT FALSE | ¿Se requiere control futuro? |
| fecha_seguimiento | DATE | Fecha de seguimiento (si aplica) |

**Relaciones:**
- N→N con medicamentos (vía tabla intermedia `recetas_medicamentos`)

---

### 4.1 recetas_medicamentos (NUEVA - Tabla Intermedia)
**Descripción:** Relación muchos a muchos entre registros médicos y medicamentos.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| registro_medico_id | INTEGER (FK) | Registro médico al que pertenece la receta |
| medicamento_id | INTEGER (FK) | Medicamento prescrito |
| dosis | VARCHAR(50) NOT NULL | Dosis indicada (ej: "500mg") |
| frecuencia | VARCHAR(50) NOT NULL | Frecuencia de toma (ej: "cada 8 horas") |
| duracion | VARCHAR(50) NOT NULL | Duración del tratamiento (ej: "7 días") |
| notas | TEXT | Notas adicionales sobre la receta |

**Relaciones:**
- 1→N con registros_medicos
- 1→N con medicamentos

---

### 5. medicamentos (NUEVA)
**Descripción:** Catálogo estandarizado de medicamentos para evitar inconsistencias en nombres.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| nombre_generico | VARCHAR(100) UNIQUE NOT NULL | Nombre genérico del medicamento |
| nombre_comercial | VARCHAR(100) | Nombre comercial (opcional) |
| formula_quimica | TEXT | Fórmula química o composición |
| laboratorio | VARCHAR(100) | Laboratorio fabricante |
| descripcion | TEXT | Descripción del medicamento |
| creado_el | TIMESTAMP DEFAULT NOW() | Fecha de creación |

**Relaciones:**
- N→N con registros_medicos (vía `recetas_medicamentos`)
- 1→N con inventario_farmacia

---

### 6. emergencias
**Descripción:** Alertas y manejo de emergencias médicas.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| paciente_id | INTEGER (FK) | Persona en emergencia (referencia a personal) |
| tipo_alerta | VARCHAR(50) | Tipo: heart_attack, accident, stroke, etc. |
| descripcion | TEXT | Descripción detallada del evento |
| estado | VARCHAR(20) DEFAULT 'active' | active, resolved, ignored |
| equipo_responsable | JSONB | Equipo de respuesta asignado |
| hora_respuesta | TIMESTAMP | Hora de respuesta |
| resuelto_el | TIMESTAMP | Hora de resolución |
| creado_el | TIMESTAMP | Fecha de creación del reporte |

**Flujo:** active → resolved/ignored

---

### 7. inventario_farmacia
**Descripción:** Inventario de medicamentos disponibles (stock, precio, proveedor).

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| medicamento_id | INTEGER UNIQUE (FK) | Referencia a catálogo de medicamentos |
| cantidad_stock | INTEGER DEFAULT 0 | Cantidad en inventario |
| nivel_minimo | INTEGER DEFAULT 5 | Nivel mínimo de alerta |
| precio_unitario | DECIMAL(10,2) | Precio por unidad |
| fecha_vencimiento | DATE | Fecha de vencimiento |
| proveedor | VARCHAR(100) | Proveedor del medicamento |

**Uso:** Control de stock y alertas de reorden.
- Relación 1→1 con `medicamentos` (UNIQUE)

---

### 8. dispensacion_medicamentos
**Descripción:** Registro de entrega de medicamentos a pacientes.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| paciente_id | INTEGER (FK) | Persona que recibe (referencia a personal) |
| inventario_id | INTEGER (FK) | Medicamento del inventario |
| cantidad | INTEGER NOT NULL | Cantidad entregada |
| fecha_dispensa | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | Fecha de entrega |
| administrado_por | INTEGER (FK) | Quién administró (usuario) |
| notas | TEXT | Notas adicionales |

**Relaciones:**
- Vincula personal con inventario_farmacia
- Registro completo de quién, cuánto y cuándo

---

### 9. registros_acceso
**Descripción:** Auditoría de actividades del sistema.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| usuario_id | INTEGER (FK) | Usuario que realizó la acción |
| accion | VARCHAR(50) | Tipo: login, view_record, prescribe, delete, etc. |
| ip_address | VARCHAR(45) | Dirección IP (IPv4 o IPv6) |
| hora | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | Hora de la acción |

**Uso:** Seguridad y seguimiento de actividad.

---

## Diagrama de Relaciones

```
┌──────────┐      ┌─────────────┐      ┌──────────┐
│  roles   │◄────►│   usuarios  │◄────►│  personal  │
│   (N)    │  N   │     (1)     │  1   │    (1)     │
└──────────┘      └─────┬───────┘      └─────┬───────┘
                        │                   │
                        │ N                 │ N
                        │                   │
                        ▼                   ▼
                  ┌────────────┐    ┌──────────────┐
                  │   citas    │    │registros_med.│
                  │    (N)     │    │     (N)      │
                  └──────┬─────┘    └──────┬───────┘
                         │                 │
                         │ N               │ N
                         │                 ▼
                         │          ┌───────────────┐
                         │          │recetas_medic. │
                         │          │     (N)       │
                         │          └──────┬────────┘
                         │                 │
                         │ N               │ N
                         ▼                 ▼
                  ┌───────────┐    ┌─────────────────┐
                  │emergencias│    │  medicamentos   │
                  │   (N)     │    │      (N)        │
                  └─────┬─────┘    └──────┬──────────┘
                        │                 │
                        │ N               │ 1
                        ▼                 ▼
                  ┌──────────────┐  ┌────────────────┐
                  │registros_ac. │  │inventario_farm.│
                  │    (N)       │  │     (1)        │
                  └──────────────┘  └────────────────┘
```

---

## Notas Importantes

1. **Django maneja automáticamente:**
   - `creado_el` y `actualizado_el` con `auto_now_add` y `auto_now`
   - Hash de contraseñas (no almacenamos el hash manualmente)
   - Relaciones FK con validación automática
     - M2M e intermedias si se requieren

2. **Gestión de Roles y Medicamentos:**
   - Centraliza la gestión de roles en `roles`.
   - Usa el catálogo `medicamentos` para evitar errores tipográficos.

3. **Campos personalizados por cliente:**
   - Usa columnas NULLABLE estándar para campos que solo usa algunos clientes (ej: enfermera).
   - Usa datos_custom JSONB para campos altamente variables entre clientes.

4. **Tipos de datos PostgreSQL usados:**
   - SERIAL = INTEGER AUTO_INCREMENT
   - TIMESTAMP = fecha y hora
   - TEXT = texto largo sin límite
   - JSONB = formato JSON eficiente para consultas
   - DECIMAL(10,2) = 10 dígitos totales, 2 decimales

5. **Constraints implícitos:**
   - UNIQUE evita duplicados (usuario, correo_electronico, codigo_empleado)
   - NOT NULL obliga valores
   - FK asegura integridad referencial

¿Quieres ajustar algo en el schema antes de crear los modelos Django?
