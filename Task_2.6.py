# zadanie 1
exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = []
top_students = []
best_student = ("",0)

[failed_students.append(i) for i, j in exam_points.items() if j < 46]
[top_students.append(i) for i, j in exam_points.items() if j > 90]

max_score = 0
max_name = ""
# [max_score = i for i in exam_points.values() if i > max_score]
for i, j in exam_points.items():
  if j > max_score:
    max_score = j
    max_name = i
  else:
    pass

best_student = (max_name, max_score)
print(best_student)


# zadanie 2
names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr', 'Jan', 'Denis', 'Amir',
'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub',
'Ludwik', 'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz', 'Łukasz', 'Bolesław', 'Amir',
'Artur', 'Albert', 'Olgierd', 'Alek', 'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']

name_dict = {}

names = sorted(set(names))

for name in names:
  name_dict.setdefault(name[0],name)
  name_dict[name[0]].append(name)
print(name_dict)

# zadanie 3
num = 30
fibonacci = []
for i in range(0,num):
  if len(fibonacci) < 2:
    fibonacci.append(1)
  else:
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
print(fibonacci)


# zadanie 4
a = 25
b = -30
c = 9

# def delta(a,b,c):
#  return b * b - 4 * a * c
#  print(delta)

# def equation(a,b,c):
#  x = delta(a,b,c)
#  if x == 0:
#    result1 = (-b - math.sqrt(x)) / (2 * a)
#    result2 = (-b + math.sqrt(x)) / (2 * a)
#    my_tuple = (result1, result2)
#    return my_tuple
#    print(my_tuple)
#   elif x > 0:
#     result = -b / (2 * a)
#     print("result")
#  else:
#    print("Brak rozwiązań")

# equation(a,b,c)

# rozwiązanie Kodilli
def equation(a,b,c):
  delta = b**2 - 4*a*c
  if delta < 0:
    return "Brak rozwiązań"
  elif delta == 0:
    x0 = -b / (2*a)
    return x0
  else:
    x1 = (-b - delta**(0.5)) / (2*a)
    x2 = (-b + delta**(0.5)) / (2*a)
    return x1,x2