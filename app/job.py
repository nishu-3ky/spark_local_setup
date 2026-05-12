from pyspark.sql import SparkSession
import time


spark = SparkSession.builder \
    .appName("MyJob") \
    .master("local[*]") \
    .config("spark.executor.cores", "2") \
    .config("spark.cores.max", "4") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()

print("\n\n=== Reading CSV ===\n")
df = spark.read.csv("data/input/data.csv", header=True, inferSchema=True)
df.show()
df=df.filter(df.age>=28)
df.show()

print("\n\n=== Writing Output ===\n")
df.write.mode("overwrite").csv("data/output/result", header=True)

time.sleep(5000)