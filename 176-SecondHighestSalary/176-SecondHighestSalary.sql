-- Last updated: 9/2/2026, 12:41:10 PM
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);