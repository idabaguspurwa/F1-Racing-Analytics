# Databricks notebook source
# MAGIC %md
# MAGIC Exploring Capabilities of the db.utils secret utility

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list(scope='f1-scope')

# COMMAND ----------

dbutils.secrets.get(scope='f1-scope', key='f1datalakes-account-key')