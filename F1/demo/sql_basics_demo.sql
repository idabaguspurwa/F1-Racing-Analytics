-- Databricks notebook source
SHOW DATABASES;

-- COMMAND ----------

USE f1_processed;

-- COMMAND ----------

SHOW TABLES;

-- COMMAND ----------

SELECT *
FROM drivers
LIMIT 15;

-- COMMAND ----------

DESC drivers;

-- COMMAND ----------

SELECT name, dob AS date_of_birth
FROM drivers
WHERE nationality = 'British' AND dob >= '1990-01-01'
ORDER BY dob DESC;

-- COMMAND ----------

SELECT *
FROM drivers
ORDER BY nationality ASC, dob DESC;

-- COMMAND ----------

SELECT name, nationality, dob
FROM drivers
WHERE (nationality = 'British' AND dob >= '1990-01-01')
OR nationality = 'Austrian'
ORDER BY dob DESC;