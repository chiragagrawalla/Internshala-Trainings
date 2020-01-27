import function
"""p1=dict()
p2=dict()
p3=dict()
p4=dict()
p5=dict()"""
p1={ 'name' : 'Virat Kohli' , 'role' : 'bat' , 'runs' :112, '4' :10, '6' :0,
'balls' :119, 'field' :0}
p2={ 'name' : 'du Plessis' , 'role' : 'bat' , 'runs' :120, '4' :11, '6' :2,
'balls' :112, 'field' :0}
p3={ 'name' : 'Bhuvneshwar Kumar' , 'role' : 'bowl' , 'wkts' :1, 'overs' :10,
'runs' :71, 'field' :1}
p4={ 'name' : 'Yuzvendra Chahal' , 'role' : 'bowl' , 'wkts' :2, 'overs' :10,
'runs' :45, 'field' :0}
p5={ 'name' : 'Kuldeep Yadav' , 'role' : 'bowl' , 'wkts' :3, 'overs' :10, 'runs' :34,
'field' :0}
player=[p1,p2,p3,p4,p5]
"""for i in player:
    i["name"]=input("enter name")
    i["role"]=input("enter role")
    if(i["role"]=="bat"):
        i["runs"]=int(input("enter runs"))
        i["4"]=int(input("enter number of 4"))
        i["6"]=int(input("enter number of 6"))
        i["balls"]=int(input("enter balls"))
        i["field"]=int(input("enter fields"))
    else:
        i["wckt"]=int(input("enter number of wickets"))
        i["overs"]=int(input("enter ovrs"))
        i["runs"]=int(input("enter runs"))
        i["field"]=int(input("enter field"))"""
batscore=0
bowlscore=0
for i in player:
    if(i["role"]=="bat"):
        batscore=function.batting(i["runs"],i["4"],i["6"],i["balls"],i["field"])
        del i["role"]
        del i["4"]
        del i["6"]
        del i["balls"]
        del i["field"]
        i["batscore"]=batscore
        print(i)
    else:
        bowlscore=function.bowling(i["wkts"],i["overs"],i["runs"],i["field"])
        del i["role"]
        del i["wkts"]
        del i["overs"]
        del i["runs"]
        del i["field"]
        i["bowlscore"]=bowlscore
        print(i)
