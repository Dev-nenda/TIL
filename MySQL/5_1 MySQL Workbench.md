# 5.1 MySQL Workbench

주요기능
- 데이터베이스 연결 기능
- 인스턴스 관리
- 위저드를 이용한 MySQL의 동작
- 통합된 기능의 SQL 편집기
- 데이터베이스 모델링 기능
- 포워드/리버스 엔지니어링 기능
- 데이터베이스 인스턴스 시작/종료
- 데이터베이스 내보내기/가져오기
- 데이터베이스 계정관리

## 5.1.1  실행

MySQL Workbench 실행

## 5.1.2 MySQL Connections

접속 될 서버와 사용자, 포트를 선택 후 접속을 시도
기본 값으로는 MySQL의 관리자인 'root' 사용자, 서버는 자신의 컴퓨터를 의미하는 'localhost', 포트는 '3306'으로 접속

다른 서버로 접속하기 위해서는 Local instance MySQL에서 Edit Connection을 통해 추가로 접속할 서버를 등록 혹은 편집 가능

### Connection 탭

Connection method
- Standard(TCP/IP)
- Local Socket/Pipe
- Standard TCP/IP over SSH

대부분 Standard(TCP/IP) 사용

### Parameters 탭

Hostname에 접속할 컴퓨터가 외부에 있다면 접속할 서버 컴퓨터의 IP를 작성

Port는 접속할 MySQL의 포트번호를 적는다. 특별한 경우가 아니면 3306을 사용하지만 보안을 위해 서버 컴퓨터에서 포트를 변경할 수도 있음

Username은 접속할 MySQL 사용자를 적어줌

Password에서 Store in Vault... 를 클릭하면 미리 사용자의 비밀번호 저장 Clear를 클릭하면 저장해 둔 비밀번호를 지운다.

Default Schema는 접속 후에 기본적으로 선택되는 데이터베이스 이름

### SSL 탭

SSL(Secure Socket Layer)은 보안을 위한 암호 규약

서버와 클라이언트가 통신할 때 암호화를 통해서 비밀을 유지시켜주고 보안을 강화

특별히 설정하지 않았다면 그대로 놔둔다.

### Advanced 탭

프로토콜의 압축, 인증 방식을 설정

### Remote Management 탭

원격 관리를 위해 설정하는 부분

활성화를 위해서는 Hostname이 127.0.0.1을 제외한 실제 IP 주소가 설정되어 있어야 한다.

Native Windows remove Management를 선택하면 MySQL 서버가 설치된 OS가 Windows인 경우에만 설정 가능

SSH login  based management는 SSH 서버 기반으로 원격 접속

### System Profile 탭

접속할 서버의 OS 종류 및  MySQL 설정 파일의 경로등을 설정한다.

활성화를 위해서는 Remote Management 탭에서 Native Windows remove Management나 SSH login based management가 선택되어 있어야 함

System Type
- FreeBSD
- Linux
- MacOS X
- OpenSolaris
- Windows

Configuration Type 은 MySQL의 설정 파일이 경로와 함께 저장

Configuration File Section은 서버의 서비스 이름을 저장
MySQL Management에서는 MySQL 서비스를 시작 혹은 중지하는 시스템 명령어를 적어줌

## 5.1.3 MySQL Workbench의 화면구성

### 패널

오른쪽 상단의 아이콘 3개는 패널 3개를  On/Off 하는 기능을 제공

### 내비게이터

Schema 탭
- 데이터베이스(=스키마) 생성 및 삭제
- 데이터베이스 개체(테이블, 뷰, 인덱스, 저장 프로시저, 함수 등) 생성 및 관리
- 데이터베이스의 속성을 조회

Administration 탭
- Management
  - MySQL 서버의 가동 상태, 설치된 폴더 등을 확인
  - MySQL 서버에 연결되어 잇는 클라이언트의 정보를 확인
  - 사용자의 생성, 삭제 및 권한 관리
  - 서버 변숫값의 확인
  - 데이터 내보내기/가져오기
- Instance
  - MySQL 연결 정보 관리
  - MySQL 인스턴스의 중지, 시작
  - Server에 기록된 로그 조회
  - MySQL 옵션 파일의 설정 정보 확인 및 변경
- Performance
  - 네트워크 상태 및 MySQL의 성능 상태를 확인
  - 성능 상태의 보고서 작성
  - 성능 구성의 설정

Navigator의 Schemas는 트리 형태로 구성

각 항목을 확장 및 축소 가능

### 쿼리창

쿼리 문장을 입력하고 실행하는 텍스트 에디터

1. Workbench의 상단 제일 왼쪽 Create a new SQL tab for executing queries 아이콘 클릭
2. 작업할 데이터베이스를 Schemas 탭에서 더블 클릭해서 선택
3. SQL 문 입력
4. Ctrl + Shift + Enter를 눌러 실행
5. 아래쪽의 결과창을 통해 결과 확인