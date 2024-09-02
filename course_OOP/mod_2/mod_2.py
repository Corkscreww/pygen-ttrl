'''№ 2'''

# with open('input.txt', encoding='utf-8') as input_file:
#     n = int(input_file.read().strip())

# rez = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         if ((i > j) and (i < n - 1 - j)):
#             row.append(j + 1)
#         if ((i <= j) and (i <= n - 1 - j)):
#             row.append(i + 1)
#         if ((i >= j) and (i >= n - 1 - j)):
#             row.append(n - i)
#         if ((i < j) and (i > n - 1 - j)):
#             row.append(n - j)
#     rez.append(row)

# for i in range(n):
#     print(*rez[i])
