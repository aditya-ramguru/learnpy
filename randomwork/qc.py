fname=input('Enter file name:')
count=0
total=0
try:
    fhand=open(fname)
except:
    if fname=="aditya":
        print("You have been punk'd!")
        quit()
    else:
        print('requestd file',fname,'not found')

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        x=line.rstrip()
        y=x[19:]
        z=float(y)
        total=total+z
        count=count+1


print('Average spam confidence:',total/count)
