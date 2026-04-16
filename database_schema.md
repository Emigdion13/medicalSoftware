# Database Schema - Sistema Médico Interno

## Tablas Principales

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
| rol | VARCHAR(20) DEFAULT 'staff' | Rol: staff, doctor, admin |
| esta_activo | BOOLEAN DEFAULT TRUE | Estado de la cuenta |
| creado_el | TIMESTAMP | Fecha de registro |
| actualizado_el | TIMESTAMP | Última actualización |

**Relaciones:** 
- 1→1 con pacientes
- 1→N con citas (como doctor)
- 1→N con registros_medicos
- 1→N con emergencias
- 1→N con registros_acceso

---

### 2. pacientes
**Descripción:** Perfil del personal registrado como paciente.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| usuario_id | INTEGER UNIQUE (FK) | Vínculo con usuarios (UNIQUE = 1 paciente = 1 usuario) |
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
| paciente_id | INTEGER (FK) | Paciente que cita |
| doctor_id | INTEGER (FK) | Médico que atiende |
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
| medicamentos_prescritos | JSONB | Medicamentos (formato flexible: [{"name": "Paracetamol", "dose": "500mg"}]) |
| doctor_id | INTEGER (FK) | Médico que registra |
| seguimiento_requerido | BOOLEAN DEFAULT FALSE | ¿Se requiere control futuro? |
| fecha_seguimiento | DATE | Fecha de seguimiento (si aplica) |

**Nota:** JSONB permite almacenar estructuras flexibles para medicamentos.

---

### 5. emergencias
**Descripción:** Alertas y manejo de emergencias médicas.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| paciente_id | INTEGER (FK) | Paciente en emergencia |
| tipo_alerta | VARCHAR(50) | Tipo: heart_attack, accident, stroke, etc. |
| descripcion | TEXT | Descripción detallada del evento |
| estado | VARCHAR(20) DEFAULT 'active' | active, resolved, ignored |
| equipo_responsable | JSONB | Equipo de respuesta asignado |
| hora_respuesta | TIMESTAMP | Hora de respuesta |
| resuelto_el | TIMESTAMP | Hora de resolución |
| creado_el | TIMESTAMP | Fecha de creación del reporte |

**Flujo:** active → resolved/ignored

---

### 6. inventario_farmacia
**Descripción:** Inventario de medicamentos disponibles.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| nombre_medicamento | VARCHAR(100) NOT NULL | Nombre comercial del medicamento |
| nombre_generico | VARCHAR(100) | Nombre genérico |
| cantidad_stock | INTEGER DEFAULT 0 | Cantidad en inventario |
| nivel_minimo | INTEGER DEFAULT 5 | Nivel mínimo de alerta |
| precio_unitario | DECIMAL(10,2) | Precio por unidad |
| fecha_vencimiento | DATE | Fecha de vencimiento |
| proveedor | VARCHAR(100) | Proveedor del medicamento |

**Uso:** Control de stock y alertas de reorden.

---

### 7. dispensacion_medicamentos
**Descripción:** Registro de entrega de medicamentos a pacientes.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL (PK) | Identificador único |
| paciente_id | INTEGER (FK) | Paciente que recibe |
| inventario_id | INTEGER (FK) | Medicamento del inventario |
| cantidad | INTEGER NOT NULL | Cantidad entregada |
| fecha_dispensa | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | Fecha de entrega |
| administrado_por | INTEGER (FK) | Quién administró (usuario) |
| notas | TEXT | Notas adicionales |

**Relaciones:**
- Vincula pacientes con inventario_farmacia
- Registro completo de quién, cuánto y cuándo

---

### 8. registros_acceso
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
┌──────────┐      ┌─────────────┐
│ usuarios │◄────►│  pacientes  │
│   (1)    │  1   │     (1)     │
└────┬─────┘      └─────┬───────┘
     │                  │
     │ N                │ N
     │                  │
     ▼                  ▼
┌────────────┐    ┌──────────────┐
│   citas    │    │registros_med.│
│    (N)     │    │     (N)      │
└──────┬─────┘    └──────┬───────┘
       │                 │
       │ N               │ N
       │                 │
       ▼                 ▼
┌───────────┐    ┌─────────────────┐
│emergencias│    │dispensacion_med.│
│   (N)     │    │      (N)        │
└─────┬─────┘    └──────┬──────────┘
      │                 │
      │ N               │ N
      ▼                 ▼
┌──────────────┐  ┌────────────────┐
│registros_ac. │  │inventario_farm.│
│    (N)       │  │     (N)        │
└──────────────┘  └────────────────┘
```

---

## Notas Importantes

1. **Django maneja automáticamente:**
   - `creado_el` y `actualizado_el` con `auto_now_add` y `auto_now`
   - Hash de contraseñas (no almacenamos el hash manualmente)
   - Relaciones FK con validación automática

2. **Tipos de datos PostgreSQL usados:**
   - SERIAL = INTEGER AUTO_INCREMENT
   - TIMESTAMP = fecha y hora
   - TEXT = texto largo sin límite
   - JSONB = formato JSON eficiente para consultas
   - DECIMAL(10,2) = 10 dígitos totales, 2 decimales

3. **Constraints implícitos:**
   - UNIQUE evita duplicados (usuario, correo_electronico, codigo_empleado)
   - NOT NULL obliga valores
   - FK asegura integridad referencial

¿Quieres ajustar algo en el schema antes de crear los modelos Django?
