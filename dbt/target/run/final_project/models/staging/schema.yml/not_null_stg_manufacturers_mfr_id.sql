
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select mfr_id
from "airflow"."staging"."stg_manufacturers"
where mfr_id is null



  
  
      
    ) dbt_internal_test