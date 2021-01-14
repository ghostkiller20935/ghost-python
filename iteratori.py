cities = ["new york", "london", "moscow"]
cities_iterator = iter(cities)
print(next(cities_iterator))
print(next(cities_iterator))
print(next(cities_iterator))
 

while cities_iterator:
    try:
        print(next(cities_iterator))
    except StopIteration:
        break