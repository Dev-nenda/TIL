# Git
1. 컴퓨터에 Git 설치시 최초 1회 해야하는 것들
    
     `git config --global user.name '<name>'`
     `git config --global user.email '<email>'`
2. `git init` => 초기화 => 현재위치에 `.git/` 생성 => 터미널에(master)가 보임
3. `rm -rf .git/` => git init 을 취소(되돌림)
4. `git init` 을 통해 관리하는 폴더는 REpo라고 부르자
5. 주의사항 *repo 안에 repo 생성 금지*


## Git 명령어
1. `git add` : 파일의 변경사항 스테이징
2. `git commit` : 파일의 변경사항 커밋
   1. 커밋 기록확인 : `git log`
3. Git의 3가지 상태공간
   1. Workding Directory
   2. Stage
   3. Commits
4. Git에서 파일의 상태
   1. 확인하는 명령어 : `git status`
   2. Untracked
      1. Unmodified
      2. Modified
      3. Satged
5. Git이 관리하지 않을 파일들은 `.gitignore`에 작성
   1. https://gitignore.io
6. commit 할 때 `-m` 옵션을 붙이지 않으면 vim이 켜진다

## Github 명령어
1. `git remote add <name> <URL>` : 로컬에 원격저장소 추가
   1. `git remote add origin <URL>`
2. `git push <name> <branch>` : \<name> 원격저장소에 \<branch> 업로드
3. `git clone <URL>` : 현재 터미널 pwd 원격 저장소 복제(clone)=> 최초 1회만 하면 된다.
4. `git pull <name> <branch>` : \<name> 원격저장소의 \<branch> 변경사항 다운로드

**_항상 작성 후 push, 작성 전 pull_**
