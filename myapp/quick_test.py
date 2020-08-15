# def quick(list):
#     if len(list) < 2:
#         return list
#
#     tmp = list[0]  # 临时变量 可以取随机值
#     left = [x for x in list[1:] if x <= tmp]  # 左列表
#     right = [x for x in list[1:] if x > tmp]  # 右列表
#     return quick(left) + [tmp] + quick(right)
#
# li = [4,3,7,5,8,2]
# print(quick(li))   # [2, 3, 4, 5, 7, 8]

# def bubble_sort(li):
#     for i in range(len(li)-1):
#         for j in range(len(li)-i-1):
#             if li[j] > li[j+1]:
#                 li[j],li[j+1]=li[j+1],li[j]
#
# li = [1,5,2,4,3,6]
# bubble_sort(li)
# print(li)

def binary_search(alist,item):
    first = 0
    last = len(alist)-1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item > alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return None
if __name__ == '__main__':
    a_list = [9,8,7,6,5,4,3,2,1]
    print(binary_search(a_list,9))