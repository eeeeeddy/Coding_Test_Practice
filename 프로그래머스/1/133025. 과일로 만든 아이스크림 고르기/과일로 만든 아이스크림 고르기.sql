-- 코드를 입력하세요
SELECT X.FLAVOR
FROM FIRST_HALF X RIGHT OUTER JOIN ICECREAM_INFO Y
  ON X.FLAVOR = Y.FLAVOR
WHERE X.TOTAL_ORDER > 3000
  AND Y.INGREDIENT_TYPE='fruit_based'
ORDER BY X.TOTAL_ORDER DESC