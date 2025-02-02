import os

from dotenv import load_dotenv

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col

load_dotenv()

spark_master_url: str = os.getenv('SPARK_MASTER_URL')

spark = (
    SparkSession.builder
    .appName('spark-standalone')
    .master(spark_master_url)
    .getOrCreate()
)

print(f'spark version: {spark.version}\n')

df = spark.createDataFrame(
    [
      ('sue', 32),
      ('li', 3),
      ('bob', 75),
      ('heo', 13)
    ],
    [
      'first_name',
      'age'
    ]
)

df = df.withColumn(
    'life_stage',
    F.when(col('age') < 13, 'child')
    .when(col('age').between(13, 19), 'teenager')
    .otherwise('adult')
)

df.show(truncate=False)