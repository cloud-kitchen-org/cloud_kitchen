# Using Alembic for Database Migrations

## Introduction
Alembic is a lightweight database migration tool for SQLAlchemy. This guide explains how to use Alembic to manage database migrations.

## Installation
1. Ensure you have Alembic installed in your project. Use pip to install it:

   ```bash
   pip install alembic
   ```
2. Verify the installation by checking the Alembic version:

   ```bash
   alembic --version
   ```

## Setting Up Alembic
1. Initialize Alembic in your project:

   ```bash
   alembic init alembic
   ```
   This will create an `alembic` directory and a base `alembic.ini` configuration file.

2. Configure the `alembic.ini` file:

   - Locate the `sqlalchemy.url` parameter.

   - Set it to your database URL (use an environment variable for security):

     ```ini
     sqlalchemy.url = <YOUR_DATABASE_URL>
     ```

   If using environment variables, modify your `env.py` file in the `alembic` directory to load the URL dynamically:

   ```python
   from sqlalchemy import engine_from_config
   from sqlalchemy import pool
   from alembic import context
   import os

   config = context.config
   config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

   target_metadata = None

   def run_migrations_offline():
       ...

   def run_migrations_online():
       ...
   ```

3. Set up `target_metadata` in `env.py`:

   ```python
   from app.db.base import Base  # Update with your SQLAlchemy Base
   from app.models import User, UserPhotos # Import all your tables

   target_metadata = Base.metadata
   ```

## Managing Migrations

### Creating a Migration Script
To create a new migration script after modifying your database models:

   1. Run the following command:

      ```bash
      alembic revision --autogenerate -m "describe your migration"
      ```
   2. Review the generated script in the `alembic/versions` directory to ensure correctness.

### Applying Migrations
To apply migrations to your database:

   ```bash
   alembic upgrade head
   ```
   This applies all migrations up to the latest one.

### Reverting to a Previous Migration
To revert to a specific migration:

   ```bash
   alembic downgrade <revision_id>
   ```
   To revert one migration step back:

   ```bash
   alembic downgrade -1
   ```

### Running All Migrations at Once
To ensure all migrations are applied from the start:

   ```bash
   alembic upgrade head
   ```

### Checking Migration History
To view migration history:

   ```bash
   alembic history
   ```

## Common Commands Cheat Sheet
- **Initialize Alembic**: `alembic init alembic`
- **Generate a Migration**: `alembic revision --autogenerate -m "message"`
- **Apply All Migrations**: `alembic upgrade head`
- **Revert to Specific Migration**: `alembic downgrade <revision_id>`
- **Revert One Step Back**: `alembic downgrade -1`
- **View Migration History**: `alembic history`
- **Show Current Revision**: `alembic current`