answer = [1, 2, 1, 4, 5, 2, 9]

def solution(arr):
    if 2 not in arr:
        return [-1]
    
    a = arr.index(2)
    b = len(arr)-1-arr[::-1].index(2)
    
    return arr[a:b+1]

if __name__ == "__main__":
    
    
    print(solution(answer))
    
    
"""
arr[::-1]은 리스트를 반대로 뒤집는 형태,
그러면 [9,2,5,6,1,2,1] 이렇게 됨.

이후 인덱스의 값이 2 인 것들을 찾아라.

index(2)를 통해서 값이 2인 인덱스를 왼쪽에서부터 가장 빠르게 찾아라. 

그러고 나서 총 arr의 길이 - 역으로 뒤집은 리스트에서 2를 찾아라.

"""