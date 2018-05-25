
# Spark
맵리듀스와 유사한 클러스터 컴퓨팅 프레임 워크
- 하지만 분산 파일 시스템 상의 파일에 대한 저장과 자원관리를 하지 않는다.
  - 따라서 하둡의 다른 시스템에 의존
- 회복 가능 분산 데이터셋(Resilient Distributed Datasets, RDD)을 사용
  - RDD는 분산된 메모리 추상화로써, 메모리 내에서 계산을 수행하게 해줌.

  #### Spark의 구성
  NoSQL 환경 제공, 일괄처리 및 대화형 모드 실행 가능
  - Spark streaming : 실시간 분석
  - Spark SQL : 데이터베이스
  - MLLib : 머신러닝
  - GraphX : 그래프 데이터베이스



**공부할 때는 python으로 ok, 하지만 production level 에서는 scala 필요.**
- 스파크는 스칼라로 쓰여졌음 (둘 다 자바 베이스)
- 스칼라로 훨씬 효율적인 코드 생산이 가능

python을 배운 상태에서 scala로 배우는 것이 그리 어렵지는 않다고 한다.

```python
# python
nums = sc.parallelize([1, 2, 3, 4])
squared = nums.map(lambda x:x*x).collect()
```
```scala
// scala
val nums = sc.parallelize(List(1, 2, 3, 4))
val squared = nums.map(x => x*x).collect()
```
[Scala Install Guide](https://www.scala-lang.org/download/2.11.8.html)

[Scala Tutorial](https://twitter.github.io/scala_school/ko/index.html) - 한국어 번역

---

# RDD
- Resilient 회복 가능
- Distributed 분산
- Dataset 데이터셋

### Creating RDD's
```python
# 1
lines = parallelize([1, 2, 3, 4])

# 2
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("appName")
sc = SparkContext(conf = conf)
# 스파크 쉘에는 sc로 SparkContext가 초기화 되어있으므로 쉘에서는 가져다 쓰면 됨.

lines = sc.textFile("hdfs:///user/maria_dev/fileName")
                    # or s3n:// , file://

# 3
hiveCtx = HiveContext(sc)
rows = hiveCtx.sql("SELECT name, age FROM users")

```

### Transforming RDD's
아래와 같은 명령어로 RDD를 변형시킬 수 있다.

    map, flatmap, filter, distinct, sample, union, intersection, subtract, cartesian

```python
# map example
rdd = sc.parallelize([1, 2, 3, 4])
squaredRDD = rdd.map(lambda x: x*x)

# This yields [1, 4, 9, 16]
```

### RDD actions
```
collect, count, countByValue, take, top, reduce, etc...
```

### Lazy evaluation
- 텐서플로우와 비슷하게 action을 하기 전까지 실제 연산은 실행되지 않는다.
---


### Working with structured data
- Extends RDD to a "DataFrame" object

Using SparkSQL in Python
```python
from pyspark.sql import SQLContext, Row
hive Context = HiveContext(sc)
inputData = spark.read.json(dataFile)
inputData.createOrReplaceTempView("myStructuredStuff")

myResultDataFrame = HiveContext.sql("""SELECT foo FROM bar ORDER BY foobar""")

# DataFrame 메소드
myResultDataFrame.show()
myResultDataFrame.select("someFieldName")
myResultDataFrame.filter(myResultDataFrame("someFieldName" > 200))
myResultDataFrame.rdd().map(mapperFunction)
```

Spark1, 2 전환 명령어

    export SPARK_MAJOR_VERSION=2 (or 1)


## Quiz

1. finding the lowest-rated movies were polluted with movies only rated by one or two people.
1. Modify one or both of these scripts to only consier movies with at least ten ratings
- 10개 이상 평가 받은 영화 중 별이 가장 낮은 영화 10개 찾기
