hrs=input('ENTER HOURS:')
rte=input('ENTER RATE:')
if int(rte)>20:
    pay=float(hrs)*float(rte)
else:
    print('error,please,enter,numeric,input')
