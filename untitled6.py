import datetime 
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yy = str(now.year)
hr = str(now.hour)
mi = str(now.minute)
ss = str(now.second)  
print(mm + "/" + dd + "/" + yy + " "+ hr + ":" + mi + ":" + ss )
 