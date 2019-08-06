
t=int(input())
a=[]
rem=0
for i in range(t):
    a.append(int(input()))
    
for i in range(t):
    rem=a[i]%12
    if rem==1:
        print(a[i]+11,"WS");
    elif rem==2:
        print(a[i]+9,"MS");
    elif rem==3:
        print(a[i]+7,"AS");
    elif rem==4:
        print(a[i]+5,"AS");
    elif rem==5:
        print(a[i]+3,"MS");
    elif rem==6:
        print(a[i]+1,"WS");
    elif rem==7:
        print(a[i]-1,"WS");
    elif rem==8:
        print(a[i]-3,"MS");
    elif rem==9:
        print(a[i]-5,"AS");
    elif rem==10:
        print(a[i]-7,"AS");
    elif rem==11:
        print(a[i]-9,"MS");
    elif rem==0:
        print(a[i]-11,"WS");
