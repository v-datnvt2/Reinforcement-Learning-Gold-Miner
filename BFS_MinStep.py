import numpy as np
from queue import Queue 
inf = 10000000000000000
class BFS_energy:
    def __init__(self,cnt = 0
                ,MAP_MAX_X = 21
                ,MAP_MAX_Y = 9
                ,damlay = -5
                ,step = 100
                ,next_time = {0:-5,-5:-20,-20:-40,-40:-100,-100:-100}
                ,time_inLay = [-5,-20,-40,-100,-100]
                ,pre_pos = []
                ,start_x = 0
                ,start_y = 0
                ,player_pos = []
                ,num = []):
        self.cnt = cnt # dem so lan buoc vo dam lay
        self.MAP_MAX_X = MAP_MAX_X
        self.MAP_MAX_Y = MAP_MAX_Y
        self.next_time = next_time
        self.step = step # so luot choi con lai
        self.damlay = damlay
        # self.stack = []
        self.x = start_x
        self.y = start_y
        self.pre_pos = pre_pos
        self.num = num
        self.time_inLay = time_inLay
        self.player_pos = player_pos
    #/*
    #   next_time : so nang luong tinh theo lan buoc vao dam lay
    #   all_lay : tat cac coordinate cua dam lay 
    #   num_step : luu lai so buoc di den tung vi tri (matrix 21*9)
    #   all_gold : tat ca coordinate cua mo vang
    #   value : nang luong tieu hao de den duoc tung vi tri (matrix 21*9)
    # */

    # def normal_BFS(self,matrix,all_gold,all_lay):
    #     q = Queue()
    #     q.push

    def BFS(self,matrix,value,num_step,visited,trace,all_gold,all_lay ,posx,posy,energy,count):
        q=Queue()
        q.put((posx,posy))
        visited[posx][posy] = 1
        current = self.damlay
        count = 0
        val_lay = {}
        for x,y in all_lay:
            val_lay[(x,y)] = matrix[x][y]

        while not q.empty():
            row, col = q.get()
            
            # if (row,col) in all_lay:
            #     count+=1
            # if count != 0:
            #     for i in range(len(all_lay)):
            #         r = all_lay[i][0]
            #         l = all_lay[i][1]
            #         if visited[r][l] == 0:
            #             matrix[r][l] = self.next_time[current]
            #     current = self.next_time[current]
            # if current >= 40:
            #     for p in all_lay:
            #         visited[p[0]][p[1]] = 1
            #         value[p[0]][p[1]] =inf
            #         step[p[0]][p[1]] = -inf

            if col+1 < self.MAP_MAX_Y and row >=0:
                if visited[row][col+1] == 0 :
                    q.put((row, col+1))
                    trace[row][col+1] = trace[row][col] + "3"
                    visited[row][col+1] = 1
                    num_step[row][col+1] = num_step[row][col] +1
                    if matrix[row][col+1] >0:
                        value[row][col+1] = value[+row][col] + 4
                    else:
                        if (row,col+1) in all_lay:
                            if val_lay[(row,col+1)] < -40:
                                t1,t2 =q.get()
                                visited[row][col+1] = 1
                                value[row][col+1] = inf
                                num_step[row][col+1] = -inf
                            else:
                                value[row][col+1] = value[row][col] -(self.num[row,col+1]+1)* val_lay[(row,col+1)]
                            # val_lay[(row,col+1)] = self.next_time[val_lay[(row,col+1)]]
                        else:
                            value[row][col+1] = value[row][col] - matrix[row][col+1]
                else:
                    tmp = value[row][col+1]
                    
                    # visited[row][col+1] =
                    
                    if matrix[row][col+1] >0:
                        tmp = value[row][col] + 4
                    else:
                        if (row,col+1) in all_lay:
                            tmp = value[row][col] - (self.num[row,col+1]+1)*val_lay[(row,col+1)]
                        else:
                            tmp = value[row][col] - matrix[row][col+1]
                    
                    if tmp < value[row][col+1] :
                        value[row][col+1] = tmp
                        num_step[row][col+1] = num_step[row][col] +1
                        trace[row][col+1] = trace[row][col] + "3"
                    



            if row+1 < self.MAP_MAX_X and col >=0:
                
                if visited[row+1][col] == 0 :
                    q.put((row+1, col))
                    trace[row+1][col] = trace[row][col] + "1"
                    visited[row+1][col] = 1
                    num_step[row+1][col] = num_step[row][col] +1
                    if matrix[row+1][col] >0:
                        value[row+1][col] = value[row][col] + 4
                    else:
                        if (row+1,col) in all_lay:
                            if val_lay[(row+1,col)] < -40:
                                t1,t2 =q.get()
                                visited[row+1][col] = 1
                                value[row+1][col] = inf
                                num_step[row+1][col] = -inf
                            else:
                                value[row+1][col] = value[row][col] -(self.num[row+1,col]+1)* val_lay[(row+1,col)]
                        else :
                            value[row+1][col] = value[row][col] - matrix[row+1][col]

                    # print(value[row+1][col], matrix[row+1][col], row, col)
                else:
                    tmp = value[row+1][col]
                    # visited[row][col+1] =
                    
                    if matrix[row+1][col] >0:
                        tmp = value[row][col] + 4
                    else:
                        if (row+1,col) in all_lay:
                            tmp  = value[row][col] -(self.num[row+1,col]+1)* val_lay[(row+1,col)]
                        else :
                            tmp= value[row][col] - matrix[row+1][col]
                    if tmp < value[row+1][col] :
                        value[row+1][col] = tmp
                        num_step[row+1][col] = num_step[row][col] +1
                        trace[row+1][col] = trace[row][col] + "1"
                    


            if 0 <= col-1 and row < self.MAP_MAX_X :
                if visited[row][col-1] == 0 :
                    q.put((row, col-1))
                    trace[row][col-1] = trace[row][col] + "2"
                    visited[row][col-1] = 1
                    num_step[row][col-1] = num_step[row][col] + 1
                    if matrix[row][col-1] >0:
                        value[row][col-1] = value[row][col] +4
                
                    else:
                        if (row,col-1) in all_lay:
                            if val_lay[(row,col-1)] <  -40:
                                t1,t2 = q.get()
                                visited[row][col-1] = 1
                                value[row][col-1] = inf
                                num_step[row][col-1] = -inf
                            else:
                                value[row][col-1] = value[row][col] - (self.num[row,col-1+1])*val_lay[(row,col-1)]
                        else:
                            value[row][col-1] = value[row][col] - matrix[row][col-1]
                else :
                    tmp = value[row][col-1]
                    
                    # visited[row][col+1] =
                    
                    if matrix[row][col-1] >0:
                        tmp = value[row][col] + 4
                    else:
                        if (row,col-1) in all_lay:
                            tmp = value[row][col] - (self.num[row,col-1]+1)*val_lay[(row,col-1)]
                        else:
                            tmp = value[row][col] - matrix[row][col-1]
                    if tmp < value[row][col-1] :
                        value[row][col-1] = tmp
                        num_step[row][col-1] = num_step[row][col] +1
                        trace[row][col-1] = trace[row][col] + "2"
                    


            if 0 <= row-1 and col < self.MAP_MAX_Y :
                if visited[row-1][col] == 0 :
                    q.put((row-1, col))
                    trace[row-1][col] = trace[row][col] + "0"
                    visited[row-1][col] = 1
                    num_step[row-1][col] = num_step[row][col] +1
                    if matrix[row-1][col] >0:
                        value[row-1][col] = value[row][col] + 4
                    else:
                        if (row-1,col) in all_lay:
                            
                            if val_lay[(row-1,col)] <-40:
                                r1,r2 = q.get()
                                visited[row-1][col] = 1
                                value[row-1][col] = inf
                                num_step[row-1][col] = -inf
                            else:
                                value[row-1][col] = value[row][col] - (self.num[row-1,col]+1)*val_lay[(row-1,col)]
                            # value[row-1][col] = value[row][col] - 10*matrix[row-1][col]
                        else :
                            value[row-1][col] = value[row][col] - matrix[row-1][col]
                
                else :
                    tmp = value[row-1][col]
                    
                    # visited[row][col+1] =
                    
                    if matrix[row-1][col] >0:
                        tmp = value[row][col] + 4
                    else:
                        if (row-1,col) in all_lay:
                            tmp = value[row][col] - (self.num[row-1,col]+1)*val_lay[(row-1,col)]
                        else:
                            tmp = value[row][col] - matrix[row-1][col]
                    if tmp < value[row-1][col] :
                        value[row-1][col] = tmp
                        num_step[row-1][col] = num_step[row][col] +1
                        trace[row-1][col] = trace[row][col] + "0"

        return num_step, value, trace, all_gold  


    def act(self,s):
            # Lay map, pos ,energy tu state
            d = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
            maps = np.array(s[...,0:self.MAP_MAX_X*self.MAP_MAX_Y]).reshape(self.MAP_MAX_X,self.MAP_MAX_Y)
            pos = np.array(s[...,self.MAP_MAX_X*self.MAP_MAX_Y : self.MAP_MAX_X*self.MAP_MAX_Y+2])
            energy = s[...,self.MAP_MAX_X*self.MAP_MAX_Y+2:self.MAP_MAX_X*self.MAP_MAX_Y+3]
            bot1 = s[...,self.MAP_MAX_X*self.MAP_MAX_Y+3:self.MAP_MAX_X*self.MAP_MAX_Y+5]
            bot2 = s[...,self.MAP_MAX_X*self.MAP_MAX_Y+5:self.MAP_MAX_X*self.MAP_MAX_Y+7]
            bot3 = s[...,self.MAP_MAX_X*self.MAP_MAX_Y+7:self.MAP_MAX_X*self.MAP_MAX_Y+9]
            bot = []
            bot.append(bot1)
            bot.append(bot2)
            bot.append(bot3)
            energy = energy[0]
            count = 0
            
            x,y = pos
            # if (x,y) in all_lay
            #khoi tao acton
            
            action = '4'
            def reset():
                num_step = np.zeros(shape = (self.MAP_MAX_X,self.MAP_MAX_Y))
                value = np.zeros(shape = (self.MAP_MAX_X,self.MAP_MAX_Y),dtype=int)
                visited = np.zeros(shape = (self.MAP_MAX_X,self.MAP_MAX_Y))
                all_gold = []
                all_lay = []
                trace = [["" for x in range(self.MAP_MAX_Y)] for y in range(self.MAP_MAX_X)]
                return num_step , value , visited , all_gold , all_lay ,trace
            
            def get_dir(matrix , s , x,y):
                if s == '2' and y-1 >=0: # turn up
                    return np.array([x,y-1])
                if s == '3' and  y+1<self.MAP_MAX_Y: # turn down
                    return np.array([x,y+1])
                if s == '0' and x-1 >=0: # turn left
                    return np.array([x-1,y])
                if s == '1' and x+1 < self.MAP_MAX_X: # turn right
                    return np.array([x+1,y])
                return np.array([x,y])

            
            num_step, value, visited, all_gold, all_lay,tr =  reset()
            next_time = self.next_time
            # Set lai map 

            for i in range(self.MAP_MAX_X):
                for j in range(self.MAP_MAX_Y):
                    if(maps[i][j] == 0): # gap dat
                        maps[i][j] = -1
                    elif(maps[i][j] == -1) : #gap rung
                        maps[i][j] = -15
                    elif maps[i][j] == -2: #gap bay
                        maps[i][j] = -3
                    elif maps[i][j] == -3: # gap dam lay
                        # maps[i][j] = self.damlay
                        # if  + 50 <= 0:
                        maps[i][j] = -5
                            # visited[i][j] = 1
                        all_lay.append((i,j))
                    else :
                        # if visited[i][j] == 0:
                            all_gold.append((i,j))
            pre_num =  np.copy(self.num)
            if(x,y) in all_lay and (self.player_pos[0],self.player_pos[0]) != (x,y) :
                self.num[x][y] +=1
                maps[x][y] = self.time_inLay[min(self.num[x][y],4)]
            for i in range(3):
                idx = bot[i][0]
                idy = bot[i][1]
                if (idx,idy) in all_lay  and (self.pre_pos[i][0],self.pre_pos[i][1])!=(idx,idy):
                    if (self.num[idx][idy] - pre_num[idx][idy])==0:
                        self.num[idx][idy]+=1
                    maps[idx][idy] = self.time_inLay[min(self.num[idx][idy],4)]
            for i in range(self.MAP_MAX_X):
                for j in range(self.MAP_MAX_Y):
                    if(i,j) in all_lay:
                        maps[i][j] = self.time_inLay[min(self.num[i][j],4)]
                        if maps[i][j] < -40:
                            visited[i][j] = 1
                            value[i][j] = inf
                            num_step[i][j] = -inf

            self.x = x
            self.y = y
            for i in range(3):
                idx = bot[i][0]
                idy = bot[i][1]
                self.pre_pos[i][0] = idx
                self.pre_pos[i][1] = idy

            nstep, value, trace , coord_gold= self.BFS(maps,num_step,value,visited,tr,all_gold,all_lay,x,y,energy,count)
            idx = x
            idy = y
            Min = inf
            for (x,y) in all_gold:
                if nstep[x][y] < Min:
                    Min = nstep[x][y]
                    idx = x
                    idy = y
                

            pos_gold = [idx,idy]    
            return pos_gold,Min