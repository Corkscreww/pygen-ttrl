'''№ 1 Дартс'''

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

'''№ 2 Скобочная последовательность'''

# with open('input.txt', encoding='utf-8') as input_file:
#     inp_str = input_file.read().strip()

# while inp_str.find(')') != -1:
#     close_parent = inp_str.find(')')
#     inp_str = inp_str[:close_parent] + inp_str[close_parent + 1:]
#     if (open_parent := inp_str[:close_parent].rfind('(')) != -1:
#         inp_str = inp_str[:open_parent] + inp_str[open_parent + 1:]


# if inp_str:
#     print(False)
# else:
#     print(True)