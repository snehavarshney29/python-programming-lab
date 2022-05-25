salary=0
bs=int(input("enter the salary"))
if(bs<10000):
    salary = bs+(bs*0.75)+(bs*0.70)
    print(salary)
elif(bs>10000 and bs<20000):
    salary = bs+(bs*0.80)+(bs*0.80)
    print(salary)
elif(bs>20000):
    salary = bs+(bs*0.90)+(bs*0.95)
    print(salary)
