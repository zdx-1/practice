def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 遍历轮数
        for j in range(n-i-1):
            # 从开头遍历数组，进行比较交换
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input())

nums = list(map(int,input().split()))

bubble_sort(nums)

for num in nums:
    print(num,end=" ")
print()