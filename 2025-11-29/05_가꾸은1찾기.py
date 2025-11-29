# 처음에 내가 제시한 답 
# 테스트만 통과
def solution(arr, idx):
    answer = 0
    for j in range(len(arr)-1,idx-1,-1):# 5,3,-1
        if arr[j] == 1 and arr[j] >= arr[idx]:
            answer = j
            return answer
    
    return -1


# 실제 정답
def solution(arr, idx):
    # idx보다 큰 인덱스부터 앞에서부터 탐색
    for i in range(idx + 1, len(arr)):
        if arr[i] == 1:
            return i  # 첫 번째로 찾은 게 가장 작은 인덱스
    
    return -1  # 못 찾으면 -1

"""
문제는… 해당 문제를 잘못 이해했다는 피드백을 받음

1. 리스트 arr을 접근하는 방법이 뒤에서 부터 접근하면 가장 큰 리스트의 인덱스를 반환하게 되는데 지금 요구하는 문제는 조건에 성립할때 가장 작은 인덱스 값을 반환하는 것. 그러므로 for i in range()구조를 바꿔줘야 할 필요가 있음
2. 다음은 if안의 구조가 잘못 되었음. for문 구조를 바꾸게 됨으로써 자연스럽게 if안의 구조도 바뀌어야함.’

여기서 key포인트는 역시 for문을 구성하는 부분인데 for  j in range(idx, len(arr))을 통해서 idx로 입력받은 숫자에서 부터 arr의 len의 길이만큼을 반복 조건을 설정하고 그에 해당하는 조건의 인덱스를 찾는
"""