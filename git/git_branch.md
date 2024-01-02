# Branch
Branch는 스티커(포인터)이다. 

## 명령어

|명령어|내용|
|-|-|
|`master`|상징적인 Branch : 제대로 동작하는 SW|
|`Head`| 현재 작업 중인 commit/Branch|
|`git log --oneline`| 로그 짧게 한줄로 표시|
|`git log --oneline --graph` |로그 짧게 그래프로 표시|
|`git branch`| 현재 brach 목록보기|
|`git branch <branch-name>`|브랜치 생성|
|`git branch -d <branch-name>`|(병합 완료 된)브랜치 삭제|
|`git branch -D <branch-name>`|(병합 완료 안된) 브랜치 강제 삭제|
|`git switch <branch-name>`|브랜치 변경(`head`)|
|`git switch -c <bracn-name>`|브랜치 생성&변경|
|`checkout` | branch 와 commit id 두개 모두 사용가능|
|`switch`|branch 이름만 사용가능|
|`git merge <target-branch>`| 현재 `head`가 위치한 branch와 `target-branch`를 병합|
|`git reset`| commit의 변경사항을 되돌림|
|`git commit --amend`| 직전 커밋 수정|
|`git commit`| `-m` 옵션없이 길게 메세지 작성 가능|
|`git config --global alias.logog 'log --oneline --graph'`| `git alias`(별명기능)|

## Merge
1. FF(Fast Fowrd)
2. Auto Merge
3. Auto Merge FAIL => Merge Conflict
   1. `both modified` 파일을 수정
   2. `add`
   3. `commit`

## Reset
1. `git reset --soft HEAD~` : 마지막 커밋의 변경사항을 stage 상태로 되돌림(staged)
2. `git reset --mixed HEAD~`/`git reset HEAD~` : 마지막 커밋의 변경사항을 stage 하지않음 (modified)
3. `git reset --hard HEAD~` : **_변경사항 날아감 : 마지막 커밋의 변경사항을 모두 삭제(unmodified)_**

## Alias
`git config --global alias.logog 'log --oneline --graph`
위 설정 등록후 `git logog` 실행시 `git log --oneline --graph` 실행됨



### 오늘의 실습

```
위 명령어를 사용해 branch 생성 및 병합, 삭제를 실행해본다.
```
### 참고

[Branch란 무엇인가?](https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80)

[Branch 시각화 사이트](https://git-school.github.io/visualizing-git/)

