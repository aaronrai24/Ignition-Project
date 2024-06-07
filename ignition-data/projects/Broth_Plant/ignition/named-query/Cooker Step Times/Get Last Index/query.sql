select top 1 index_id 
from broth_cook_times
where cooker = :cooker
order by index_id desc