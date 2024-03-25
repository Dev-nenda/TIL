# 3.2 MySQL을 이용한 데이터베이스 구축절차

데이터베이스를 구축하는 가장 기본적인 순서
1. 데이터베이스 생성
2. 테이블 생성
3. 데이터 입력
4. 데이터 조회/활용

## 3.2.1 데이터베이스 생성

### step0

- worckbench 실행 후 root 사용자의 localhost 3306으로 접속
- Administration과 Schemas로 구분 된 탭에서 Schemas탭을 기본적으로 클릭해 놓는다.
- **MySQL에서는 스키마와 데이터베이스가 완전히 동일한 용어로 사용(다른 DBMS에서는 개별용어)**

### step1
- Workbench의 SCHEMAS에서 마우스 우클릭 후 Create Schema(=Create Database)를 선택
- 데이터베이스의 이름을 shopdb로 입력 후 Apply 클릭
- Apply SQL Script to Database창에서 SQL문이 자동으로 생성
- Apply와 Finish를 클릭하면 shopdb 데이터베이스 추가
- **CREATE SCHEMA 'shopdb'** 문을 쿼리 창에서 입력하는 것과 동일한 작동
- File >> Close Tab >> Don't Save

## 3.2.2 테이블 생성

### step0

- 테이블 생성 전 각 열의 영문 이름 및 데이터 형식을 정해야 한다.
- **개체(데이터베이스, 테이블, 열 등) 이름은 영문을 사용해야 한다.**
- 한글로 사용하게 되면 호환성 등 추후에 문제가 발생할 소지가 많다.
- ex) 회원 테이블(memberTBL)의 데이터 형식을 다음과 같이 지정

    |열 이름(한글)|영문 이름|데이터 형식|길이|NULL 허용|
    |-|-|-|-|-|
    |아이디|memberID|문자(CHAR)|8글자(영문)|x|
    |회원 이름|memeberName|문자(CHAR)|5글자(한글)|x|
    |주소|memberAddress|문자(CHAR)|20글자(한글)|O|

**NULL 허용**은 아무것도 입력하지 않는 것을 허용하는지 여부를 나타낸다

### step1

- Workbench의 Navigator >> SCHEMAS 에서 shopdb를 확장하고 Tables를 선택한 후, Create TAble
- 테이블 이름에 'memberTBL'을 입력 > APPLY
- 열 이름을 더블 클릭해서 입력, 데이터 형식은 직접 입력 or 드롭다운
- 아이디와 회원이름은 NN에서 체크를 킨다(NOT NULL)
- 아이디(memberID) 기본 키로 설정 >> APPLY
    
    **경고창이 나올텐데, MySQL에서 대소문자를 모두 소문자로 처리한다는 경고창이다**
- Apply SQL Script to Database 창이 나오면 자동으로 SQL문이 생성되어 있고, Apply >> Finish를 클릭하면 자동 적용

### step2
- 같은 방식으로 productTBL을 생성 후 저장

### step3

- 생성 된 테이블을 확인
- ShopDB의 테이블에서 확장을하면 두개의 테이블이 생성

    **테이블이 보이지 않는다면 Refresh All을 클릭하면 생성 확인**

## 3.2.3 데이터 입력

### step1
- Navigator의 SCHEMAS에서 ShopDB >> Tables >> memberTBL 선택 후 Select Rows - Limits 1000 선택
- 오른쪽 아래 Result Grid에서 데이터 입력

    **중간에 데이터를 잘못 입력했다면 삭제할 행의 앞부분에서 마우스 우클릭 후 삭제 선택**

### step2
- 동일한 방법으로 productTBL 데이터 입력

    ** 데이터 입력 SQL `INSERT INTO ...` 삭제하는 SQL `DELETE ...`

## 3.2.4 데이터 활용

### step0
- 기존 쿼리창을 모두 닫고 새로운 쿼리창을 하나 열기
- Navigator에서 ShopDB를 더블 클릭하면 진한 색으로 바뀐다.(쿼리창에 작성할 SQL문이 선택된 데이터베이스에 적용된다는 의미)

### step1

 ```SQL
 SELECT * FROM productTBL; -- 입력후 Ctrl + Shift + Enter로 실행
 ```

**IntelliSense 기능을 제공하므로 예약어의 경우에는 탭을 눌러 선택가능, 단 마리아 디비를 같은 컴퓨터에서 사용할 경우 기능이 되지 않을 수 있다.**

- SELECT의 기본 형식은 SELECT 열 이름 FROM 테이블 이름 [WHERE 조건] 형식
- `*`는 모든 열을 의미
- 회원 테이블 중 이름과 주소만 출력하기

    ```SQL
    SELECT memberName, memberAddress FROM memberTBL;
    ```
    
- '지운이' 정보만 추출하기
    
    ```SQL
    SELECT * FROM memberTBL WhERE memberName = '지운이' ;
    ```
    해당 코드를 실행할 경우 이전 모든 쿼리문이 실행 되는데, 이를 방지하기 위해 실행하고 싶은 SQL문을 드래그 후 실행

### step2

- 간단한 테이블을 생성하는 SQL 문

    ```SQL
    CREATE TABLE \`my TestTBL` (id INT) ;
    ```
     
- 쿼리문 입력후 생성된 테이블이 보이지 않을 경우 Refresh All
- 
### step3

- 테이블을 삭제하는 SQL문

    ```SQL
    DROP TABLE \`my TestTBL` ;
    ```

