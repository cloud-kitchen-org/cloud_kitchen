# CLOUD KITCHEN

## Overview

## Prerequisites
- Python 3.12.9
- Required Python packages (see [Installation](#installation))

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/cloud-kitchen-org/cloud_kitchen.git
   cd cloud_kitchen/
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   Linux: source venv/bin/activate
   Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the `.env` files with the following command:
   ```sh
   cp .env.example .env
   cp .env.template .env.development
   ```
5. Run the server with the following command:
   ```sh
   uvicorn app.main:app --reload
   ```

## Database Setup (Docker container)
- Setup the .env values
- Start the database container
  ```sh
  docker compose up -d
  ```

## Database Migrations
- Navigate to project root directory
  ```sh
  cd cloud_kitchen/
  ```
- Run the following commands in the terminal (with the venv activated)
  ```sh
  alembic upgrade head
  python -m scripts.seed_roles
  ```