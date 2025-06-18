# Databricks notebook source
# MAGIC %md
# MAGIC # Accessing Azure Data Lake with Access Keys
# MAGIC 1. Set spark config to fs.azure.account.key
# MAGIC 2. List files from the demo container
# MAGIC 3. Read data from circuits.csv files

# COMMAND ----------

f1datalakes_account_key = dbutils.secrets.get(scope='f1-scope', key='f1datalakes-account-key')

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.f1datalakes.dfs.core.windows.net",
    f1datalakes_account_key
)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@f1datalakes.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@f1datalakes.dfs.core.windows.net/circuits.csv"))