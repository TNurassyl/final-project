
  create view "airflow"."staging"."stg_vehicle_types__dbt_tmp"
    
    
  as (
    select
    mfr_id,
    vehicle_type,
    ingested_at
from "airflow"."raw"."vehicle_types"
  );