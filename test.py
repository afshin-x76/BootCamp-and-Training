def partition_problem(arr):
    total = sum(arr) // 2
    for i in list(range(1, len(arr) + 1)):
        for e in range(len(arr) - i):
            lst=[]
            tarlst = list(range(e, i+e))
            target = len(tarlst) - 1
            while True:
                for j in tarlst:
                    lst.append(arr[j])
                if sum(lst) == total:
                    return lst
                lst = []
                if len(tarlst) > 2:
                    if tarlst[-1] == len(arr) and tarlst[1] - tarlst[0] == 1 and target == 0:
                        break
                if tarlst[target] + 1 > len(arr):
                    target -= 1
                tarlst[target] += 1
    return False

array = [6, 5, 15, 16]
print(partition_problem(array))


