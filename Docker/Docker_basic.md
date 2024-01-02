# Docker
Docker 컨테이너는 애플리케이션의 모든 코드 및 종속성을 표준 형식으로 패키징할 수 있게 해주는 컨테이너이다. 

이를 통해 애플리케이션이 컴퓨팅 환경 전반에서 빠르고 안정적으로 실행이 가능하다.

---
## Image와 Container

### Image
Docker에서 image란 컨테이너로 실행될 소프트웨어 모음이다. Docker 플랫폼에서 실행할 수 있는 컨테이너 생성 지침이 포함되어 있다.

### Container
Docker에서 Container는 Image로부터 생성되며, 호스트 운영체제에서 실행되는 Container는 코드와 모든 종속성을 패키지화하여 애플리케이션이 **한 환경에서 다른 환경으로** 빠르고안정적으로 실행될 수 있게 해주는 표준 소프트웨어 장치이다.

쉽게 비유하자면, Image는 도장이고, Container는 Image라는 도장으로 찍어내는 결과물이다. 
그러므로 하나의 Image로 다수의 Conatainer를 생성할 수 있다.

---

## Docker 명령어

|명령어|내용|
|-|-|
|`$ docker run <image-name>`| 컨테이너를 생성+실행|
|`$ docker run <image-name> <command>`|컨테이너 생성+실행+시작 커맨드 override|
|`$ docker ps`|실행중인 컨테이너 목록|
|`$ docker ps -a`|모든 컨테이너 목록|
|`$ docker create <image-name>`|이미지를 생성|
|`$ docker start <container-ID>`|컨테이너 실행|
|`$ docker start -a <container-ID>`|`STDOUT`/`STDERR` 출력하며 컨테이너 실행|
|`$ docker system prune`|모든 종료된 컨테이너 및 기타 삭제|
|`$ docker logs <container-ID>`|해당 컨테이너의 출력기록(로그)확인 |
|`$ docker kill <container-ID>`|해당 컨테이너 즉시 종료|
|`$ docker stop <container-ID>`|**해당 컨테이너 안전 종료(권장)**|
|`$ docker exec <container-ID> <command>`|실행중인 컨테이너에 새로운 명령어 실행|
|`$ docker exec -it <container-ID> <command>`|실행중인 컨테이너에 새로운 명령어 실행+입출력|
|`$ docker exec -it <container-ID> sh`|실행중인 컨테이너 내부의 `sh`실행+입출력|
|`$ docker run -it <image-name> sh`|새로운 컨테이너 생성+실행+`sh` 실행|

## Dockerfile

### Dockerfile 생성
|명령어(command)|내용|
|-|-|
|`create Dockerfile` | Docker 파일 생성|
|`$ docker build <build-context>`|build context(파일/폴더)를 기반으로 이미지 빌드|
|`$ docker build -t <name>/<pjt-name>:<version> <build-context>` | 빌드된 이미지에 태그 생성|

### Docker 파일 내부
|명령어(Instrucion)|내용|
|-|-|
|`FROM <image-name>`| 베이스 이미지 명시|
|`RUN <command>`|베이스 이미지에서 실행할 명령어|
|`CMD ["<command>"]`| 컨테이너 시작 명령어 설정|

## Docker Compose

Docker Compose란, 여러개의 컨테이너로부터 이루어진 서비스를 구축, 실행하는 순서를 자동으로 하여, 관리를 간단히 하는 기능이다.

### 명령어

|명령어|내용|
|-|-|
|`docker-compose up`|`docker-compose.yml` 파일을 기준으로 컨테이너 실행|
|`docker-compose up --build`|다시 빌드하고 실행|
|`docker-compose up -d`|터미널이 아닌 백그라운드에서 실행|
|`docker-compose down`|docker-compose로 실행 중인 모든 컨테이너 종료|
|`docker-compose ps`|`docker-compose.yml`을 기준으로 실행 중인 컨테이너 확인|


### 재시작 정책

|policy name|내용|
|-|-|
|`'no'`|어떠한 이유로도 종료된 컨테이너를 다시 실행하지 않는다.(`'`필수 =>`yaml`문서에서 `no`는 `false`를 의미하기 때문에 문자열로 표시)|
|`always`|언제나 종료된 컨테이너를 다시 실행한다.(`'`생략 가능)
|`on-failure`|에러 (코드)|
|`unless-stopped`|일반적으로 종료되면 다시 실행하나, 개발자가 강제로 종료한 경우에는 다시 실행하지 않는다.|

