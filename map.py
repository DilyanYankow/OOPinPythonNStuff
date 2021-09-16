# map() = applies a function to each item in an iterable (list, tuple, ect.)
#
# map(function, iterable)


store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 40.00),
         ("socks", 5.00)]

to_euros = lambda data: (data[0], data[1]*0.84)
to_dollars = lambda data: (data[0], data[1]/0.84)

store_to_euros = map(to_euros, store)
store_to_dollars = map(to_dollars, store)

for i in store_to_euros:
    print(i)

print("----------")

for i in store_to_dollars:
    print(i)