# Write a program to calculate the credit card balance after one year if a person only pays the minimum 
# monthly payment required by the credit card company each month.

def calculateBalance(balance, annualInterestRate, monthlyPaymentRate):
  month = 0
  while(month < 12): 
      minimumPayment = monthlyPaymentRate * balance
      balance -= minimumPayment
      interest = (annualInterestRate/12.0)*balance
      balance += interest
      month += 1
  if month == 12:
      return 'Remaining balance: ' + str(round(balance,2))

print(calculateBalance(42, 0.2, 0.04)) # Remaining balance: 31.38
print(calculateBalance(484, 0.2, 0.04)) # Remaining balance: 361.61
