N, M = map(int, input().split())


# N-1 만큼의 횟수로 자른 후
# N개의 조각을 다시 M-1개의 금으로 잘라줘야 한다.
print((N-1)+(N*(M-1)))