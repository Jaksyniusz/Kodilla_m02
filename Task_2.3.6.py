# ludzie listy piszą

# zadanie 1
name_list = ["Michael", "Terry", "Eric", "Graham"]
dictionary_name_list = dict()

for i in name_list:
    dictionary_name_list[i] = len(i)

print(str(dictionary_name_list))


# zadanie 2
number_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
first_number_list = []

for i in number_list:
    if ((i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0)):
        pass
    else:
        first_number_list.append(i)

print(first_number_list)


# zadanie 3
week_list = ['pon','śro','pią','sob']
week_list = week_list + ["wto", "czw", "nie"]
print(week_list)

# alternatywnie
week_list = ['pon','śro','pią','sob']
week_list.insert(1, "wto")
week_list.insert(3, "czw")
week_list.append("nie")
print(week_list)


# zadanie 4
akcje_herbata = ["2. włącz czajnik", "4. znajdź opakowanie herbaty", "6. zalej herbatę", "1. nalej wody do czajnika", "3. wyjmij kubek", "5. włóż herbatę do kubka"]
print(akcje_herbata)
akcje_herbata.sort()
print(akcje_herbata)