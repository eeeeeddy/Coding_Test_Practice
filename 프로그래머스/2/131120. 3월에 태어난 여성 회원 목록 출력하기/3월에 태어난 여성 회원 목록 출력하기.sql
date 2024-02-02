-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, SUBSTR(TO_CHAR(DATE_OF_BIRTH,'YYYY-MM-DD'),1,10) DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE EXTRACT(MONTH FROM DATE_OF_BIRTH) = 3
  AND GENDER = 'W'
  AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC