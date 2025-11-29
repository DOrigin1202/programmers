"""
문제 설명
문자열 my_string과 정수 배열 indices가 주어질 때, my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ indices의 길이 < my_string의 길이 ≤ 100
my_string은 영소문자로만 이루어져 있습니다
0 ≤ indices의 원소 < my_string의 길이
indices의 원소는 모두 서로 다릅니다.
입출력 예
my_string	indices	result
"apporoograpemmemprs"	[1, 16, 6, 15, 0, 10, 11, 3]	"programmers"
입출력 예 설명
입출력 예 #1

예제 1번의 my_string의 인덱스가 잘 보이도록 표를 만들면 다음과 같습니다.
index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18
my_string	a	p	p	o	r	o	o	g	r	a	p	e	m	m	e	m	p	r	s
`indices`에 있는 인덱스의 글자들을 지우고 이어붙이면 "programmers"가 되므로 이를 return 합니다.
"""

#내가 제출한 답
def solution(my_string, indices):
    answer = []

    # 먼저 indices를 오름차순으로 정렬을 해야하는데
    #indices.sorted()
    
    sorted_indices = sorted(indices)
    print(sorted_indices)
    for i in range(0,len(my_string)):
        answer.append(my_string[i])
    for j in sorted_indices:
        int(j)
        answer = answer.pop(answer[j])
    return answer

#정답
def solution(my_string, indices):
    answer = []

    sorted_indices = sorted(indices, reverse = True)
    
    for i in range(0,len(my_string)):
        answer.append(my_string[i])
        
    for j in sorted_indices:
        answer.pop(j)
    return ''.join(answer)

# 틀린 이유
#1. pop은 인덱스를 받는데, answer[j]는 값이기 때문에 answer.pop(j)같이 사용해주어야 한다.

#2. sorted하는 과정에서 pop을 수행해 왼쪽에서부터 pop을 수행하게 되면 작은수부터 빠져나가면서 index가 바뀌게 되어 pop되는 값이 계속해서 달라진다.
    # 이런 방법을 타기 해기 위해서는 뒤에서 부터 pop을 하면 된다.

#3. ‘’.join(answer)로 하면 리스트를 str으로 변환

#4. answer.pop(j)를 수행할때
    
    #answer =  answer.pop(j)이렇게 하면 문제가 발생 pop(j)는 지워진 요소 하나를 반환함 즉 위와 같이 하면 ‘P’하나의 값을 answer에 재 선언하게 되는 것이고 이 P하나 있는 answer을 다시 pop하게 되면 str을 pop할 수 없다는 문구가 나오면서 에러가 발생하는 것이다.