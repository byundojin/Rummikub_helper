# user_case_1 = [15,43]
# ground_case_1 = [5,11,12,13,16,17,18,31,44,45,46,47]
# total_case_1 = user_case_1 + ground_case_1
# total_case_1.sort()
case_2 = [1,2,3,53,54,55]


def solve_rummickub(user_case:list, ground_case:list):
    duplication = range(52)
    total_case = user_case + ground_case
    total_case.sort()

def get_subset(case):
    case = []

# is_relate_cube_exist(list) -> boolean / 관련 큐브를 확인하여 있으면 true 없으면 false를 반환
def is_relate_cube_exist(case):
    print("한거 없음")

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
print(get_relate_same_number(case_2))
print(get_relate_same_color(case_2))