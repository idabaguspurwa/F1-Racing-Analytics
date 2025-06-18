-- Databricks notebook source
CREATE DATABASE IF NOT EXISTS f1_processed
LOCATION 'abfss://processed@f1datalakes.dfs.core.windows.net/'

-- COMMAND ----------

DESC DATABASE f1_processed