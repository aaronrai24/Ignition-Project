update broth_cook_times 
set product = :product
,product_weight = :prodWeight
,total_weight = :totalWeight
,water_weight = :totalWeight - :prodWeight
where index_id = :index