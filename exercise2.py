"""
Question
-------
write a program to count the number of even and ood numbers
"""
num=[1,2,3,4,5,6,7,8,9]
even,ood=0,0
for i in  num:
    if i % 2 ==0:
        even +=1
    else:
        ood +=1
print('number of Even Number', even)
print('number of Odd Number', ood)











    # if i % 2 != 0:
    #     print(len(evenNum))

