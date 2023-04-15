case_1 = list(range(1,105))
card = []
r = []
result = []
for i in range(4):
    card.append([])
    for j in range(15):
        card[i].append(0)

def create_card(case):
    for i in case:
        card[i//13%4][i%13] += 1


def is_clear():
    result = True
    for i in card:
        for j in i:
            if j != 0:
                result = False
    return result

def dfs():
    color = -1
    num=0
    for i in range(4):
        if num != 0:
            break
        for j in range(15):
            if card[i][j] != 0:
                color = i
                num = j
                break
            
    if num == 0:
        if is_clear():
            result.append(r)
            print(len(result))
            return
    if num <= 11 and card[color][num + 1] != 0:
        t = []
        card[color][num] -= 1
        card[color][num + 1] -= 1
        t.append(color * 13 + num)
        t.append(color * 13 + num + 1)
        l = 2
        while card[color][num + l] and num + l <= 13:
            card[color][num + l] -= 1
            t.append(color * 13 + num + l)
            r.append(t)
            dfs()
            r.pop(-1)
            l += 1
        l -= 1
        while l > -1:
            card[color][num + l] += 1
            l -= 1
    c_avail = 0
    c_avail_list = []
    for i in range(6):
        c_avail_list.append(-1)
    for i in range(4):
        if card[i][num] != 0:
            c_avail_list[c_avail] = i
            c_avail += 1
    if c_avail == 3:
        t = []
        for i in range(3):
            card[c_avail_list[i]][num] -= 1
            t.append(c_avail_list[i] * 13 + num)
        r.append(t)
        dfs()
        r.pop(-1)
        for i in range(3):
            card[c_avail_list[i][num]] += 1
    if c_avail == 4:
        for i in range(4):
            if color == i:
                continue
            t = []
            for j in range(4):
                if i == j:
                    continue
                card[j][num] -= 1
                t.append(j*13+num)
            r.append(t)
            dfs()
            r.pop(-1)
            for j in range(4):
                if i == j:
                    continue
                card[j][num] += 1

create_card(case_1)
c = 1
for i in dfs():
    print(c)
    c += 1

