update broth_cook_times_active
set product = :product
,product_weight = :prodWeight
,total_weight = :totalWeight
,water_weight = :totalWeight - :prodWeight
where cooker = :cooker