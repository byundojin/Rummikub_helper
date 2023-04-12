from itertools import combinations
import time
case_1 = list(range(1,53))
user_case_2 = [15,43]
ground_case_2 = [5,11,12,13,16,17,18,31,44,45,46,47]
case_2 = user_case_2 + ground_case_2
case_2.sort()

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

def split_cube(case):
    n_cu = get_relate_same_number(case)
    c_cu = get_relate_same_color(case)
    result = []
    for i in n_cu:
        if len(i) >= 3:
            yield i
        if len(i) == 4:
            for j in combinations(i, 3):
                yield (list(j))
    for i in c_cu:
        for j in i:
            b=[j]
            while True:
                if j == i[-1] or b[-1] == i[-1] or b[-1] + 1 != i[i.index(b[-1]) + 1]:
                    break
                b.append(i[i.index(b[-1]) + 1])
                if len(b) > 2:
                    yield b[:]

a = [i for i in split_cube(case_2)]
print("====================================")
for i in a:
    print(i)
print(len(a))

