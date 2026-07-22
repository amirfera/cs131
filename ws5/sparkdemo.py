import sys

from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

spark = (
    SparkSession.builder
    .appName("ws5-regression")
    .getOrCreate()
)

input_path = sys.argv[1]

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(input_path)
)

df.show()

assembler = VectorAssembler(
    inputCols=["total_bill", "size"],
    outputCol="features"
)

train_df, test_df = df.randomSplit([0.8, 0.2], seed=131)

lr = LinearRegression(
    featuresCol="features",
    labelCol="tip"
)

pipeline = Pipeline(stages=[assembler, lr])

pipelineModel = pipeline.fit(train_df)

predictions = pipelineModel.transform(test_df)

evaluator = RegressionEvaluator(
    labelCol="tip",
    predictionCol="prediction"
)

rmse = evaluator.setMetricName("rmse").evaluate(predictions)
r2 = evaluator.setMetricName("r2").evaluate(predictions)

model = pipelineModel.stages[-1]

print(f"Coefficients: {model.coefficients}")
print(f"Intercept: {model.intercept}")
print(f"RMSE: {rmse}")
print(f"R²: {r2}")

spark.stop()
