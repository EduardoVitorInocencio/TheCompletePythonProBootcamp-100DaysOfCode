print('\nEdu \'\ s house burguer: Welcome to the tip calculator!')

#If the bill was $150.00, split between 5 people, with 12% tip. 
totalBill = input('What was the total bill?')
totalBill = float(totalBill[1 : len(totalBill)])

percentualTip = int(input('How much tip would you like to give? 10, 12 or 15?'))/100
totalTip = totalBill * percentualTip
totalBillPlusTip = totalBill + totalTip
 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
qtdePeople = int(input('How many people to split the bill?'))

#Format the result to 2 decimal places = 33.60
splitedTotal = round(totalBillPlusTip/qtdePeople,2)

print('\n********** Total Bill **********')

print(f'Total Bill:                      ${totalBill}\n\n')
print(f'Number of people:                 {qtdePeople}\n\n')
print(f'Choosed tip:                     ${percentualTip * 100}%\n\n')
print(f'Total adding the tip:            ${totalBillPlusTip}\n\n')
print(f'Total splited per {qtdePeople}:  ${splitedTotal}\n\n')