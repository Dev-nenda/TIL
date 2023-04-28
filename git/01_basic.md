# 실습
## ~에 완전히 새로운 리포(test-repo/)를 생성
```
$ mkdir test-repo/
$ cd test-repo/
$ git init
Initialized empty Git repository in C:/Users/judge/test-repo/.git/
```

## README.md를 생성하고 커밋
### 메세지는 First Commit

```
$ touch README.md
$ git add README.md
$ git commit -m 'First Commit'
```
## README.md 에 간략한 자기소개를 작성하고 커밋
### 이때는 -m 옵션 없이 진행
### 메세지는 Add Intro
### vim 사용을 잊지 말자

```
$ git add README.md
$ git commit
# vim이 켜지면 i를 누르고 Add Intro 입력 후 esc :wq
```

##