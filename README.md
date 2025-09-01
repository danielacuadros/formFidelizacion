# Prueba Técnica GCO – Sistema de Registro y Búsqueda de Clientes

Este proyecto fue desarrollado como parte de una prueba técnica y consiste en una solución integral para la gestión de clientes en un programa de fidelización. Está compuesto por un frontend web, un backend en Java con Spring Boot, una base de datos en MySQL y un motor de búsqueda avanzado en Python con generación de reportes y visualización de datos.

## Tecnologías utilizadas

- **XAMPP / MySQL**: Sistema de gestión de base de datos.
- **IntelliJ IDEA**: Desarrollo del backend en Java usando Spring Boot.
- **Visual Studio Code**: Desarrollo del frontend web con HTML, CSS y JavaScript.
- **PyCharm**: Desarrollo del motor de búsqueda en Python con integración a MySQL, generación de reportes en Excel y gráficos con librerías como `pandas` y `matplotlib`.

---

## Descripción de los módulos

### 1. Frontend

Formulario de inscripción diseñado para que los clientes de la compañía puedan registrarse en el programa de fidelización de alguna de las marcas que conforman el grupo.

#### Datos solicitados:

- Tipo de identificación (lista desplegable)
- Número de identificación
- Nombres
- Apellidos
- Fecha de nacimiento
- Dirección
- Ciudad (lista desplegable)
- Departamento (lista desplegable)
- País (lista desplegable)
- Marca (lista desplegable): Americanino, American Eagle, Chevignon, Esprit, Naf Naf o Rifle

#### Funcionalidades:

- Validaciones en tiempo real con JavaScript (números, campos obligatorios, fechas válidas).
- Listas desplegables dinámicas cargadas desde el backend.
- Diseño responsivo y limpio, orientado a una experiencia de usuario profesional.

---

### 2. Backend (Java - Spring Boot)

Arquitectura de 4 capas:

- **Modelo**: Representación de la entidad `Cliente`.
- **Repositorio**: Acceso a datos usando Spring Data JPA.
- **Servicio**: Lógica de negocio para manejo de clientes.
- **Controlador**: Exposición de endpoints REST para operaciones CRUD.

#### Funcionalidades:

- Recepción de datos del formulario de registro.
- Validación y persistencia de la información en la base de datos MySQL.
- Separación clara de responsabilidades en capas para escalabilidad y mantenimiento.

---

### 3. Motor de búsqueda (Python)

Aplicación desarrollada con Python y MySQL para realizar búsquedas avanzadas sobre la base de datos de clientes.

#### Funcionalidades:

- Búsqueda por múltiples campos: nombre, apellido, ciudad, marca, entre otros.
- Integración con `pandas` para manipulación de datos.
- Exportación de resultados a archivos Excel.
- Generación de gráficos para análisis visual con `matplotlib`.

---

### 4. Base de datos

- Motor: MySQL (a través de XAMPP)
- Base de datos "gco_clientes" normalizada para la gestión eficiente de clientes. (tablas: cliente, marcas, ciudades)
- Script `.sql` disponible para importar la estructura y datos de prueba.

---

## Estructura del repositorio

formFidelizacion/
│
├── gcoBack// Proyecto backend → Java (IntelliJ)
├── gcoForm// Frontend → Formulario web (Visual Studio Code)
├── gcoPython// motor de busqueda → Proyecto Python (PyCharm)
├── README.md → Documentación del proyecto
└── .gitignore → Exclusión de archivos innecesarios

---

## Autor

Daniela Cuadros  
daniicuadros@gmail.com
