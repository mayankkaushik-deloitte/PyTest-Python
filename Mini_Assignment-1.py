import string


class StringClass:
    s = ""

    def __init__(self):
        self.s = input()

    def length(self):
        return len(self.s)

    def convert(self):
        arr = []
        for char in self.s:
            arr.append(char)
        return arr


class PairsPossible(StringClass):
    arr = []
    s = "dasdasdasd"

    def __init__(self):
        self.s = input()
        pass

    def storeList(self):
        for i in range(len(self.s)):
            for j in range(i + 1, len(self.s)):
                self.arr.append(self.s[i] + self.s[j])

    def printList(self):
        print("The possible pairs are :: ")
        for i in range(len(self.arr)):
            print(self.arr[i] + " ", end='')
        print()


class SearchCommonElements:
    StringClassString = ""
    PairPossibleString = ""

    arr = []

    def __init__(self, a, b):
        self.StringClassString = a
        self.PairPossibleString = b

    def common(self):
        dict = {}
        for char in self.StringClassString:
            if char in dict:
                continue
            else:
                dict[char] = 1;
        for char in self.PairPossibleString:
            if char in dict:
                self.arr.append(char)
                dict.pop(char)

    def printList(self):
        print("The common elements are :: ")
        print(self.arr)


class UnEqualSumPairs(PairsPossible):
    arr = PairsPossible.arr
    def __init__(self):
        pass
    def countPairs(self):
        # print(self.arr)
        count = 0
        dict = {}
        for i in range(len(self.arr)):
            sum = int(self.arr[i][0]) + int(self.arr[i][1])
            # print(sum)
            if str(sum) in dict:
                dict[str(sum)] = dict[str(sum)] + 1
            else:
                dict[str(sum)] = 1
        for key, val in dict.items():
            if val == 1:
                count = count + 1
        return count


StringObj = StringClass()
print("The length of the string is :: ")
print(StringObj.length())
print("The string after conversion looks like this :: ")
print(StringObj.convert())
pairs = PairsPossible()
pairs.storeList()
pairs.printList()
third = SearchCommonElements(StringObj.s, pairs.s)
third.common()
third.printList()
fourth = UnEqualSumPairs()
print("The pairs are : " + str(fourth.countPairs()))