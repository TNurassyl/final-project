
    
    

with child as (
    select mfr_id as from_field
    from "airflow"."staging"."stg_vehicle_types"
    where mfr_id is not null
),

parent as (
    select mfr_id as to_field
    from "airflow"."staging"."stg_manufacturers"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


