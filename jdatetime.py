import jdatetime 
now = jdatetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yy = str(now.year)
hr = str(now.hour)
mi = str(now.minute)
ss = str(now.second)  
now = yy + "/" + mm + "/" + dd + " "+ hr + ":" + mi + ":" + ss
   
 