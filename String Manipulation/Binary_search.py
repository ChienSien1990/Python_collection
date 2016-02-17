# Paste your code into this box
totalBal = balance
monthIntPay= (annualInterestRate) / 12.0
minFixMonthPay = 0
lowerBound = balance/12
upperBound = (balance*((1+monthIntPay)**12))/12
UpdatedBal = balance
while abs(UpdatedBal)>0.5:
    minFixMonthPay = (lowerBound+upperBound)/2
    UpdatedBal = balance
    for x in range(1,13):
        monthUnpaidBal = (UpdatedBal)-minFixMonthPay
        UpdatedBal = (monthUnpaidBal) *(1 + monthIntPay) 
    if UpdatedBal<upperBound:
        if UpdatedBal>0:
            lowerBound = minFixMonthPay
        else:
            upperBound = minFixMonthPay
    else:
        if UpdatedBal>0:
            upperBound = minFixMonthPay
        else:
            lowerBound = minFixMonthPay
minFixMonthPay=round(minFixMonthPay, 2)


print "Lowest Payment: ", minFixMonthPay