#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by http://blog.csdn.net/marty_fu/article/details/7679297

origin = [0, 0] # 坐标系统原点 
legal_x = [0, 50] # x轴方向的合法坐标 
legal_y = [0, 50] # y轴方向的合法坐标 

def create(pos): 
    def player(direction,step): 
        # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等 
        # 然后还要对新生成的x，y坐标的合法性进行判断处理 
        new_x = pos[0] + direction[0]*step 
        new_y = pos[1] + direction[1]*step 
        pos[0] = new_x 
        pos[1] = new_y 
        #注意！此处不能写成 pos = [new_x, new_y]，原因在上文有说过 
        return pos 
    return player 
  
player1 = create(origin[:]) # 创建棋子player1，起点为原点 
print player1([1,0],10) # 向x轴正方向移动10步 
print player1([0,1],20) # 向y轴正方向移动20步 
print player1([-1,0],10) # 向x轴负方向移动10步

print "origin is",origin

player2 = create(origin[:]) # 创建棋子player2，起点为原点 
print player2([-1,0],10) # 
print player2([1,1],20) # 
print player2([1,0],10) # 