import random
import math

class Node :

    def __init__(self, x:int, y:int, name:str):
        self.pos : list = [x,y]
        self.title : str = name

    def __repr__(self):
        return str(self.title)

    def getDist(self, node : object) -> float:

        sqr = (node.pos[0] - self.pos[0])**2 + (node.pos[1] - self.pos[1])**2 
        d = math.sqrt(sqr) 

        return d


def shuffle(arr : list) -> list:
    
    newArr : list = [None for _ in range(len(arr))]

    for i in range(len(arr)):
        while(True):
            x : int = random.randint(0,5)
            if(newArr[x] == None):
                newArr[x] = arr[i]
                break
    
    return newArr


def setup() -> list:

    v1 : Node = Node(0,0,"v1")
    v2 : Node = Node(1,1,"v2")
    v3 : Node = Node(2,1,"v3")
    v4 : Node = Node(3,0,"v4")
    v5 : Node = Node(2,-1,"v5")
    v6 : Node = Node(1,-1,"v6")

    return [v1,v2,v3,v4,v5,v6]


def SimAnn() -> None:
    
    lis = setup()

    print("\n")

    lis = shuffle(lis)

    temp = int(input("Temperature (Default = 3) : "))
    coolingFac = int(input("CoolingFactor (Default = 1) : "))
    print("\n", "Running Test", "\n")

    print("Starting Values : ", lis , "\n")

    for _ in range(3):

        x1 : int = random.randint(0,5)
        x2 : int = 0

        while(True):
            x2 = random.randint(0,5)
            if(x2 != x1): break

        fo = 0
        for i in range(len(lis)-1): fo += lis[i].getDist(lis[i+1])

        lisNew = lis.copy()
        lisNew[x1], lisNew[x2] = lisNew[x2], lisNew[x1]

        fn = 0
        for i in range(len(lisNew)-1): fn += lisNew[i].getDist(lisNew[i+1])

        if fn < fo : 
            lis = lisNew.copy()
            print("Swapped ", lis[x2], "<->", lis[x1], " [better result]")
        else:

            p = math.e**(-((fo - fn) / 3 * temp))  #Is this right? =  //df Max = 3 bcs dist (v1,v4) is max -> sqrt(3**2)
            x = random.random()

            if(x < p): 
                lis = lisNew.copy()
                print("Swapped ", lis[x2], "<->", lis[x1], " [random swap]")
            else :
                print("Swapped nothing") 
                pass

        print("Iteration : ", _ + 1, " -> ", lis)
        print("\n")
        temp -= 1 * coolingFac


def threshHold() -> None:

    lis = setup()

    print("\n")

    lis = shuffle(lis)

    theta = int(input("Threshhold (Default = 1) : "))
    print("\n", "Running Test", "\n")

    print("Starting Values : ", lis , "\n")

    for _ in range(3):

        x1 : int = random.randint(0,5)
        x2 : int = 0

        while(True):
            x2 = random.randint(0,5)
            if(x2 != x1): break

        fo = 0
        for i in range(len(lis)-1): fo += lis[i].getDist(lis[i+1])

        lisNew = lis.copy()
        lisNew[x1], lisNew[x2] = lisNew[x2], lisNew[x1]

        fn = 0
        for i in range(len(lisNew)-1): fn += lisNew[i].getDist(lisNew[i+1])

        if fn < fo - theta: 
            lis = lisNew.copy()
            print("Swapped ", lis[x2], "<->", lis[x1], " [better result]")
        else:
            print("Swapped nothing") 

        print("Iteration : ", _ + 1, " -> ", lis)
        print("\n")


if __name__ == "__main__":
    threshHold()