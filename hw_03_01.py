
# Exercise 1:

places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']
# = [Argentina, San Diego, Boston, New York]

f = lambda x:x if x.strip() else None 
filtered_places = list(filter(f, places))
print(filtered_places)




# Exercise 2:

# .sort(key=)

authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

sorted_authors = sorted(authors, key=lambda n:n.split()[-1].lower())
print(sorted_authors)




# Exercise 3:

places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

# HINT: KEEP IN MIND PEMDAS. USE THE CELCIUS - FAHRENHEIT CONVERSION
# F = C * 9/5 + 32

f_places = list(map(lambda d:(d[0], d[1]*(9/5)+32), places))
print(f_places)




# Exercise 4:

def fibonacci(num):
    if num <= 2:
        return 1
    else:
         return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
