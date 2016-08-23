
# hadoop bin
export PATH=$PATH:"/Users/chenshan/google_driver/github/ipython-notebook-spark/hadoop-2.0.0-cdh4.5.0/bin"
export PATH=$PATH:"/Users/chenshan/google_driver/github/ipython-notebook-spark/spark-1.6.0-bin-cdh4/spark-1.6.0-bin-cdh4/bin"
export PATH=$PATH:"/Users/chenshan/google_driver/github/ipython-notebook-spark/spark-1.6.0-bin-cdh4/spark-1.6.0-bin-cdh4/python"
export PATH=$PATH:"/Users/chenshan/google_driver/github/ipython-notebook-spark/spark-1.6.0-bin-cdh4/spark-1.6.0-bin-cdh4/python/lib/py4j-0.9-src.zip"

### make the bin of spark and hadoop accessiable
export SPARK_HOME="/Users/chenshan/google_driver/github/ipython-notebook-spark/spark-1.6.0-bin-cdh4/spark-1.6.0-bin-cdh4"
export SUBMISSION_OPTS="--master spark://10.21.208.21:7077 --deploy-mode client"
