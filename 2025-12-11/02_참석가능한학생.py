

def solution(rank, attendance):
    available = [(rank[i],i) for i in range(len(rank)) if attendance[i]]
    
    available.sort()
    a,b,c = [student_id for _, student_id in available[:3]]
    return 10000*a + b*100 + c 

rank = [3, 7, 2, 5, 4, 6, 1]
attendance = [False, True, True, True, True, False, False]

print(solution(rank, attendance))