select
    mfr_id,
    vehicle_type,
    ingested_at
from {{ source('raw', 'vehicle_types') }}