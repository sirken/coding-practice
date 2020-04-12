from Test import Test, Test as test

'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
'''

def tickets(people):

    bank = []

    def rem_bank(note, num):
        for x in range(num):
            bank.remove(note)

    for amt in people:
        if amt == 50:
            if 25 in bank:
                rem_bank(25, 1)
                bank.append(amt)
            else:
                return 'NO'
        elif amt == 100:
            if 25 in bank and 50 in bank:
                rem_bank(25, 1)
                rem_bank(50, 1)
                bank.append(amt)
            elif bank.count(25) >= 3:
                rem_bank(25, 3)
                bank.append(amt)
            else:
                return 'NO'
        elif amt == 25:
            bank.append(amt)

    return 'YES'

# Top solution, a little hard to read but not bad
def tickets(people):
  till = {100.0:0, 50.0:0, 25.0:0}

  for paid in people:
    # Add their bill to the till
    till[paid] += 1
    # Determine change
    # 25-25=0, 50-25=25, 100-25=75
    change = paid-25.0

    # Check 50s first, then 25s. Biggest to smallest
    for bill in (50,25):
      # If the bill type is <= to the change needed, and there's a bill available, give them one
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    # If change is remaining (it's above 0), then we don't have the bills to give
    if change != 0:
      return 'NO'

  return 'YES'

# Other interesting solution, seems awkward but easily readable
def tickets(a):
    n25 = n50 = n100 = 0
    for e in a:
        if e==25: n25+=1
        elif e==50: n25-=1; n50+=1
        elif e==100 and n50>0: n25-=1; n50-=1
        elif e==100 and n50==0: n25-=3
        if n25<0 or n50<0:
            return 'NO'
    return 'YES'


test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")
test.assert_equals(tickets([25, 25, 50, 50, 100]), "NO")
test.assert_equals(tickets([50, 100, 100]), "NO")
test.assert_equals(tickets([100, 25, 100]), "NO")
test.assert_equals(tickets([25, 50, 50, 100]), "NO")
test.assert_equals(tickets([25, 50, 25, 25, 50, 25, 25, 25, 100, 25, 25, 25, 25, 25, 50, 100]), "YES")
test.assert_equals(tickets([25, 25, 50]), "YES")
