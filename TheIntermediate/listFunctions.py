
lucky_numbers = [42, 8, 15, 16, 23, 42, 55, 76, 1, -45, 0]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()           # makes a copy of the friends list

print(friends)

friends.extend(lucky_numbers)       # adds two lists together
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Grace")
print(friends)

friends.remove("Jim")
print(friends)

friends.append("Creed")
friends.append("Creed")
friends.append("Creed")
friends.remove("Creed")
print(friends)          # only gets rid of the first one it encounters

friends.pop()           # pops an element from the back of the list (basically treats it like a stack)
print(friends)

print(friends.index("Grace"))

print(friends.count("Creed"))

friends2.sort()
print(friends2)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)



