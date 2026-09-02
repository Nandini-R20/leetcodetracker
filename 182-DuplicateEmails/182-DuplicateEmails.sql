-- Last updated: 9/2/2026, 12:41:05 PM
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;