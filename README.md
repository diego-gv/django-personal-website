<!-- markdownlint-disable MD033 -->
<h1 align="center">Personal portfolio</h1>

<div align="center">
  :snake:
</div>
<div align="center">
  <strong>Project to learn Django framework and fullstack development</strong>
</div>
<br />

<div align="center">
  <!-- Made with Python -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"
      alt="made-with-python" />
  </a>
  <!-- Python version -->
  <a href="https://www.python.org/downloads/release/python-3810/">
    <img src="https://img.shields.io/badge/python-3.8.10-blue.svg"
      alt="Python 3.8.10" />
  </a>
  <!-- Test Coverage --> <!--TODO-->
  <a href="https://codecov.io/github/diego-gv/django-personal-portfolio">
    <img src="https://img.shields.io/codecov/c/github/diego-gv/django-personal-portfolio/master.svg"
      alt="Test Coverage" />
  </a>
</div>

<hr>

## Descripción

Este proyecto representa un ejemplo para aprender y practicar el framework [Django](https://www.djangoproject.com/) y comenzó como un ejemplo basado en un tutorial de [RealPython](https://realpython.com/) (ver material empleado).

Se tiene como objetivo implementar y testear nuevas funcionalidades para continuar aprendiendo este increíble framework (y paquetes estrechamente relacionados), perfeccionar el manejo del propio lenguaje [Python](https://www.python.org/downloads/) y aprender sobre el desarrollo FullStack.

## Material empleado

- Frameworks y herramientas
  - [Bootstrap](https://getbootstrap.com/)
- Documentación y tutoriales
  - [Get Started With Django Part 1: Build a Portfolio App](https://realpython.com/get-started-with-django-1/) (_done_)
  - [Get Started With Django Part 2: Django User Management](https://realpython.com/django-user-management/) (_[TODO](https://realpython.com/django-user-management/#change-email-templates)_)
  - [Aprende la librería para CSS de Bootstrap desde cero](https://codingpotions.com/bootstrap)
  - [How to generate lots of dummy data for your Django app](https://mattsegal.dev/django-factoryboy-dummy-data.html)

## Principales dependencias

```text
Django==4.0.2
factory-boy==3.2.1
django REST Framework  _(pendiente...)_ https://www.django-rest-framework.org/
```

Además se han utilizado los siguientes frameworks o paquetes:

- [Bootstrap 4.1.3](https://getbootstrap.com/)

## Entorno de desarrollo

Para poder trabajar de forma comoda se han preparado una serie de comandos para generar datos de prueba. Estos comandos son:

```sh
# comandos individuales
python3 manage.py setup_dummy_projects
python3 manage.py setup_dummy_posts
python3 manage.py setup_dummy_users

# bash script conjunto
bash setup_dummy_data.sh
```

El servidor podemos lanzarlo a través de dos posibles comandos:

```sh
# gunicorn
gunicorn portfolio.wsgi --workers 1 --timeout 0 -b 0.0.0.0:8888 --reload # http://localhost:8888/
# django
python manage.py runserver # http://127.0.0.1:8000/
```

Para arrancar el servidor de correo para pruebas se puede hacer lanzando el siguiente comando en la consola:

```sh
python -m smtpd -n -c DebuggingServer localhost:1025
```

### Errores

Es posible que los ficheros `static`, como los `CSS styles` no se muestren de forma correcta. Para solucionarlo solo hay que ejecutar el siguiente comando (Fuente [stackoverflow](https://stackoverflow.com/questions/4420378/why-does-my-django-admin-site-not-have-styles-css-loading/10047615#10047615)):

```sh
python manage.py collectstatic
```
