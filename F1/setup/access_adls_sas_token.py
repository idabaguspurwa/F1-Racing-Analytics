# Databricks notebook source
# MAGIC %md
# MAGIC # Accessing Azure Data Lake with SAS Token
# MAGIC 1. Set spark config for the SAS Token
# MAGIC 2. List files from the demo container
# MAGIC 3. Read data from circuits.csv files

# COMMAND ----------

f1datalakes_demo_sas_token = dbutils.secrets.get(scope='f1-scope', key='f1datalakes-demo-sas-token')

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.f1datalakes.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.f1datalakes.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.f1datalakes.dfs.core.windows.net", f1datalakes_demo_sas_token)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@f1datalakes.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@f1datalakes.dfs.core.windows.net/circuits.csv"))