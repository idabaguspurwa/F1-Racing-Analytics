# Databricks notebook source
# MAGIC %md
# MAGIC # Accessing Azure Data Lake with Service Principal
# MAGIC 1. Register Azure AD Application / Service Principal
# MAGIC 2. Generate a secret password for the Application
# MAGIC 3. Set Spark config with App / Client Id, Directory / Tenant Id & Secret
# MAGIC 4. Assign Role 'Storage Blob Data Contributor' to the Data Lake

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.f1datalakes.dfs.core.windows.net",
    "fpgBuhQVVczHjal5xtyVtou0T/xU8g1Bh982f/foR6RLq7+uxLOkxBQ0J7R2Zob/c+KwU7ymbT0p+ASt1+NoHw=="
)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@f1datalakes.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@f1datalakes.dfs.core.windows.net/circuits.csv"))