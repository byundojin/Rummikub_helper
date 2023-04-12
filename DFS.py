from itertools import combinations
case_1 = [5,15,16,17,18,31,43,44,45,46,47]
# case_1 = list(range(1,105))
class cube():
    cubes = {}
    case = []
    joker = 0
    player_cube = []
    shape_cube = []
    def __init__(self, num) -> None:
        self.num = num
        if num % 13 == 0:
            self.n = 13
        else:
            self.n = num % 13
        self.c = num // 13 % 4
        cube.cubes[num] = self
        self.relate_c = None
        self.relate_n = []
        self.comb_c = []
        self.comb_n = []
        self.amount = 0
        if num > 52:
            cube.cubes[num-52].amount +=1
        pass

    def __repr__(self) -> str:
        # return f"{self.num}:{self.c}:{self.n}"
        return f"{self.num}"

    def relate_cubes():
        for i in cube.case:
            if i > 52:
                if i - 52 + 1 in cube.case and i % 13 != 0:
                    cube.cubes[i].relate_c = cube.cubes[i - 52 +1]
            elif i + 1 in cube.case and i % 13 != 0:
                cube.cubes[i].relate_c = cube.cubes[i+1]
        for i in cube.case:
            for j in cube.case:
                if i != j and j % 13 == i % 13 and i % 52 != j % 52:
                    cube.cubes[i].relate_n.append(cube.cubes[j])

    def combination_cubes(self):
        if len(self.relate_n) > 0:
            a = [self]
            for i in self.relate_n:
                if i.num < 53:
                    a.append(i)
            if len(a) >= 3:
                self.comb_n.append(a)
            if len(a) == 4:
                for i in combinations(a,3):
                    self.comb_n.append(list(i))
        b = [self]
        while True:
            if b[-1].relate_c == None:
                break
            b.append(b[-1].relate_c)
            if len(b) >= 3:
                self.comb_c.append(b[:])

    def create_cube(player_cube, shape_cube = []):
        case = player_cube + shape_cube
        case.sort()
        cube.player_cube = player_cube
        cube.shape_cube = shape_cube
        if 105 in case:
            cube.joker += 1
            case.remove(105)
            if 106 in case:
                cube.joker += 1
                case.remove(106)
        cube.case = case_1
        for i in case:
            cube(i)
        cube.relate_cubes()
        for i in cube.cubes:
            cube.cubes[i].combination_cubes()
        cube.view_cubes()
    
    def view_cube(self):
        print(self,":", self.relate_c,"|",self.relate_n)
        print("comb_n : ", self.comb_n)
        print("comb_c : ", self.comb_c)

    def view_cubes():
        for i in cube.cubes:
            cube.view_cube(cube.cubes[i])


cube.create_cube(case_1)