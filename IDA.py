import random
import copy

N = [5,10,11,12]
# N = [12]
inf = float('inf')

class State(): 
    '''
    状態を管理するクラス
    visited によって移動可能な経路の展開(expand)及びゴール判定が可能
    '''
    def __init__(self):
        self.visited = [False]*n
        self.num_visited = 0
        self.current_id = 0
        self.flg = False
        
    def update(self):  #状態を更新する関数
        self.visited[self.current_id] = True
        self.num_visited = sum(self.visited)

    def expand(self): # 移動可能な節点を展開する関数
        
        ex_node = []
        if sum(self.visited) == n-1:
            return [0]
        
        for i,v in enumerate(self.visited):
            if i != 0:    
                if v == False:
                    if i != self.current_id:
                        ex_node.append(i)
                
        return ex_node
    
    def isGoal(self): # 全てを訪れたらTrueを返す
        if (sum(self.visited)==n):
            return True
        
        return False
    
    def h(self,children):  # ヒューリスティック関数
        if not self.flg:
            return 0
        ans = inf
        for i in children:
            if ans > edge[self.current_id][i]:
                ans = edge[self.current_id][i]
        return ans
    

def DFS(node,path,limit):
    global num_ge    # 生成数をカウント
    num_ge += 1

    if path.isGoal():
        return True,0   
    
    new_limit = inf
    s = False
    children  = path.expand()
    global num_ex    # 展開数をカウント 
    num_ex += len(children)
    for child in children:        

        c = edge[node][child]
        b = c+path.h(children)


        if b <= limit:
            path.current_id = child
            new_path = copy.deepcopy(path)  
            new_path.update()  # 状態の更新
            (s,nb) = DFS(child,new_path,limit-c)
            b = nb+c

        new_limit = min(b,new_limit)

        if s:
            break
    return s,new_limit

def IDA(root,path):
    children = path.expand()
    limit = path.h(children)

    while(limit != inf):
        solved,limit = DFS(root,path,limit)
        
        if solved:
            return limit
        
    return 'NO_SOLUTION'

import time 
for n in N:
    edge = [[inf]*(n) for _ in range(n)]
    h0 = []
    h_num = [0,0]
    minout = []
    min_num = [0,0]
    for seed in range(1,6):
        random.seed(seed)
        for i in range(n):
            for j in range(i,n):
                cost = random.randint(1,100)
                if i==j:
                    continue
                edge[i][j] = cost
                edge[j][i] = cost

        print("==========")
        print("seed",seed)
        print("N",n)

        start = time.time()  
        num_ex = 0
        num_ge = 0
        path = State()   
        path.flg = False
        ans = IDA(0,path)
        end = time.time()-start
        print("cost",ans)
        print("time",end)
        h_num[0] += num_ex
        h_num[1] += num_ge        
        h0.append(end)

        start2 = time.time() 
        num_ex = 0
        num_ge = 0    
        path = State()
        path.flg = True
        ans2 = IDA(0,path)
        end2 = time.time()-start2
        minout.append(end2)    
        min_num[0] += num_ex
        min_num[1] += num_ge           

        print("cost_minout",ans2)
        print("time_minout",end2)

        if seed == 5:
            print('::::::::::')
            print("h0",sum(h0)/5)
            print("展開数",h_num[0]/5)
            print("生成数",h_num[1]/5)
            

            print("min",sum(minout)/5)
            print("展開数",min_num[0]/5)
            print("生成数",min_num[1]/5)

            

