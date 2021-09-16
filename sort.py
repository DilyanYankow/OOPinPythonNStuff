# sort() method = used with lists
# sort() function = used with iterables

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Crabs"]
# sorted_students = sorted(students, reverse=True)      #list = func(tuple)
# students.sort(reverse=True)
#
# for i in students:
#     print(i)


students = [("Squidward", "F", 50),
            ("Sandy", "A", 33),
            ("Patrick", "D", 20),
            ("Spongebob", "F", 10),
            ("Mr. Crabs", "B", 22)]

# students.sort()     #by first collumn

grade = lambda grades:grades[1]

age = lambda ages:ages[2]
students.sort(key=age)

for i in students:
    print(i)

print("_____________tuple sort now")
studentstuple = (("Squidward", "F", 50),
            ("Sandy", "A", 33),
            ("Patrick", "D", 20),
            ("Spongebob", "F", 10),
            ("Mr. Crabs", "B", 22))

age = lambda stuage:stuage[2]
sorted_tuplestudents = sorted(students, key=age)

for i in students:
    print(i)