def batting(runs,four,six,balls,field):
    sum=0
    sum=sum+(runs//2)+four*1+six*2+field*10
    if(runs>50):
        sum=sum+5
    if(runs>100):
        sum=sum+10
    strike_rate=(runs/balls)*100
    if(80<strike_rate<100):
        sum=sum+2
    elif(strike_rate>100):
        sum=sum+4
    return sum
def bowling(wckt,over,runs,field):
    sum=0
    sum=sum+(wckt*10)+(field*10)
    if(wckt>=3):
        sum=sum+5
    if(wckt>=5):
        sum=sum+10
    econmy_rate=runs//over
    if(3.5<econmy_rate<4.5):
        sum=sum+4
    elif(2<econmy_rate<3.5):
        sum=sum+7
    elif(econmy_rate<2):
        sum=sum+10
    return sum

#print(batting(112,10,0,119,0))
#print(bowling(3,10,34,0))
