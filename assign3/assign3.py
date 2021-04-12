

from csv import reader
from pyspark import SparkContext, SparkConf



sc = SparkContext(appName="Assign3SparkProg")
sc.setLogLevel("ERROR")
data = sc.textFile("hdfs://10.56.2.183:54310/hw2-input/NYPD_Complaint_Data_Current_YTD.csv")


# This uses csv reader to split each line of the file, then filter for July (row[5] is RPT_DT column)
splitdata = data.mapPartitions(lambda x: reader(x)).filter(lambda row: row[5].startswith('07'))
#Count the number of each crime committed (row[7] is OFNS_DESC column)
topCrimes = splitdata.map(lambda row: (row[7], 1)).reduceByKey(lambda a, b: a + b)

output = topCrimes.collect()

print("The top 3 crimes in July are:")

for (crime, number) in output[0:3]:
    print(crime, number)

