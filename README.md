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
  <a href="https://www.python.org/downloads/release/python-3916/">
    <img src="https://img.shields.io/badge/python-3.9.16-blue.svg"
      alt="Python 3.9.16" />
  </a>
  <!-- Django version -->
  <a href="https://docs.djangoproject.com/en/4.1/releases/4.0.2/">
    <img src="https://img.shields.io/badge/django-4.0.2-darkgreen.svg"
      alt="Django 4.0.2" />
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
  - [x] [Bootstrap](https://getbootstrap.com/)
  - [ ] [Django](https://www.djangoproject.com/)
  - [ ] [Django REST framework](https://www.django-rest-framework.org/)
  - [ ] [Django CMS](https://docs.django-cms.org/en/latest/index.html)
- Documentación y tutoriales
  - [ ] [Aprende la librería para CSS de Bootstrap desde cero](https://codingpotions.com/bootstrap)
  - [x] [Get Started With Django Part 1: Build a Portfolio App](https://realpython.com/get-started-with-django-1/)
  - [x] [Get Started With Django Part 2: Django User Management](https://realpython.com/django-user-management/)
    - [ ] Send Emails to the Outside World
    - [ ] Log in With GitHub
  - [ ] [Get Started With Django Part 3: Django View Authorization](https://realpython.com/django-user-management/)
  - [x] [How to generate lots of dummy data for your Django app](https://mattsegal.dev/django-factoryboy-dummy-data.html)

## Principales dependencias

```text
Django==4.0.2
factory-boy==3.2.1
django-extensions _(pendiente...)_ https://django-extensions.readthedocs.io/
```

Además se han utilizado los siguientes frameworks o paquetes:

- [Bootstrap 4.1.3](https://getbootstrap.com/)

## Entorno de desarrollo

### Generar datos de _dummy_ de muestra

Para poder trabajar de forma comoda se han preparado una serie de comandos para generar datos de prueba. Estos comandos son:

```sh
# comandos individuales
python3 manage.py setup_dummy_projects
python3 manage.py setup_dummy_posts
python3 manage.py setup_dummy_users

# comando conjunto
python3 manage.py setup_dummy_data
```

### Lanzar el servidor

El servidor podemos lanzarlo a través de dos posibles comandos:

```sh
# gunicorn
gunicorn portfolio.wsgi --workers 1 --timeout 0 -b 0.0.0.0:8888 --reload # http://localhost:8888/
# django
python manage.py runserver # http://127.0.0.1:8000/
```

### Servidor de correo

Para arrancar el servidor de correo para pruebas se puede hacer lanzando el siguiente comando en la consola:

```sh
python -m smtpd -n -c DebuggingServer localhost:1025
```

También se puede configurar un servidor real para realizar pruebas más realistas. ALgunos servidores gratuitos de prueba son:

- [Mail](https://www.mailgun.com/)
- [Sendinblue](https://es.sendinblue.com/)

### Errores

Es posible que los ficheros `static`, como los `CSS styles` no se muestren de forma correcta. Para solucionarlo solo hay que ejecutar el siguiente comando (Fuente [stackoverflow](https://stackoverflow.com/questions/4420378/why-does-my-django-admin-site-not-have-styles-css-loading/10047615#10047615)):

```sh
python manage.py collectstatic
```
