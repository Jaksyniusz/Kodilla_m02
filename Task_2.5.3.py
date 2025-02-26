# zadanie 1
my_list = []
[my_list.append(i * i) for i in range(1, 11)]
for i in my_list:
    if i % 2 == 0:
        pass
    else:
        print(i)


# zadanie 2
new_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
only_zero_list = []
not_only_zero_list = []
new_list.sort()

only_zero_list = new_list[0:10]
not_only_zero_list = new_list[10:]

print(only_zero_list)
print(not_only_zero_list)