string= input("plese enter your own word")
char= input("plese enter your own charechter")
i=0
count= 0
while(i<len(string))# string opration
if(string[i]== char): # condition1
    count= count+1
    i= i+1
    print("total number of time," char,"has Occuered=", count)
    
