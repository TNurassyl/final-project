select
    country,
    count(distinct mfr_id) as manufacturers_cnt
from "airflow"."staging"."stg_manufacturers"
group by country