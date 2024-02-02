-- 코드를 입력하세요
SELECT round(avg(DAILY_FEE),0) AVERAGE_FEE
from car_rental_company_car
where car_type='SUV'