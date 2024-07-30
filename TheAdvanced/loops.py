
# ----------------------------------WHILE LOOPS
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

while True:
    if i <= 0:
        break
    print(i)
    i -= 1

print("Done with -")



print("----------------------------------")



# ----------------------------------FOR LOOPS
for letter in "University of British Columbia":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

for i in range(20):                 # NOT INCLUSIVE OF 20
    print(i)

for i in range (3, 10):             # again not inclusive of ending value
    print(i)

for i in range(len(friends)):
    print(friends[i])


# -------------------------------------------------
def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num

    return result

print(raise_to_power(3, 4))
