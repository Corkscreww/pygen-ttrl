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

'''№ 3 Функция inversions()'''

# def inversions(sequence):
#     count = 0
#     for i in range(len(sequence) - 1):
#         for j in range(i + 1, len(sequence)):
#             if sequence[i] > sequence[j]:
#                 count += 1
#     return count


# sequence = [4, 3, 2, 1]
# print(inversions(sequence))

'''№ 4 Покемоны'''

# with open('input.txt', encoding='utf-8') as input_file:
#     # pokemon = input_file.readline().strip()
#     pokemon = list(map(str.strip, list(input_file)))
#     pok_set = set(pokemon)
#     print(len(pokemon) - len(pok_set))

'''Блок 4.3 Методы экземпляра класса'''
'''№ 15 Класс Knight ♞'''

# class Knight:
#     def __init__(self, horizontal, vertical, color):
#         self.horizontal = horizontal
#         self.vertical = vertical
#         self.color = color

#     def char_trans(self, char):
#         char_t = {
#             'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6
#         }
#         return char_t[char.lower()]

#     def get_char(self):
#         return 'N'

#     def can_move(self, h, v):
#         h = self.char_trans(h)
#         v_dif = abs(v - self.vertical)
#         h_dif = abs(h -self.char_trans(self.horizontal))
#         if (v_dif == 1 and h_dif == 2) or (v_dif == 2 and h_dif == 1):
#             return True
#         else:
#             return False
#         abs()

#     def move_to(self, h, v):
#         if self.can_move(h, v):
#             self.horizontal = h
#             self.vertical = v

#     def draw_board(self):
#         for i in sorted(['a', 'b', 'c', 'd', 'e', 'f', 'g'], reverse=True):
#             for j in range(8):
#                 if self.horizontal == i and self.vertical == j:
#                     print(self.get_char(), end='')
#                 elif self.can_move(i, j):
#                     print('*', end='')
#                 else:
#                     print('.', end='')
#             print()

# knight = Knight('c', 3, 'white')
# print(knight.horizontal, knight.vertical)
# print(knight.can_move('e', 5))
# print(knight.can_move('e', 4))
# knight.move_to('e', 4)
# print(knight.horizontal, knight.vertical)

'''4.3'''
'''№ 2 Класс BankAccount'''


# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance

#     def get_balance(self):
#         return self._balance

#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise ValueError('На счете недостаточно средств')
#         self._balance -= amount

#     def transfer(self, account, amount):
#         self.withdraw(amount)
#         account.deposit(amount)

# account1 = BankAccount(100)
# account2 = BankAccount(200)
# try:
#     account1.transfer(account2, 150)
# except ValueError as e:
#     print(e)

'''№4.5.2 Класс HourClock'''


# class HourClock:
#     def __init__(self, hours) -> None:
#         self.hours = hours

#     def get_hours(self):
#         return self._hours

#     def set_hours(self, hours):
#         if isinstance(hours, int) and 0 < hours < 13:
#             self._hours = hours
#         else:
#             raise ValueError('Некорректное время')
#     hours = property(get_hours, set_hours)

# time = HourClock('Pizza time')
# try:
#     time.hours = 15
# except ValueError as e:
#     print(e)