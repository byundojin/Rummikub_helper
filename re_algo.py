user_case_1 = [15,43]
ground_case_1 = [5,11,12,13,16,17,18,31,44,45,46,47]
total_case_1 = user_case_1 + ground_case_1
total_case_1.sort()
def get_subset(case):
    case = []


# get_relate_same_number() / 같은 수 끼리 정리
def get_relate_same_number(case):
    results = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in case:
        results[(i - 1) % 13].append(i)
    while [] in results:
        results.remove([])
    return results

# get_relate_same_color() / 같은 색 끼리 정리
def get_relate_same_color(case):
    results = [[],[],[],[]]
    for i in case:
        results[(i - 1) // 13].append(i)
    while [] in results:
        results.remove([])
    return results

print(total_case_1)
print(get_relate_same_number(total_case_1))
print(get_relate_same_color(total_case_1))