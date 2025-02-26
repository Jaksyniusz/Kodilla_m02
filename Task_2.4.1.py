# iterator

vegetables = ["burak", "ziemniak", "szczypior", "cebula"]
vege_iterator = iter(vegetables)

for i in range (1, 6):
    print(next(vege_iterator))