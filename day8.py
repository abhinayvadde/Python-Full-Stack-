# Max sum of 3 no. in a list
'''
if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum = max_sum_so_far = arr[0]
    for i in range(1, len(arr)):
        max_sum_so_far = max(arr[i], max_sum_so_far + arr[i])
        max_sum = max(max_sum, max_sum_so_far)
    print("Maximum sum of contiguous subarray is:", max_sum)


# # To find the maximum product of a contiguous subarray in a list.
if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    max_product = max_product_so_far = arr[0]
    for i in range(1, len(arr)):
        max_product_so_far = max(arr[i], max_product_so_far * arr[i])
        max_product = max(max_product, max_product_so_far)
    print("Maximum sum of contiguous subarray is:", max_product)


# To arrange the 0 to last of the list
li = [1,3,0,4,2,0,8,9,0]
a = 0
for i in li:
    if i != 0:
        li[a] = i
        a += 1
for i in range(a, len(li)):
    li[i] = 0
print(li)




li = [1,3,0,4,2,0,8,9,0]
j= 0
for i in range(len(li)):
    if li[i] != 0:
        li[j],li[i] = li[i],li[j]
        j += 1
print(li)
'''


if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum = max_sum_so_far = arr[0]
    for i in range(1, len(arr)):
        max_sum_so_far = max(arr[i], max_sum_so_far + arr[i])
        max_sum = max(max_sum, max_sum_so_far)
    print("Maximum sum of contiguous subarray is:", max_sum)




li = [-2,1,4,-3,-1,2,4]
j = 0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        li = max(li[i],j+li[i])
        j = max(j,li)
    print(j)
        

