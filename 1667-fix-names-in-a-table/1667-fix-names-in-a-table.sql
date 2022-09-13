SELECT user_id, CONCAT(UPPER(LEFT(Name,1)) , LOWER(SUBSTRING(name,2))) AS Name
FROM Users
ORDER BY user_id