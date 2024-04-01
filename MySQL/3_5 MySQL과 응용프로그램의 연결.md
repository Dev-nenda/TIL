# 3.5 MySQL과 응용프로그램의 연결

Microsoft Visual Studio Community를 이용한 웹과 데이터베이스 연동 실습

## step 1
Visual Studio Community 2017 설치
- 설치 화면 중 ASP.NET 및 웹 개발 부분만 체크 후 설치
- 설치 완료 후 실행
- 나중에 로그인 선택 후 친숙한 환경에서 시작을 기본에서 놔둔 상태로 시작

## step 2
Connector/ODBC 설치

## step 3

ODBC Data source 실행
- 시스템 DSN 탭 클릭
- 추가 버튼 클릭
- MySQL ODBC 8.0 Unicode Driver 선택 후 마침
- Data source name, user, password, database 선택 후 test로 성공 메세지가 나온다면 확인

## step 4
Visual Studio 2017 실행
- 파일 >> 새로만들기 >> 프로젝트 >> Visual C# >> 웹 >> 이전버전 >> ASP.NET
- 오른쪽 솔루션 탐색기에서 Website(1) >> 추가 >> WebForm >> 확인
- 왼쪽 아래 디자인 >> 도구상자 >> 데이터 >> SqlDAtaSource 더블클릭
- 데이터 소스 구성 선택
- 새연결 >> Microsoft ODBC 데이터소스
- 연결추가 >> 사용ㅈ 또는 시스템 데이터 소스 이름사용 >> 앞서만든 ODBC로 선택
- 응용 프로그램 구성 파일에 연결 문자열 저장도 기본 값 
- Select 문 구성 >> 사용자 지정 SQL문 또는 스토어드 프로시저 지정
- 사용자 지정 문 또는 스토어드 프로시저 정의  >> SELECT * FROM memberTBL
- 쿼리테스트 >> 쿼리테스트 
- 도구상자 >> ListView
- 데이터 소스 선택 >> SqlDataSource1 >> List View