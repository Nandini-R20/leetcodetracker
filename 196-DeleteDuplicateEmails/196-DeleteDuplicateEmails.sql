-- Last updated: 9/2/2026, 12:40:52 PM
DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;