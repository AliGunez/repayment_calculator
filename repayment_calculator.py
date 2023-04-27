'''
repayment calculator, this software takes in how much you and your friends spent on
a group activity individually and calculates who has to pay who back in the least amount
of transactions so that everyone ends up paying an equal amount for the activity
'''


# creating the list for the people involved and how much they spent
people = []
spent = []
total = 0

# defining a function for receiving the information and storing it accordingly in the lists
def people_spent():
    payee = input("Who paid?: ")
    transaction = float(input("How much was spent?: £"))

    if payee.lower() in people:
        x = people.index(payee.lower())
        spent[x] += transaction
    else:
        people.append(payee.lower())
        spent.append(transaction)


# creating a loop that asks for user input on whether or not they want to add more
# transactions or not
new_purchase = input("Would you like to add a new purchase 'yes' or 'no': ")

while new_purchase.lower() != "no":
    people_spent()
    new_purchase = input("Would you like to add a new purchase 'yes' or 'no': ")

print("-" * 40)
print(people)
print(spent)

# calculating the total spent
for number in spent:
    total += number
# calculate the average
average = total / len(people)

print("-" * 40)
print(f"Total spent = £{total}")
print(f"{total} divided by {len(people)} people = £{average}")

# sort the lists so that they are from the highest amount to the lowest and corresponding correctly
spent, people = zip(*sorted(zip(spent, people), reverse=True))
spent = list(spent)  # convert back to list to allow modifications

# calculate who needs to pay who back
balances = {}
for i in range(len(people)):
    if spent[i] < average:
        for j in range(len(people)):
            if spent[j] > average:
                amount = min(average - spent[i], spent[j] - average)
                if people[i] not in balances:
                    balances[people[i]] = {}
                if people[j] not in balances[people[i]]:
                    balances[people[i]][people[j]] = 0
                balances[people[i]][people[j]] += amount
                spent[i] += amount
                spent[j] -= amount


print("_" * 40)
# print out the balances
for p1 in balances:
    for p2 in balances[p1]:
        print(f"{p1} needs to pay {p2} £{balances[p1][p2]:.2f}")
print("_" * 40)