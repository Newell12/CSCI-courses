# def mystery(nested_list):
#     prod = 1
#     for inner in nested_list:
#         for ele in inner:
#             prod *= ele
#     return prod
#
# def mystery2(nested_list):
#     prod = 1
#     for i in range(len(nested_list)):
#         for j in range(len(nested_list[i])):
#             prod*=nested_list[i][j]
#     return prod
import copy
var = [[[1], 2], [3, 4], 5, 6]
copy1 = copy.deepcopy(var)
copy2 = var[:]
copy3 = var
var[1][0] = 2
print(copy1, copy2)
print(copy2, copy3)
