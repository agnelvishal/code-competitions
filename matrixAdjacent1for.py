for x in range(int(input())):
    m, n = map(int, input().split())
    g = [0 for i in range(m*n)]
    j = 0
    for i in range(m):
        for v in list(input()):
            g[j] = v
            j += 1
    l = [-n, n, 1,  -1, -n-1, n-1, n+1, -n+1]
    c = 0
    for s in range(m*n):
        f = 0
        i = s//n
        if g[s] == "x":
            # print(i,j)
            for k in range(8):
                j = s+l[k]
                h=j//n
                if j >= 0 and j < n*m:
                    if ((g[j] == 'b'or g[j] == 'r') and (k < 2 or (h == i and k < 4)) )or (3 < k < 8 and (h == i+1 or h == i-1) and g[j] == 'r'):
                        f = 1
            if f == 0:
                # print(s,i)
                c += 1
        # if g[s]=="x":
        #     if s-n>=0:
        #         if g[s-n]=="b":
        #             f=1
        #     if s-1>=0 and s%n!=0:
        #         if g[s-1]=="b":
        #             f=1
        #     if s+n<n*m:
        #         if g[s+n]=="b":
        #             f=1
        #     if s+1<n*m and s%n-1!=0:
        #         if g[s+1]=="b":
        #             f=1

        # if f==0:
        #     print(s)
        #     c+=1
    print(c)
