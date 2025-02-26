# filtrowanie w liście składanej
#[wyrażenie for element in lista if warunek]

philosoph_list = ['Arystoteles','Platon','Sokrates']
number_list = []

[number_list.append(len(philo)) for philo in philosoph_list]
print(number_list)