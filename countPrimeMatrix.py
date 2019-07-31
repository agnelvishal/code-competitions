
def p(n):
    r=all(n % z for z in range(2, n))*(n > 1)
    if s==0:
        return r   
    else:
        return not r


def isSafe(c, d, visited):
    # row number is in range, column number
    # is in range and value is 1
    # and not yet visited
    return (c >= 0 and c < m and
            d >= 0 and d < n and
            not visited[c][d] and p(graph[c][d]))


def DFS(i, j, visited):

    # These arrays are used to get row and
    # column numbers of 8 neighbours
    # of a given cell
    rowNbr = [-1, 0, 0,  1]
    colNbr = [0,  -1, 1,  0]

    # Mark this cell as visited
    visited[i][j] = True
    #print(graph[i][j])
    # Recur for all connected neighbours
    for k in range(4):
        if isSafe(i + rowNbr[k], j + colNbr[k], visited):
            DFS(i + rowNbr[k], j + colNbr[k], visited)


def countIslands():
    # Make a bool array to mark visited cells.
    # Initially all cells are unvisited
    visited = [[False for f in range(n)]for e in range(m)]

    # Initialize count as 0 and travese
    # through the all cells of
    # given matrix
    count = 0
    for i in range(m):
        for j in range(n):
            # If a cell with value 1 is not visited yet,
            # then new island found
            if visited[i][j] == False and p(graph[i][j]):
                # Visit all cells in this island
                # and increment island count
                DFS(i, j, visited)
                count += 1
    return count


for x in range(int(input())):
    try: 
        m, n = map(int, input().split())
        graph=[[2] * n for _ in range(m)]
        for i in range(m):
                for j,v in enumerate(list(map(int, input().split()))):
                        graph[i][j]=v
        s=0
        print(countIslands(),end=' ')
        s=1
        print(countIslands())
    # except ArithmeticError:
    #     print(0,0)
    #     exit(3)
    # except AttributeError:
    #     exit(4)
    # except EOFError:
    #     exit(5)
    # except KeyError:
    #     exit(6)          
    # except TypeError:
    #     exit(7)
    # except ValueError:
    #     exit(8)
    except RuntimeError:
        exit(m)
    except IOError:
        exit(10)
    except Exception as e:
        print(e)
        exit(11)                         
exit(x)