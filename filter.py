# filter() = creates a collection of elements from an iterable for which a function returns true
# filter(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 40.00),
         ("socks", 5.00)]
# I want all the items with cost less than 27.00

lowPrices = lambda data: data[1] <= 27.00

low_priced_store = list(filter(lowPrices, store))

for i in low_priced_store:
    print(i)