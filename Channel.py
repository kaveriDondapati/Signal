s=input("aaa");
count=0;
l=list(s);
for i in l:
    if(l[i]==l[i]):
        break;
        count=1;
        
        
    elif(l[i]!=l[i+1]):
        count+=1;
       
    else:
        count=0;
        
print(count)