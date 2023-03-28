from itertools import combinations

def _arr_split(arr):
    resurt = []
    index = 0
    for i in range(len(arr)):
        if arr[index][0] != arr[i][0]:
            yield resurt
            resurt = []
            index = i
        resurt.append(arr[i])
    yield (resurt)

def result_analysis(case):
    relate_case = _relate_cube_arr(case)
    arr = [i for i in _arr_split(relate_case)]
    comp_arr = [] #comparative_arr 비교 배열
    for i in range(len(case)):
        prel_arr = [] #preliminary_arr 예비 배열
        if i == 0:
            for j in arr[0]:
                if j == case:
                    yield j
                else:
                    prel_arr.append([j])
        else:
            count = 0
            for j in range(len(comp_arr)):
                is_join = False
                if case[i] in _sumf(comp_arr[j - count]):
                    continue
                else:
                    for k in range(len(arr[i])):
                        b = []
                        if _is_not_arr_duplication(arr[i][k], comp_arr[j - count]):
                            b = comp_arr[j - count] + [arr[i][k]]
                            if _is_arr_same(b, case):
                                yield b
                                continue
                            is_join = True
                        else:
                            continue
                        prel_arr.append(b)
                    if is_join:
                        comp_arr.remove(comp_arr[j - count])
                        count += 1
        comp_arr += prel_arr

def _is_arr_same(arr, case):
    result = False
    re = _sumf(arr)
    if set(re) == set(case):
        result = True
    return result

def _is_not_arr_duplication(arr, case):
    result = True
    re = _sumf(case)
    if set(arr) & set(re):
        result = False
    return result

def _sumf(arr):
    re = []
    for i in arr:
        re += i
    return re

def _relate_cube_arr(case):
    results = []
    arr = _relate_cube_arr_column(case) + _relate_cube_arr_line(case)
    for i in arr:
        for j in range(0, len(i)):
            for k in combinations(i, j + 1):
                c = list(k)
                if not c in results:
                    if len(c) == 1 or (sum(c) == len(c) * (len(c) - 1 + 2 * c[0]) / 2) or (c[0] % 13 == c[1] % 13):
                        results.append(c)
    results.sort()
    return results

def _relate_cube_arr_line(case):
    results = [[],[],[],[]]
    for i in case:
        results[(i - 1) // 13].append(i)
    while [] in results:
        results.remove([])
    return results

def _relate_cube_arr_column(case):
    results = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in case:
        results[(i - 1) % 13].append(i)
    while [] in results:
        results.remove([])
    return results