def permu(st,i,cur):
    if i==len(st):
        print(cur)
    permu(st,i+1,cur+st[i])
    permu(st,i+1,cur)
    i=0
    cur=st
permu(("abc"))
     