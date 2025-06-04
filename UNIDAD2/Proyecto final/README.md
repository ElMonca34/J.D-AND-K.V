# 📚 Sistema de Gestión de Libros

Este es un proyecto en Python para la gestión de libros, autores y editoriales. Está organizado con una arquitectura modular dividida en **backend** y **frontend**, y utiliza SQLite como motor de base de datos.

## 🧾 Descripción General

El sistema permite:

- Registrar, modificar y eliminar autores.
- Registrar editoriales y asociarlas a libros.
- Gestionar libros, incluyendo relaciones con autores y editoriales.
- Mostrar información desde un frontend modular.

## 📁 Estructura del Proyecto

```
Proyecto final/
├── backend/
│   ├── autor/
│   ├── editorial/
│   ├── libro/
│   ├── db.sqlite3
│   └── manage.py
├── frontend/
│   ├── controladores/
│   ├── modelos/
│   ├── vistas/
│   └── main.py
├── README.md
├── requirements.txt
├── respaldo_autores.txt
└── respaldo_libros.txt
```

## ⚙️ Requisitos

Requiere Python 3.7 o superior.

Instala los paquetes necesarios con:

```bash
pip install -r requirements.txt
```

## 🚀 Ejecución

### 1. Ejecutar el Backend

Desde la raíz del proyecto:

```bash
cd backend
```

Si es la primera vez que ejecutas el proyecto o has realizado cambios en los modelos, ejecuta:

```bash
python manage.py makemigrations
python manage.py migrate
```

Luego, para iniciar el servidor:

```bash
python manage.py runserver
```

### 2. Ejecutar el Frontend

```bash
cd frontend
python main.py
```

## 💾 Base de Datos

- Se utiliza `SQLite` y se incluye el archivo `db.sqlite3`.
- Para restaurar datos puedes usar los archivos:
  - `respaldo_autores.txt`
  - `respaldo_libros.txt`

## 🧩 Módulos

- **Autor**: Control de información de autores.
- **Editorial**: Gestión de editoriales.
- **Libro**: Registro de libros y sus relaciones.
- **Frontend**: Presentación de la información (posiblemente consola o interfaz gráfica básica).

## 📌 Notas Adicionales

- Estructura limpia y separada por capas (modelo, vista, controlador).
- Se recomienda hacer respaldos periódicos de `db.sqlite3`.

