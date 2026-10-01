SELECT c.name AS customers FROM 
customers c LEFT JOIN orders o
ON c.id = o.customerID
WHERE o.id is NULL;