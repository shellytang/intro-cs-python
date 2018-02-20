# Write a program that calculates the minimum fixed monthly 
# payment needed in order pay off a credit card balance within 12 months.
# The monthly payment must be a multiple of $10 and is the same for all months.

def calculateFixedPayment(balance, annualInterestRate):
  origBalance = balance # save original value of the balance
  monthlyPayment = 10
  while balance > 0:
      for count in range(12):
          balance -= monthlyPayment
          interest = (annualInterestRate/12.0)*balance
          balance += interest
      if balance > 0:
          balance = origBalance
          monthlyPayment += 10     
  return 'Lowest Payment: ' + str(monthlyPayment)

print(calculateFixedPayment(3329, 0.2)) # 'Lowest Payment: 310'
print(calculateFixedPayment(3926, 0.2)) # 'Lowest Payment: 360'
print(calculateFixedPayment(375, 0.25)) # 'Lowest Payment: 40'