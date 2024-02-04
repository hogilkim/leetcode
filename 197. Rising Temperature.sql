# Write your MySQL query statement below

SELECT w2.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = -1 AND w2.temperature > w1.temperature

SELECT w2.id
FROM Weather w1
INNER JOIN Weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = -1 AND w2.temperature > w1.temperature