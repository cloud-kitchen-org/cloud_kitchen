# Phase 1 Database Design: Food Ordering Platform

This document provides the full schema design for the backend database supporting Phase 1 of the food ordering platform. The focus is on data normalization, scalability, and clarity.

---

## 📌 Core Principles

* Use **PostgreSQL** for relational integrity and support for future geo-spatial indexing (PostGIS)
* Follow **3rd normal form** where applicable
* Maintain audit fields: `created_at`, `updated_at`, and `deleted_at` (soft deletes)
* Use **UUIDs** as primary keys for scalability and security

---

## 🔐 USERS TABLE

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) UNIQUE,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('user', 'partner', 'admin')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🧍 USER ADDRESSES

```sql
CREATE TABLE user_addresses (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    label VARCHAR(50),
    address_line1 TEXT,
    address_line2 TEXT,
    area VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    pincode VARCHAR(10),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🧑‍🍳 RESTAURANTS

```sql
CREATE TABLE restaurants (
    id UUID PRIMARY KEY,
    partner_id UUID REFERENCES users(id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    image_url TEXT,
    cuisine_tags TEXT[],
    address_line1 TEXT,
    address_line2 TEXT,
    area VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    pincode VARCHAR(10),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    opening_hours JSONB,
    approval_status VARCHAR(20) DEFAULT 'pending' CHECK (approval_status IN ('pending', 'approved', 'rejected')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📂 MENU CATEGORIES

```sql
CREATE TABLE categories (
    id UUID PRIMARY KEY,
    restaurant_id UUID REFERENCES restaurants(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    sort_order INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🍽️ MENU ITEMS

```sql
CREATE TABLE items (
    id UUID PRIMARY KEY,
    category_id UUID REFERENCES categories(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    image_url TEXT,
    tax_percentage DECIMAL(5,2) DEFAULT 0.00,
    tags TEXT[],
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🛍️ CART

```sql
CREATE TABLE cart_items (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    restaurant_id UUID REFERENCES restaurants(id),
    item_id UUID REFERENCES items(id),
    quantity INTEGER DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🧾 ORDERS

```sql
CREATE TABLE orders (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    restaurant_id UUID REFERENCES restaurants(id),
    address_id UUID REFERENCES user_addresses(id),
    status VARCHAR(20) DEFAULT 'PLACED' CHECK (status IN ('PLACED', 'CONFIRMED', 'COMPLETED', 'CANCELLED')),
    total_amount DECIMAL(10,2) NOT NULL,
    payment_status VARCHAR(20) DEFAULT 'PENDING' CHECK (payment_status IN ('PENDING', 'PAID', 'FAILED')),
    delivery_type VARCHAR(20) DEFAULT 'delivery' CHECK (delivery_type IN ('pickup', 'delivery')),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📦 ORDER ITEMS

```sql
CREATE TABLE order_items (
    id UUID PRIMARY KEY,
    order_id UUID REFERENCES orders(id) ON DELETE CASCADE,
    item_id UUID REFERENCES items(id),
    quantity INTEGER NOT NULL,
    price_at_order_time DECIMAL(10,2),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

---

## 💳 PAYMENTS

```sql
CREATE TABLE payments (
    id UUID PRIMARY KEY,
    order_id UUID REFERENCES orders(id),
    provider VARCHAR(50),
    transaction_id VARCHAR(100),
    amount DECIMAL(10,2),
    currency VARCHAR(10) DEFAULT 'INR',
    status VARCHAR(20) CHECK (status IN ('PENDING', 'SUCCESS', 'FAILED')),
    paid_at TIMESTAMPTZ,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📌 Indexing & Optimization Notes

* Add GIN/BTREE indexes on frequently queried columns:

  * `restaurants.city`, `user_addresses.city`, `orders.user_id`
* Consider full-text search on item names and restaurant names later
* Use `ON DELETE CASCADE` for child relations (e.g., cart items, order items)

---

## 🧪 Seed & Migrations

* Use Alembic (FastAPI) or Django Migrations for schema changes
* Seed test users, restaurants, menu items for dev/staging

---

This schema will support all features from Phase 1 with scalability for future extensions like reviews, delivery tracking, or real-time dashboards.
