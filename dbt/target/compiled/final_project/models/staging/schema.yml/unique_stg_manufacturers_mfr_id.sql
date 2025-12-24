
    
    

select
    mfr_id as unique_field,
    count(*) as n_records

from "airflow"."staging"."stg_manufacturers"
where mfr_id is not null
group by mfr_id
having count(*) > 1


