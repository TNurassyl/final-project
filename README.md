# VPIC Data Pipeline (Airflow + PostgreSQL + dbt)

End-to-end data pipeline built with Airflow, PostgreSQL, and dbt.
The pipeline loads data from a public REST API and transforms it into an analytics-ready data mart.

---

## Data Source

**NHTSA Vehicle Product Information Catalog (VPIC)**
[https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json](https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json)

Entities:

* Manufacturers
* Vehicle Types

Relationship:

* vehicle_types.mfr_id → manufacturers.mfr_id

---

## Architecture

Database schemas:

* raw — raw data loaded from API
* staging — cleaned and standardized data (dbt views)
* mart — analytics-ready data (dbt tables)

Main components:

* PostgreSQL — data warehouse
* Airflow — orchestration
* dbt — transformations and tests

---

## Airflow DAGs

### 1. ingestion_vpic_api

* Runs daily
* Loads data from VPIC REST API
* Writes data into:

  * raw.manufacturers
  * raw.vehicle_types
* Uses idempotent loading (raw tables are truncated before insert)

### 2. dbt_transformation

* Runs daily
* Executes:

  * dbt run
  * dbt test

---

## dbt Models

### Staging

* staging.stg_manufacturers (view)
* staging.stg_vehicle_types (view)

### Mart

* mart.manufacturers_by_country (table)

---

## dbt Tests

Implemented tests:

* not_null
* unique
* relationships

All tests pass successfully.

---

## How to Run

### 1. Start services

```bash
docker compose up -d
```

### 2. Create Airflow admin user (one-time)

```bash
docker exec -it airflow_web airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com
```

### 3. Open Airflow UI

```
http://localhost:8080
```

Login:

```
admin / admin
```

### 4. Run pipelines

1. Enable and trigger `ingestion_vpic_api`
2. Enable and trigger `dbt_transformation`

Both DAGs should complete with **green (success)** status.

---

## Result

The project delivers a complete, reproducible data pipeline:

* Automated ingestion from a public API
* Layered data modeling (raw → staging → mart)
* Data quality checks with dbt tests
* Orchestration using Airflow

The pipeline fully satisfies the final project requirements.
