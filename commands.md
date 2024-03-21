# Console commands to use

**Activate venv:**

```bash
.\venv\Scripts\activate
```

**Django makemigrations, migrate:**

```bash
python manage.py makemigrations
python manage.py migrate
```

**Django superuser:**

```bash
python manage.py createsuperuser
```

**Django runserver:**

```bash
cd .\app\
python.exe .\manage.py runserver
```

**Freeze:**

```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

**Fixtures:**

```bash
python manage.py dumpdata goods.Categories --indent 2 --output fixtures\goods\categories.json
python manage.py dumpdata goods.Product --indent 2 --output fixtures\goods\products.json
```
> Given that json files are created in UTF-8 encoding

```bash
python manage.py loaddata fixtures\goods\categories.json
python manage.py loaddata fixtures\goods\products.json
```

---

**Autopep8:**

```bash
autopep8 --in-place --aggressive --aggressive <filename>
```

**Autoflake:**

```bash
autoflake --in-place --remove-unused-variables <filename>
```

**Ruff:**

```bash
ruff check --fix
ruff format
```

**Black:**

```bash
black .
```

**Isort:**

```bash
isort .
```

**Mypy:**

```bash
mypy <filename>
```
