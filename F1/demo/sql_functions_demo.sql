-- Databricks notebook source
USE f1_processed;

-- COMMAND ----------

SELECT *, CONCAT(driver_ref, '-', code) AS new_driver_ref
FROM drivers

-- COMMAND ----------

SELECT *, SPLIT(name, ' ')[0] forename, SPLIT(name, ' ')[1] surname
FROM drivers

-- COMMAND ----------

SELECT *, current_timestamp
FROM drivers

-- COMMAND ----------

INSERT INTO drivers(data_source)
VALUES ('ErgastAPI');
SELECT *, date_format(dob, 'dd-MM-yyyy')
FROM drivers

-- COMMAND ----------

SELECT MAX(dob)
FROM drivers

-- COMMAND ----------

SELECT COUNT(*)
FROM drivers
WHERE nationality = 'Austrian';

-- COMMAND ----------

SELECT nationality, COUNT(*)
FROM drivers
GROUP BY nationality
ORDER BY nationality;

-- COMMAND ----------

SELECT nationality, COUNT(*)
FROM drivers
GROUP BY nationality
HAVING COUNT(*) > 50
ORDER BY nationality;

-- COMMAND ----------

SELECT nationality, name, dob, RANK() OVER(PARTITION BY nationality ORDER BY dob DESC) AS age_rank
FROM drivers 
ORDER BY nationality, age_rank