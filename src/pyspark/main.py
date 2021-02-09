from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
print(spark.version)
print(spark.catalog.listTables())

query = 'SELECT * FROM tableName'
queryDf = spark.sql(query)

pdDF = queryDf.toPandas()

spark_temp = spark.createDataFrame(pdDF)
spark_temp.creatOrReplaceTempView("temp")

airports = spark.read.csv(FILE_PATH, header=True)
airprots.show()

flights = spark.table("flights")
flights = flights.withColumn("duration_hrs", flights.air_time/60)
