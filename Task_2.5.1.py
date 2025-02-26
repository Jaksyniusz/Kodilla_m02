# lista składana
#[wyrażenie for element in lista]

numbers = [1, 3, 5, 11, 20]
squares = []
for number in numbers:
    squares.append(number * number)
print(f"Na wstępie mieliśmy taką listę {numbers}")
print(f"A oto jej kwadraty {squares}")

squares = [number * number for number in numbers]
print(f"Te kwadraty {squares} uzyskano dzięki list comprehension")