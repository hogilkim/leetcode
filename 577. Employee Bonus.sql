# Write your MySQL query statement below
# Feb 6, 2024 577
SELECT name, bonus
FROM Employee 
LEFT JOIN Bonus
ON Employee.empId = Bonus.empId
WHERE bonus is NULL OR bonus < 1000