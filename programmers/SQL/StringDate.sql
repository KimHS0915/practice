-- 루시와 엘라 찾기
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;

-- 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%el%' AND ANIMAL_TYPE='Dog'
ORDER BY NAME;

-- 중성화 여부 파악하기
SELECT ANIMAL_ID,
       NAME,
       (CASE WHEN SEX_UPON_INTAKE LIKE 'Neutered%' THEN 'O'
             WHEN SEX_UPON_INTAKE LIKE 'Spayed%' THEN 'O'
             ELSE 'X'
       END) AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
