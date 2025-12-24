
  
    

  create  table "airflow"."staging"."manufacturers_by_country__dbt_tmp"
  
  
    as
  
  (
    select
    country,
    count(distinct mfr_id) as manufacturers_cnt
from "airflow"."staging"."stg_manufacturers"
group by country
  );
  