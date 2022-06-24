#greedy algoritm

def max_weight():
    arr.sort(reverse = True)
    for i in range(n):
        arr[i] = arr[i] * (i + 1)
    return max(arr)

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(max_weight())