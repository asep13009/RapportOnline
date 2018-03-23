#coba
def prime(bilangan):
    count1=0
    for i in range (1,bilangan):
        if (bilangan%i==0):
            count1 +=1
    if (count1==2):
        return "prime"
    else:
        return "not prime"

tes=prime(2)

print(tes)
#cobain