
def p(n):
    print(n)
    if n==0:
        return 0
    r=all(n % z for z in range(2,int(n**(.5)+1)))
    return r if s==0 else not r
def r():
    c=0
    for i in range(m):
        for j in range(n):
            if p(g[i+j]):
                c+=1
                k(i+j)
    return c
def k(e):
    z=[e]
    while(z):
        q=z.pop()
        g[q]=0
        col=q%n
        row=q//m
        # print(row,col,q)
        # print(z)
        #print(q-n)
        if row>0 and p(g[q-n]):
            z+=[q-n]
            # print(z)
        if col<n-1 and p(g[q+1]):
            z+=[q+1]
        if row<m-1 and p(g[q+n]):
            z+=[q+n]
            
        if col>0 and p(g[q-1]):
            z+=[q-1]

for x in range(int(input())):
            m, n = map(int, input().split())
            g=[0 for i in range(m+n+1)]
            for i in range(m):
                    for j,v in enumerate(list(map(int, input().split()))):
                            g[n*i+j]=v
            s=0
            print(r(),end=' ')
            s=1
            print(r())

                 
