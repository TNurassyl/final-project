select
    mfr_id,
    upper(trim(mfr_name)) as mfr_name,
    upper(country) as country,
    ingested_at
from "airflow"."raw"."manufacturers"