# Git 
Git은 형상 관리도구 중 하나로, 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.

장점으로, 소스코드를 따로 주고 받을 필요 없이, Git을 사용하면 하나의 프로젝트, 같은 파일을 여러사람이 동시에 작업하는 병렬 개발이 가능하다는 것이다.

작업 중간중간 commit을 잘하면 다시 코드를 되돌리기도 용이하고 관리하기가 좋다.

## Github
Github은 분산 버전 관리 툴인 Git을 사용하는 프로젝트를 지원하는 웹 호스팅 서비스이다. 개발자들의 클라우드라고 할 수 있다.

## 명령어

|명령어|내용|
|-|-|
|`git init`|해당 폴더를 Github의 repository로 만듬|
|`git remote ad origin 원격 저장소 주소`|`git remote`를 통해 repository 사이트와 폴더를 연결|
|`git add <file>` | 생성한 파일을 스테이징함|
|`git commit -m commit message'`| 스테이징한 파일을 commit함|
|`git push origin master`|repository 사이트에 백업|
|`reset`| 지정한 시점으로 완전히 되돌아감(`--hard` 옵션과 같이 사용할 경우 reset전 내용은 두 번 다시 볼 수 없다.)|
|`checkout`| 기존의 내용은 그대로 두고 지정한 시점으로 이동만 함|