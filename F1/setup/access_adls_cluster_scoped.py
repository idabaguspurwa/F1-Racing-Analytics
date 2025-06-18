# Databricks notebook source
# MAGIC %md
# MAGIC # Accessing Azure Data Lake with Cluster Scoped Credentials
# MAGIC 1. Set spark config to fs.azure.account.key in the cluster
# MAGIC 2. List files from the demo container
# MAGIC 3. Read data from circuits.csv files

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@f1datalakes.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@f1datalakes.dfs.core.windows.net/circuits.csv"))