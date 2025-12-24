select
    country,
    count(distinct mfr_id) as manufacturers_cnt
from {{ ref('stg_manufacturers') }}
group by country