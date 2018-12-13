import csv
f=open("data.csv","r")
D={'rollno1':11,'name1':"anurag",'gender1':"male",'age1':78,'rollno2':12
   'name2':"disha",'gender2':"female",'age2':67,'rollno3':13,
   'name':"gurvinder",'gender':"male",'age':72}
D[mark1]=63
D[mark2]=59
D[mark3]=67
if 'rollno1' in D:
    print(D('name1'))
    print(D('gender1'))
    print(D('mark1'))
elif 'rollno2' in D:
    print(D('name2'))
    print(D('gender2'))
    print(D('mark2))
elif 'rollno3' in D:
    print(D('name3'))
    print(D('gender3'))
    print(D('mark3'))
else:
    print("invalid")
f.close()
