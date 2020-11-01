# 해설
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input("n, m : ").split())

# 2차원 리스트의 맵 정보 입력 받기
graph = [[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 4
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    # 이미 방문한 노드
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력