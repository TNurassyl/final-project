
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    mfr_id as unique_field,
    count(*) as n_records

from "airflow"."staging"."stg_manufacturers"
where mfr_id is not null
group by mfr_id
having count(*) > 1



  
  
      
    ) dbt_internal_test