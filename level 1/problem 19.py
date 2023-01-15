days = ["monday", "Tuesday", "wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dayN=0
cnt=0
for i in range(1900,2001):
    if(i%4==0 and i%100!=0) or (i%100==0 and i%400==0):
        months[1]=29
    else:
        months[1]=28
    
    
    monthN=0 #매년마다 1월부터 다시 셈
    for month in months: #month는 달마다의 날짜
        monthN+=1 #1월부터 센다.

        for i in range(0, month):  #1일부터 그 달 말일까지
            if i+1==1 and days[dayN%7]=="Sunday":
                cnt+=1
            dayN+=1 #다음 요일

print(cnt)