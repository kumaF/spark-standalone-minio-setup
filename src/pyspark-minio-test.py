import os

from dotenv import load_dotenv

from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col

from pyspark.sql.types import (
    StringType,
    DateType,
    DoubleType,
    IntegerType
)


load_dotenv()

s3_url: str = os.getenv('MINIO_URL')
s3_access_key: str = os.getenv('MINIO_ACCESS_KEY')
s3_secret_key: str = os.getenv('MINIO_SECRET_KEY')
spark_master_url: str = os.getenv('SPARK_MASTER_URL')

conf = SparkConf()

conf.set('spark.hadoop.fs.s3a.endpoint', s3_url)
conf.set('spark.hadoop.fs.s3a.access.key', s3_access_key)
conf.set('spark.hadoop.fs.s3a.secret.key', s3_secret_key)
conf.set('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
conf.set('spark.hadoop.fs.s3a.path.style.access', 'true')
# conf.set('spark.jars', '/Users/gh05t/Documents/projects/spark-minio/jars')
conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262')

spark = (
    SparkSession.builder
    .appName('spark-standalone-minio')
    .master(spark_master_url)
    .config(conf=conf)
    .getOrCreate()
)

print(f'spark version: {spark.version}')
print(spark._jsc.hadoopConfiguration().get('fs.s3a.endpoint'))


def load_stock_data(ticker: str):
    df = (
        spark.read
        .option('header', True)
        .csv(f's3a://data-bucket/stock-data/stocks/{ticker.upper()}.csv')
    )

    return df.select(
        col('Date').cast(DateType()).alias('date'),
        col('Open').cast(DoubleType()).alias('open'),
        col('High').cast(DoubleType()).alias('high'),
        col('Low').cast(DoubleType()).alias('low'),
        col('Close').cast(DoubleType()).alias('close'),
        col('Adj Close').cast(DoubleType()).alias('adj_close'),
        col('Volume').cast(IntegerType()).alias('volume')
    )


aapl = load_stock_data('aapl')
aapl.show(truncate=False)