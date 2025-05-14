
# 🌐 Proyecto Web Personal con Django

Este es mi **primer proyecto web personal** realizado con **Python y Django**, se encuentra desplegado en: https://maurolaf.pythonanywhere.com/portfolio/ con el objetivo de integrar y reforzar los conocimientos fundamentales de desarrollo web, entornos virtuales, bases de datos y estructuración de proyectos.

## 🛠 Tecnologías utilizadas

- **Python 3.13**
- **Django 5.2.1**
- **HTML básico**
- **Virtualenv / Pipenv** (gestión de entorno)
- **SQLite3** (por defecto en Django)
- **Visual Studio Code**

## 📦 Instalación y ejecución del entorno

1. Clona el repositorio y entra a la carpeta raíz del proyecto:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. Activa el entorno virtual con pipenv:

```bash
pipenv install
pipenv shell
```

3. Ejecuta el servidor de desarrollo de Django:

```bash
cd webpersonal
python manage.py runserver
```

## 🔑 Conceptos aplicados

### ✅ Entorno virtual

Gestioné el proyecto con **Pipenv**, lo cual permite mantener aisladas las dependencias mediante los archivos `Pipfile` y `Pipfile.lock`.

### ✅ Estructura del proyecto

- `webpersonal/` contiene el proyecto Django.
- `core/` es la aplicación principal, donde definí las vistas, rutas y lógica.
- `templates/` y archivos HTML: se trabajó con HTML simple sin plantillas aún, pero se dejó base para eso.
- `Pipfile`: definí las dependencias como Django, Pillow, pylint, etc.

### ✅ Vistas en Django

Se trabajó con **funciones de vista simples** (`HttpResponse`) y rutas personalizadas, como:

- `/` → Portada
- `/about-me/` → Acerca de
- `/portfolio/` → Portafolio
- `/contact/` → Contacto

Estas rutas fueron registradas en `urls.py`, usando `path()` con nombres amigables para el admin y futuras plantillas.

### ✅ Archivos estáticos y base HTML

Se definió un bloque de código HTML (`html_base`) común en las vistas, que actúa como plantilla base manual para evitar duplicación de código.

### ✅ Migraciones y modelos

Aprendí que en Django es fundamental ejecutar:

```bash
python manage.py makemigrations
python manage.py migrate
```

Esto aplica los cambios en los modelos a la base de datos. Entendí también que no es necesario migrar otras apps si no fueron modificadas.

## 📚 Conocimientos adquiridos

- Diferencia entre `venv` y `pipenv`, y ventajas de usar Pipenv en proyectos colaborativos.
- Cómo organizar archivos y carpetas en un proyecto Django.
- Uso de `verbose_name` y `choices` en modelos para mejorar la legibilidad y funcionalidad en el admin.
- Corrección de errores comunes de rutas (`/portfolio/` vs `/porfolio/`).
- Cómo trabaja `AppConfig` vs `Meta` en los modelos de Django.
- Uso de `manage.py` y cómo funciona internamente con `__name__ == "__main__"`.

## 🎯 Objetivo

Este proyecto tiene como objetivo **aprender Django desde cero**, desarrollar una estructura web simple y prepararme para el desarrollo de aplicaciones más avanzadas. Próximamente planeo integrar:

- Formularios con `forms.Form` o `ModelForm`
- Plantillas con `render()`
- Bases de datos externas como MySQL o PostgreSQL
- Bootstrap o Tailwind para mejorar el diseño

## 💬 Comentarios

Este proyecto fue creado desde la terminal, con una fuerte práctica en Visual Studio Code, utilizando `pipenv`, configurando rutas, resolviendo errores y entendiendo cómo interactúa Django internamente. Me ayudó a desarrollar disciplina, lógica de rutas y modularidad en el backend.

## 📸 Capturas (opcional)

## 🔗 Recursos útiles

- [Documentación de Django](https://docs.djangoproject.com/es/5.2/)
- [Tipos de campo en modelos](https://docs.djangoproject.com/en/5.2/ref/models/fields/)
- [Emmet en VS Code](https://code.visualstudio.com/docs/editor/emmet)

## 🧠 Autor

**Mauro Lafuente**  
Estudiante de desarrollo web y backend
"# Web-Personal" 
