user_case_1 = [15,43]
ground_case_1 = [5,11,12,13,16,17,18,31,44,45,46,47]
total_case_1 = user_case_1 + ground_case_1
total_case_1.sort()
# case_2 = [1,2,3,53,54,55,105]


def solve_rummickub(user_case:list, ground_case:list = []):
    duplication = []
    joker = is_joker(user_case) + is_joker(ground_case)
    is_duplication(user_case, duplication)
    is_duplication(ground_case, duplication)
    total_case = user_case + ground_case
    total_case.sort()
    print(is_relate_cube_exist(total_case, joker))
    print(f"joker : {joker}")
    print(f"user_case : {user_case}")
    print(f"ground_case : {ground_case}")
    print(f"total_case : {total_case}")
    print(f"duplication : {duplication}")



# is_duplication(list) -> void / 중복인지 확인하여 중복을 제거하고 dupl에 중복을 넣는다
def is_duplication(_case, dupl):
    prel = []
    for i in _case:
        if i > 52:
            if (i - 52) in _case:
                prel.append(i)
    for i in prel:
        _case.remove(i)
        dupl.append(i)

# is_joker(list) -> int / case를 확인하고 조커수를 반환한다.
def is_joker(_case):
    count = 0
    if 105 in _case:
        _case.remove(105)
        count += 1
    if 106 in _case:
        _case.remove(106)
        count += 1
    return count

def get_subset(case):
    case = []

# is_relate_cube_exist(list) -> boolean / 관련 큐브를 확인하여 있으면 true 없으면 false를 반환
def is_relate_cube_exist(case, joker):
    row = get_relate_same_color(case)
    colum = get_relate_same_number(case)
    if joker == 2:
        return True
    print(row)
    b = []
    for i in row:
        r = []
        a = [i.pop(0)]
        while True:
            if len(i) == 0:
                break
            elif i[0] - 1 == a[-1]:
                a.append(i.pop(0))
            else:
                r.append(a)
                a = [i.pop(0)]
        r.append(a)
        print("r",r)
        if joker == 1:
            c = [r.pop(0)]
            while True:
                if len(r) == 0:
                    c[-1] += [0]
                    break
                elif r[0][0] - 2 == c[-1][-1]:
                    c[-1] = c[-1] + [0] + r.pop(0)
                else:
                    c.append(r.pop(0))
            r = c
        for i in r:
            if len(i) < 3:
                b.append(i)
    if b == []:
        return True
    a = []
    for i in b:
        a += i
    while True:
        if 0 in a:
            a.remove(0)
        else:    
            break
    for i in a:
        i = i % 13
    list(set(a))
    print("a :", a)
    print(colum)
    for i in colum:
        print(i)
        if i[0] % 13 in a:
            if len(i) + joker < 3:
                return False
    return True





            
                        
                

            
            

                

            


    

# get_relate_same_number(list) -> list / 같은 수 끼리 정리한 list를 반환
def get_relate_same_number(case):
    results = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in case:
        results[(i - 1) % 13].append(i)
    while [] in results:
        results.remove([])
    return results

# get_relate_same_color(list) -> list / 같은 색 끼리 정리한 list를 반환
def get_relate_same_color(case):
    results = [[],[],[],[]]
    for i in case:
        results[((i - 1) // 13) % 4].append(i)
    while [] in results:
        results.remove([])
    return results

# print(total_case_1)
# print(get_relate_same_number(total_case_1))
# print(get_relate_same_color(total_case_1))
print(solve_rummickub(total_case_1))

