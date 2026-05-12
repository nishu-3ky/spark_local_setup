from pyspark.sql import SparkSession
import time
import os

os.environ["HADOOP_HOME"] = r"C:\Program Files\hadoop"
os.environ["hadoop.home.dir"] = r"C:\Program Files\hadoop"

spark = SparkSession.builder \
    .appName("MyJob") \
    .master("local[*]") \
    .config("spark.executor.cores", "2") \
    .config("spark.cores.max", "4") \
    .config("spark.executor.memory", "1g") \
    .config("spark.sql.shuffle.partitions", "4") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.RawLocalFileSystem") \
    .config("spark.hadoop.fs.AbstractFileSystem.file.impl", "org.apache.hadoop.fs.local.LocalFs")\
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

print("\n\n=== Reading CSV ===\n")

df = spark.read.csv(
    "data/input/data.csv",
    header=True,
    inferSchema=True
)

df.show()

print("\n\n=== Writing Output ===\n")

output_path = "file:///D:/prep/DataEngineer/PySpark/SetupCode/spark_local_setup/data/output/result"

df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(output_path)

print("Write Successful")

spark.stop()