# E-Commerce Web Platform

## 📌 Descripción  
Este proyecto es una **plataforma web de comercio electrónico** diseñada para facilitar la creación y publicación de listados de productos por parte de vendedores.  
En su **versión inicial (MVP)**, la plataforma permitirá:  
- Registrar y autenticar usuarios.  
- Crear listados de productos con título, descripción, imágenes y precio.  
- Navegar y buscar productos publicados por otros usuarios.  
- Administrar los listados propios (editar, eliminar).  

En futuras versiones, se integrarán funcionalidades avanzadas como generación automática de descripciones mediante IA.  

---

## 🚀 Estado del proyecto  
Actualmente en **fase inicial de desarrollo**, centrada en:  
- Definición de requisitos funcionales.  
- Estructura básica de la base de datos.  
- Creación del prototipo de interfaz.  

---

## 🛠️ Tecnologías previstas  
- **Frontend:** React.js o Next.js  
- **Backend:** Node.js con Express  
- **Base de datos:** MongoDB o PostgreSQL  
- **Control de versiones:** Git + GitHub  

---

## 📅 Objetivo a corto plazo  
Desarrollar un **MVP funcional** que permita a los usuarios:  
1. Registrarse e iniciar sesión.  
2. Publicar productos con imágenes.  
3. Buscar y visualizar productos disponibles.

---

## 🚀 Guía para ejecutar el proyecto tras clonar el repositorio

1. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

2. **Aplica las migraciones**
   ```bash
   python manage.py migrate
   ```
   > Esto creará la base de datos (`db.sqlite3`) y las categorías por defecto.

3. **(Opcional) Crea o actualiza las categorías por defecto**
   ```bash
   python manage.py setup_categories
   ```
   > Usa `--force` para actualizar las categorías si ya existen.

4. **Inicia el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

5. **Accede a la plataforma**
   - Abre tu navegador y visita: [http://localhost:8000](http://localhost:8000)

---

**Notas importantes:**
- Los archivos de base de datos (`db.sqlite3`), archivos subidos (`media/`) y archivos estáticos recolectados (`staticfiles/`) no están en el repositorio y se generarán automáticamente.
- No necesitas ejecutar ningún script adicional para datos iniciales; el comando `setup_categories` y las migraciones cubren todo lo necesario.
- Si necesitas usuarios de ejemplo, créalos desde el panel de administración de Django o usando el comando `createsuperuser`.
