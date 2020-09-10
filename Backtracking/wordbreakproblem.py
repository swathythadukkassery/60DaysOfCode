def isValid(dict1,str,result):
    for i in range(len(str)):
        
        if(str[0:i+1] in dict1):

            
            if i==len(str)-1:
                
                result+=str
                print(result)
                return
            
            isValid(dict1,str[i+1:],result+str[0:i+1]+" ")
        
    return      
    

dict1=list(input().split())
word=input()

result=""
isValid(dict1,word,result)

