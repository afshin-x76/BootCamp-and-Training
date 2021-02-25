def fractional_knapsack(arr):
    weight = 10
    print(arr)
    best=[0,0]
    for i in arr:
        if best[0] < i[0]:
            best.append([i[0], i[1]])

    while True:
        count = 2
        if weight - best[count][1][1] > 0:
            weight -= best[count][1][1]
        elif weight > 0:
            print(best)
            print(best[count])
            print(best[count][1][1])
            print(weight)
            weight -= weight / best[count][1][1] * best[count][1][0]
        if weight <= 0:
            break
        count += 1

    print(weight)
    

def translate_knapsack_list(arr):
    final_list = []
    for i in arr:
        final_list.append([i[0] // i[1],[i[0],i[1]]])
    print(final_list)
    return fractional_knapsack(final_list)

arr = [[5,12], [2,1], [2,1], [2,1]]

print(translate_knapsack_list(arr))