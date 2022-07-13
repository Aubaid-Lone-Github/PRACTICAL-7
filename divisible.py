T=[(4,8,12),(40,44,48),(6,7,90)]
res=()
k=4
res = [sub for sub in T if all(ele % k == 0 for ele in sub)]
print("Numbers divisible by k are :",res)            
