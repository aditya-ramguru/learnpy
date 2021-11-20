intvl = int(input("enter integer value "))
introman={1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C'}
b = intvl%10
a = intvl//10
if a>=1 and a<4:
    tens = introman[10]*a
elif a ==4:
    tens = introman[10]+introman[50]
elif a>=5 and a<9:
    tens = introman[50]+(introman[10]*(a-5))
else:
    tens = introman[10]+introman[100]
if b>=1 and b<4:
    ones = introman[1]*b
elif b==4:
    ones = introman[1]+introman[5]
elif b>=5 and b<9:
    ones = introman[5]+ (introman[1]*(b-5))
else:
    ones = introman[1]+introman[10]

print("roman numeral is ",tens+ones)