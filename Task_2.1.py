variable_x = "x"
default_list = [None, "default", 1, [0, 0.5, variable_x]]

for i in default_list:
    print(i)

# wariacja
for i in default_list:
    print(str(i) + "1")