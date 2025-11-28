"""
1. 문자열의 앞의 n글자

문제설명 : 문자열 my_string과 정수 n이 매개변수로 주어질 때, 
my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

제안사항 : 
my_string은 숫자와 알파벳으로 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000
1 ≤ n ≤ my_string의 길이

입출력 예
my_string	         n	    result
"ProgrammerS123"	11	    "ProgrammerS"
"He110W0r1d"	    5	    "He110"

입출력 예
입출력 예 #1

예제 1번의 my_string에서 앞의 11글자는 "ProgrammerS"이므로 이 문자열을 return 합니다.
입출력 예 #2

예제 2번의 my_string에서 앞의 5글자는 "He110"이므로 이 문자열을 return 합니다.

"""

#나의 답
def solution(my_string, n):
    answer = ''
    for i in range(0,n):
        answer += my_string[i]
    return answer

"""
2. 접두사인지 확인하기

문제 설명
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ my_string의 길이 ≤ 100
1 ≤ is_prefix의 길이 ≤ 100
my_string과 is_prefix는 영소문자로만 이루어져 있습니다.

입출력 예
my_string	is_prefix	result
"banana"	"ban"	    1
"banana"	"nan"	    0
"banana"	"abcd"	    0
"banana"	"bananan"	0

입출력 예 설명
입출력 예 #1

예제 1번에서 is_prefix가 my_string의 접두사이기 때문에 1을 return 합니다.
입출력 예 #2

예제 2번에서 is_prefix가 my_string의 접두사가 아니기 때문에 0을 return 합니다.
입출력 예 #3

예제 3번에서 is_prefix가 my_string의 접두사가 아니기 때문에 0을 return 합니다.
입출력 예 #4

예제 4번에서 is_prefix가 my_string의 접두사가 아니기 때문에 0을 return 합니다.

"""

def solution(my_string, is_prefix):
    #answer = [i for i in my_sti]
    a = ""
    print(my_string)
    print(is_prefix)
    for i in my_string:
        a += i
        print(a)
        if a == is_prefix:
            return 1
        #else:
    return 0

"""

3. 문자열 뒤집기

문제 설명
문자열 my_string과 정수 s, e가 매개변수로 주어질 때, my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.

제한사항
my_string은 숫자와 알파벳으로만 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000
0 ≤ s ≤ e < my_string의 길이

입출력 예
my_string	        s	e	result
"Progra21Sremm3"	6	12	"ProgrammerS123"
"Stanley1yelnatS"	4	10	"Stanley1yelnatS"

입출력 예 설명
입출력 예 #1

예제 1번의 my_string에서 인덱스 6부터 인덱스 12까지를 뒤집은 문자열은 "ProgrammerS123"이므로 "ProgrammerS123"를 return 합니다.
입출력 예 #2

예제 2번의 my_string에서 인덱스 4부터 인덱스 10까지를 뒤집으면 원래 문자열과 같은 "Stanley1yelnatS"이므로 "Stanley1yelnatS"를 return 합니다.

"""
def solution(my_string, s, e):
    answer = ''
    n = len(my_string)
    for i in range(0,s):
        answer += my_string[i]
    for j in range(e,s-1,-1):
        answer += my_string[j]
    for k in range(e+1,n):
        answer += my_string[k]
    return answer

"""
문제 설명
문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

제한사항
my_string은 영소문자로 이루어져 있습니다.
1 ≤ m ≤ my_string의 길이 ≤ 1,000
m은 my_string 길이의 약수로만 주어집니다.
1 ≤ c ≤ m

입출력 예
my_string	            m	c	result
"ihrhbakrfpndopljhygc"	4	2	"happy"
"programmers"	        1	1	"programmers"

입출력 예 설명

입출력 예 #1

예제 1번의 my_string을 한 줄에 4 글자씩 쓰면 다음의 표와 같습니다.
1열	2열	3열	4열
i	h	r	h
b	a	k	r
f	p	n	d
o	p	l	j
h	y	g	c

2열에 적힌 글자를 세로로 읽으면 happy이므로 "happy"를 return 합니다.
입출력 예 #2

예제 2번의 my_string은 m이 1이므로 세로로 "programmers"를 적는 것과 같고 따라서 1열에 적힌 글자를 세로로 읽으면 programmers입니다. 따라서 "programmers"를 return 합니다.
"""
def solution(my_string, m, c):
    answer = ''
    l = []
    
    for i in range(0,len(my_string),m):
        l.append(my_string[i:i+m])
    for j in l:
        answer += j[c-1]
    return answer

"""
문제 설명
두 정수 q, r과 문자열 code가 주어질 때, code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

제한사항
0 ≤ r < q ≤ 20
r < code의 길이 ≤ 1,000
code는 영소문자로만 이루어져 있습니다.

입출력 예
q	r	code	result
3	1	"qjnwezgrpirldywt"	"jerry"
1	0	"programmers"	"programmers"

입출력 예 설명

입출력 예 #1

예제 1번의 q와 r은 각각 3, 1이고 인덱스와 그 값을 q로 나눈 나머지가 잘 보이도록 표로 만들면 다음과 같습니다.
code	q	j	n	w	e	z	g	r	p	i	r	l	d	y	w	t
index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15
q로 나눈 나머지	0	1	2	0	1	2	0	1	2	0	1	2	0	1	2	0
`q`로 나눈 나머지가 1인 인덱스의 문자들을 앞에서부터 순서대로 이어 붙이면 "jerry"가 되므로 이를 return 합니다.

입출력 예 #2

예제 2번의 q와 r은 각각 1, 0이고 인덱스와 그 값을 q로 나눈 나머지가 잘 보이도록 표로 만들면 다음과 같습니다.
code	p	r	o	g	r	a	m	m	e	r	s
index	0	1	2	3	4	5	6	7	8	9	10
q로 나눈 나머지	0	0	0	0	0	0	0	0	0	0	0
`q`로 나눈 나머지가 1인 인덱스의 문자들을 앞에서부터 순서대로 이어 붙이면 "programmers"가 되므로 이를 return 합니다.

"""
def solution(q, r, code):
    answer = ''
    li = []
    for i in range(0,len(code),q):
        li.append(code[i:i+q])
    # print(li)
    for j in li:
        answer += j[r:r+1]
        
    return answer