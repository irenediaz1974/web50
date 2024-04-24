***
## Tarea a realizar:

- Luego de creado subdirectorio commerce
-  cd into the commerce
- Ejecutar para correr migrations en auctions app:

```python
python manage.py makemigrations auctions
```
 ###### System check identified some issues:

    WARNINGS:
    ←[33;1mauctions.User: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
            HINT: Configure the DEFAULT_AUTO_FIELD setting or the AuctionsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.←[0m
    ←[36;1mMigrations for 'auctions':←[0m
    ←[1mauctions\migrations\0001_initial.py←[0m
        - Create model User
 
- Ejecutar  para aplicar migraciones a la Base de datos:
```python
python manage.py migrate
```
    System check identified some issues:

    WARNINGS:
    ←[33;1mauctions.User: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
            HINT: Configure the DEFAULT_AUTO_FIELD setting or the AuctionsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.←[0m
    ←[36;1mOperations to perform:←[0m
    ←[1m  Apply all migrations: ←[0madmin, auctions, auth, contenttypes, sessions
    ←[36;1mRunning migrations:←[0m
    Applying contenttypes.0001_initial...←[32;1m OK←[0m
   
   