# def dfs(graph, visited, node):
#     visited[node] = True
#     for neighbor in graph[node]:
#         if not visited[neighbor]:
#             if neighbor != node + 1:
#                 return False
#             if not dfs(graph, visited, neighbor):
#                 return False
#     return True
#
# def solution(N, A, B):
#     graph = {i: [] for i in range(1, N + 1)}
#
#     for index in range(len(A)):
#         graph[A[index]].append(B[index])
#         graph[B[index]].append(A[index])
#
#     # DFS를 사용하여 그래프 순회 (노드의 개수 10만개, 간선의 개수 10만개이므로 메모리 사용량을 고려했을 때 DFS)
#     visited = [False] * (N + 1)
#     if not dfs(graph, visited, 1):
#         return False
#
#     for index in range(1, N + 1):
#         if not visited[index]:
#             return False
#
#     return True
def solution(N, S):
    def find_available_groups(seats, n):
        unavailable_seats = set()
        for seat in seats:
            row, column = seat.split()
            unavailable_seats.add((int(row), ord(column) - ord('A')))

        available_groups = 0
        for i in range(len(seats) - n + 1):
            consecutive_seats = [(row, column) for row, column in seats[i:i + n]]
            if all(seat not in unavailable_seats for seat in consecutive_seats):
                available_groups += 1

        return available_groups

    # 좌석 정보 분리
    seats_input = S.split()

    # 가능한 경우 계산
    available_groups = find_available_groups(seats_input, 4)

    return available_groups



if __name__ == '__main__':
    print(solution(2, '1A 2F 1C'))
