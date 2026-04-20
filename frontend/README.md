# Centro Médico - Frontend

Sistema de gestión integral para centros médicos, desarrollado con **React 19**, **TypeScript** y **Vite**. Interfaz moderna, responsive y con animaciones fluidas.

## 📋 Tabla de Contenidos

- [Tecnologías](#tecnologías)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Comandos Disponibles](#comandos-disponibles)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Rutas de la Aplicación](#rutas-de-la-aplicación)
- [Páginas](#páginas)
  - [Dashboard](#dashboard-)
  - [Citas](#citas-)
  - [Pacientes](#pacientes-)
  - [Farmacia](#farmacia-)
  - [Emergencias](#emergencias-)
- [Componentes Reutilizables](#componentes-reutilizables)
- [Diseño y Estilo](#diseño-y-estilo)
- [Animaciones](#animaciones)
- [Arquitectura](#arquitectura)

---

## 🛠 Tecnologías

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| React | 19.2 | UI Library |
| TypeScript | ~6.0 | Tipado estático |
| Vite | 5.4 | Build tool & dev server |
| React Router DOM | 7.1 | Routing |
| Axios | 1.15 | HTTP client (para API) |

## 📦 Requisitos Previos

- **Node.js** >= 18.x
- **npm** >= 9.x (o yarn / pnpm)

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone <repository-url>
cd medicalSoftware/frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev
```

La aplicación estará disponible en `http://localhost:5173`.

## 📜 Comandos Disponibles

| Comando | Descripción |
|---------|-------------|
| `npm run dev` | Inicia el servidor de desarrollo con hot reload |
| `npm run build` | Compila TypeScript y genera la versión de producción (output en `dist/`) |
| `npm run preview` | Sirve la build de producción localmente para pruebas |
| `npm run lint` | Ejecuta ESLint para detectar problemas de código |

---

## 📁 Estructura del Proyecto

```
frontend/
├── src/
│   ├── components/          # Componentes reutilizables
│   │   └── ui/
│   │       ├── AnimatedCard.tsx
│   │       ├── Badge.tsx
│   │       ├── Modal.tsx
│   │       └── ProgressBar.tsx
│   ├── layouts/             # Layouts de la aplicación
│   │   └── MainLayout.tsx
│   ├── pages/               # Páginas / vistas principales
│   │   ├── Dashboard.tsx
│   │   ├── Citas.tsx
│   │   ├── Pacientes.tsx
│   │   ├── Farmacia.tsx
│   │   └── Emergencias.tsx
│   ├── App.tsx              # Configuración de rutas
│   ├── main.tsx             # Punto de entrada
│   ├── index.css            # Estilos globales + diseño system
│   └── vite-env.d.ts        # Declaraciones de módulos Vite
├── public/                  # Archivos estáticos
├── package.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

---

## 🗺 Rutas de la Aplicación

| Ruta | Página | Descripción |
|------|--------|-------------|
| `/login` | Login | Pantalla de autenticación |
| `/` o `/dashboard` | Dashboard | Panel principal con métricas y resumen |
| `/citas` | Citas | Gestión de citas médicas (calendario) |
| `/pacientes` | Pacientes | Directorio y ficha de pacientes |
| `/farmacia` | Farmacia | Inventario de medicamentos |
| `/emergencias` | Emergencias | Panel de alertas y emergencias activas |

---

## 📄 Páginas

### Dashboard (`/`)

Panel principal que muestra un resumen general del centro médico.

**Componentes incluidos:**
- **4 tarjetas de estadísticas**: Pacientes totales, citas del día, ingresos mensuales, emergencias activas
- **Gráfico de barras**: Pacientes atendidos por día de la semana (Lunes a Domingo)
- **Gráfico circular**: Distribución de pacientes por especialidad médica (Medicina General, Pediatría, Cardiología, Ginecología, Traumatología)
- **Feed de actividad**: Timeline con las últimas acciones (nuevas citas, pacientes registrados, medicamentos actualizados)
- **Emergencias activas**: Lista de emergencias con prioridad (Crítico, Moderado, Leve)

### Citas (`/citas`)

Sistema de gestión y programación de citas médicas.

**Funcionalidades:**
- Vista tipo calendario con lista de citas
- Filtros por estado (Programada, Completada, Cancelada)
- Formulario modal para agendar nuevas citas
- Campos: paciente, doctor, especialidad, fecha/hora, motivo, estado

### Pacientes (`/pacientes`)

Directorio completo de pacientes registrados.

**Funcionalidades:**
- Tabla con búsqueda en tiempo real (nombre, cédula)
- Paginación (10 pacientes por página)
- Tarjetas con foto, datos personales y historial médico resumido
- Modal para agregar nuevos pacientes (nombre, cédula, edad, género, teléfono, email, grupo sanguíneo, alergias)

### Farmacia (`/farmacia`)

Control de inventario de medicamentos.

**Funcionalidades:**
- Tabla con búsqueda por nombre o categoría
- Paginación (8 items por página)
- Barras de progreso para nivel de stock
- Badges de estado (Disponible, Bajo, Agotado)
- Modal para agregar medicamentos (nombre, categoría, precio, stock mínimo, stock actual)

### Emergencias (`/emergencias`)

Panel de monitoreo y gestión de emergencias médicas.

**Funcionalidades:**
- Tarjetas de estadísticas (activas, críticas, resueltas)
- Alertas con prioridad visual (rojo = crítico, amarillo = moderado, verde = leve)
- Indicador de tiempo transcurrido (⏱)
- Filtros por estado (Activas, Resueltas)

---

## 🧩 Componentes Reutilizables

### `AnimatedCard` (`components/ui/AnimatedCard.tsx`)
Tarjeta con animación de entrada (fade-in + slide-up) y efecto hover.

**Props:**
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | ReactNode | - | Contenido de la tarjeta |
| `delay` | number | 0 | Retraso en segundos para la animación |
| `color` | string | - | Color del borde superior decorativo |

### `Badge` (`components/ui/Badge.tsx`)
Etiqueta de estado con colores semánticos.

**Props:**
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `text` | string | - | Texto a mostrar |
| `variant` | `'success' \| 'warning' \| 'danger' \| 'info' \| 'purple'` | - | Variante de color |

### `ProgressBar` (`components/ui/ProgressBar.tsx`)
Barra de progreso con animación de llenado.

**Props:**
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | number | 0 | Valor actual (0-100) |
| `max` | number | 100 | Valor máximo |
| `color` | string | - | Color de la barra |

### `Modal` (`components/ui/Modal.tsx`)
Modal con overlay y animación de entrada.

**Props:**
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `isOpen` | boolean | - | Si el modal está visible |
| `onClose` | () => void | - | Callback al cerrar |
| `title` | string | - | Título del modal |
| `children` | ReactNode | - | Contenido del modal |

---

## 🎨 Diseño y Estilo

### Paleta de Colores

| Variable | Color | Uso |
|----------|-------|-----|
| `--primary` | `#6366f1` (indigo) | Botones, links activos, header |
| `--primary-dark` | `#4f46e5` | Hover de botones primarios |
| `--success` | `#10b981` (green) | Estados positivos, badges success |
| `--warning` | `#f59e0b` (amber) | Alertas moderadas, badges warning |
| `--danger` | `#ef4444` (red) | Alertas críticas, badges danger |
| `--info` | `#3b82f6` (blue) | Info general, badges info |
| `--purple` | `#8b5cf6` (violet) | Elementos decorativos, badges purple |
| `--dark` | `#1e293b` (slate) | Sidebar, textos principales |
| `--gray-50` | `#f8fafc` | Fondos claros |
| `--gray-100` | `#f1f5f9` | Cards, secciones |
| `--gray-400` | `#94a3b8` | Textos secundarios |
| `--gray-600` | `#475569` | Labels, subtítulos |
| `--white` | `#ffffff` | Fondos de cards, modales |

### Tipografía

- **Fuente principal**: `Inter`, sans-serif (Google Fonts)
- **Títulos principales**: 24px, font-weight 700 (bold)
- **Subtítulos**: 18px, font-weight 600 (semibold)
- **Labels**: 12px, font-weight 500 (medium), uppercase, letter-spacing 0.05em
- **Body**: 14px, font-weight 400 (regular)

### Efectos Visuales

- **Glassmorphism**: Fondos semitransparentes con `backdrop-filter: blur(10px)`
- **Gradientes**: Header con gradiente `#6366f1 → #8b5cf6`
- **Sombras**: `box-shadow: 0 2px 8px rgba(0,0,0,0.06)` en cards
- **Bordes redondeados**: `border-radius: 12px` (cards), `8px` (inputs)
- **Bordes decorativos**: Barra superior de 4px con color semántico en stat cards

---

## ✨ Animaciones

### Definidas en `index.css`

| Animación | Duración | Descripción |
|-----------|----------|-------------|
| `fadeInUp` | 0.5s ease-out | Fade-in + slide-up (cards, sections) |
| `fadeIn` | 0.3s ease-out | Fade-in simple (badges, modals) |
| `pulse` | 2s infinite | Pulso continuo (emergencias críticas) |
| `slideIn` | 0.3s ease-out | Slide-in desde la derecha (modals) |
| `barGrow` | 1s ease-out | Crecimiento de barras (gráfico) |
| `counter` | 1.5s ease-out | Contador numérico (stat cards) |
| `float` | 3s ease-in-out | Flotación suave (logo) |
| `shimmer` | 2s infinite | Efecto shimmer (loading states) |

### Animaciones por Página

**Dashboard:**
- Estadísticas: fade-in escalonado (0.1s, 0.2s, 0.3s, 0.4s delay)
- Gráfico de barras: crecimiento progresivo (0.2s a 1.0s)
- Gráfico circular: fade-in escalonado (0.3s, 0.5s)
- Feed de actividad: fade-in escalonado (0.2s a 1.0s)
- Emergencias activas: fade-in escalonado (0.2s, 0.4s)
- Emergencias críticas: efecto pulse continuo

**Login:**
- Contenedor principal: fade-in + slide-up (0.5s)
- Logo: efecto float (3s infinite)
- Inputs: focus con glow effect (box-shadow transition)
- Botón: hover con scale(1.02), background gradient shift, shadow increase

**Citas / Pacientes / Farmacia:**
- Tablas: fade-in escalonado (0.1s a 0.4s)
- Badges: fade-in (0.3s delay)
- Modales: slide-in desde la derecha (0.3s)

**Emergencias:**
- Alertas: fade-in escalonado (0.1s a 0.5s)
- Emergencias críticas: efecto pulse (2s infinite)

---

## 🏗 Arquitectura

### Enrutamiento
- **React Router DOM v7** con `BrowserRouter` para routing client-side
- Layout wrapper con `<Outlet />` para renderizar páginas dentro del sidebar

### Componentes
- **UI Components** (`components/ui/`): Componentes genéricos reutilizables
- **Pages** (`pages/`): Vistas completas con lógica de negocio propia
- **Layouts** (`layouts/`): Estructura compartida (MainLayout con sidebar)

### Estilos
- **CSS Variables** para diseño system consistente (colores, spacing, fonts)
- **Responsive**: Grid layouts con `auto-fit` y `minmax()` para adaptación automática
- **Mobile-first**: Sidebar colapsa en pantallas pequeñas (< 768px)

### Estado
- Datos mock almacenados en state local con `useState` y `useEffect` para fetch simulado
- Búsqueda y filtrado realizados con `useMemo` para optimización

### Tipado
- TypeScript estricto con interfaces para todas las props y datos
- Type aliases para estados (BadgeVariant, EmergencyStatus, etc.)

---

## 📝 Notas de Desarrollo

- Los datos son **mock** (simulados). Para conectar a backend real, reemplazar los `useState` con datos de API usando `axios`.
- El diseño es **responsive** y se adapta a pantallas pequeñas (sidebar colapsa).
- Las animaciones están definidas en `index.css` y se aplican vía clases CSS.
- Para agregar nuevas páginas, crear el componente en `pages/` y añadir la ruta en `App.tsx`.
