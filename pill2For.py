for x in range(int(input())):
            m, n = map(int, input().split())
            g=[[0]*n for i in range(m)]
            for i in range(m):
                    for j,v in enumerate(list(input())):
                            g[i][j]=v

            r = [-1, 0, 0,  1,-1,-1,1,1]
            c = [0,  -1, 1,  0,-1,1,-1,1]
            d=0
            for i in range(m):
                for j in range(n):
                    f=0
                    if g[i][j]=='x':
                        for k in range(8):
                            x=i+r[k]
                            y=j+c[k]
                            if x>=0 and y>=0 and x<m and y<n:
                                if k<4:
                                    if g[x][y]=='b' or g[x][y]=='r':
                                        f=1
                                        #print(i,j,k)
                                else:
                                    if  g[x][y]=='r':
                                        f=1
                                        #print(i,j,k)
                        if f==0:
                            #print(i,j)
                            d+=1
            print(d)
