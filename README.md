Django Project Template
---

Usage
---
* Create a NEW repo using this as a template
* Update docker-compose.yml as needed
  * add or remove services (psql, redis, etc)
* Add a new django app (don't add unnecessary functionality to "Base" Directory)
  * ```bash
    django-admin startapp <app_name>
    ```
  * the above command can be run inside the "backend" docker compose container
* Migrations
  * ```bash
    python manage.py makemigrations
    ``` 
  * ```bash
    python manage.py migrate
    ```
    
Notes
----
While it may seem the Base folder is an anti-pattern to Django enthusiasts, it provides a simple way for new adopters to 
quickly spin up a project in just a few minutes, and allow them to start writing business logic instead of needing to
learn the nuances of the `django-admin` CLI.
