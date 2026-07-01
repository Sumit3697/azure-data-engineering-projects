from pyspark.sql import SparkSession
from delta import *

spark = SparkSession.builder \
    .appName("Medallion-Bronze") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# API se data laao - dummy URL hai, chal jayega
import requests
data = requests.get("https://jsonplaceholder.typicode.com/users").json()
df = spark.createDataFrame(data)

# Bronze Delta table me daal do
df.write.format("delta").mode("overwrite").save("./bronze/users_delta")
print("Bronze layer loaded: 10 records ingested to Delta Lake")
spark.stop()
