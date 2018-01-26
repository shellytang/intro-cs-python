# calculate a more accurate fixed monthly rate and use bisection search
def calculateFixedPayment(balance, annualInterestRate):
  monthlyInterestRate = annualInterestRate / 12
  lowerBound = balance / 12
  upperBound = (balance * (1 + annualInterestRate)**12) / 12.0
  originalBalance = balance
  epsilon = 0.01 # number by which to determine how close to be to an answer

  while abs(balance) > epsilon:
    balance = originalBalance
    payment = (lowerBound + upperBound)/2.0
    for month in range(12):
      balance -= payment
      balance *= 1 + monthlyInterestRate
    if balance > 0:
      lowerBound = payment
    else:
      upperBound = payment
  return "Lowest Payment: " + str(round(payment, 2))

print(calculateFixedPayment(320000, 0.2)) # 29157.09
print(calculateFixedPayment(999999,0.18)) # 90325.03