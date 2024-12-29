SELECT c.CAR_ID,
       c.CAR_TYPE, 
       FLOOR(c.DAILY_FEE * 30 * (1 - d.DISCOUNT_RATE/100)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR c
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
ON c.CAR_TYPE = d.CAR_TYPE
WHERE d.CAR_TYPE in ('세단', 'SUV') 
  AND d.DURATION_TYPE = '30일 이상'
  AND c.CAR_ID NOT in (SELECT CAR_ID
                   FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                   WHERE START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01')
  AND FLOOR(c.DAILY_FEE * 30 * (1 - d.DISCOUNT_RATE/100)) BETWEEN 500000 AND 1999999
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC