-- 코드를 입력하세요
SELECT DATE_FORMAT(DATETIME, '%k') AS HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR >= 9 AND HOUR <= 19
ORDER BY CAST(DATE_FORMAT(DATETIME, '%k') AS UNSIGNED);
