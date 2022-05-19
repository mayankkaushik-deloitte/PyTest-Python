class DS:
    def __init__(self):
        pass
    def duplicates(self):
        n = int(input("Enter the size of the list of lists :: "))
        arr = [[] for i in range(n)]
        for i in range(n):
            dict = {}
            arr[i] = list(map(int, input("elements of array:-").strip().split()))
            for j in range(len(arr[i])):
                if arr[i][j] in dict:
                    dict[arr[i][j]] = dict[arr[i][j]] + 1
                else:
                    dict[arr[i][j]] = 1
            for key, val in dict.items():
                if val > 1 :
                    print(key, "-->", val)
    def mergeList(self):
        arr1 = list(map(int,input("elements of array:-").strip().split()))
        arr2 = list(map(int,input("elements of array:-").strip().split()))
        print(arr1 + arr2)
    def appendNested(self):
        list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
        list1[2][1][2].extend(["h", "i", "j"]);
        print(list1)
    def mapValues(self):
        Keys = ["Ten", "Twenty", "Thirty"]
        Values = [10,20,30]
        dict = {}
        for i in range(len(Keys)):
            dict[Keys[i]] = Values[i]
        print(dict)
    def mergeDicts(self):
        dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
        dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
        dict1.update(dict2)
        print(dict1)
    def renameDict(self):
        sampleDict = {

            "name": "Kelly",

            "age": 25,

            "salary": 8000,

            "city": "New york"
        }
        sampleDict["location"] = sampleDict.pop("city")
        print(sampleDict)
    def convertToList(self):
        dict = {"HuEx" : [1, 3, 4], "is": [7, 6], "best": [4, 5]}
        arr = []
        for key, val in dict.items():
            arr.append([key])
            for each in val:
                arr[len(arr) - 1].append(each)
        print(arr)

obj = DS()
obj.duplicates()
obj.mergeList()
obj.appendNested()
obj.mapValues()
obj.mergeDicts()
obj.renameDict()
obj.convertToList()