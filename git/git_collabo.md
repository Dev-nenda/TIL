# Git-Collabo

## Repo 생성
이전과 다르게 github remote repo 생성을 한다.

intitialize repo 하위 항목(README, .gitignore)에 체크시 remote에서 root commit이 발생한다. 

### git push origin \<branch-name>
1. `git push origin master` 

    `origin`이라는 이름의 원격저장소에 나의 로컬저장소 `master` branch를 push하겠다.

2. `git push origin a` 

    `origin` 이라는 이름의 원격저장소에 내 로컬저장소 `a` branch를 push하겠다.

### git pull origin \<branch-name>

1. `git pull origin master` 

     `origin`의 `master` branch를  **현재 local HEAD branch** 에 받겠다. 

## Merge 

Conflict 발생하지 않을 경우
1. 각자 branch 생성
2. 각자 작업 실행
3. 작업 후 push 진행
4. PR open
5. 상대방에게 리뷰 및 merge 요청
6. 상대방이 확인 후 merge를 진행

Conflict 발생할 경우
1. 각자 branch 생성
2. 각자 작업 실행
3. 작업 후 push 진행
4. PR open
5. 같은 파일을 작업하였을 경우 PR진행 중 conflict 발생
6. PR 에서 comment와 code lin review 진행
7. 최종 협의 후 merge

## Git Contribute(Fork)

[Git countribute(Fork) 하기](https://git-scm.com/book/ko/v2/GitHub-GitHub-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%97%90-%EA%B8%B0%EC%97%AC%ED%95%98%EA%B8%B0)
