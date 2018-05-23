# Hadoop
### 하둡을 왜 쓰는가?
- 하나의 컴퓨터에서 처리할 수 없는 대용량의 데이터를 나누어 처리하기 위해 사용

**장점**
- Computing power
- Fault tolerance
- Flexibility
- Low cost
- Scalability


하둡의 메인은 기본적으로 다음과 같이 구성
- HDFS (Hadoop Distributed File System)
  - 하둡 분산 파일 시스템
- MapReduce
  - 분산 처리 프레임 워크
- YARN (yet another resource negotiator)
  - 클러스터 자원 관리

위 기반을 바탕으로 Hive, Hbase, Spark, Pig, Mahout 등의 application 생태계가 구성됨


### 기본 설정
VirtualBox - hortenworks sandbox 이용

1. **Web interface**
 - http://127.0.0.1:8888/ 로 접속

1. **CMD 명령어**
  - Putty, ssh, http://127.0.0.1:4200/ 등으로 HDFS의 명령행에 접근이 가능하다.
  - 일반적인 linux 명령어 사용 가능
  - root 권한이 없으면 각 노드의 filesystem만 조작이 가능. 필요시 `sudo su` 혹은 루트 계정으로 로그인
  - Hadoop File System 조작예) `hadoop fs -ls`

## HIVE
하둡 시스템의 데이터베이스
- HiveQL을 맵리듀스 작업으로 변환하고 하둡 환경에서 실행
- 관계형 데이터베이스는 아니지만, SQL 기반 명령어 사용 가능

## Spark
맵리듀스와 유사한 클러스터 컴퓨팅 프레임 워크
- 하지만 분산 파일 시스템 상의 파일에 대한 저장과 자원관리를 하지 않는다.
  - 따라서 하둡의 다른 시스템에 의존
- 회복가능 분산 데이터셋(Resilient Distributed Datasets, RDD)를 사용
  - RDD는 분산된 메모리 추상화로써, 메모리 내에서 계산을 수행하게 해줌.

  #### Spark의 구성
  NoSQL 환경 제공, 일괄처리 및 대화형 모드 실행 가능
  - Spark streaming : 실시간 분석
  - Spark SQL
  - MLLib : 머신러닝
  - GraphX : 그래프 데이터베이스
