import json

import sys

import time

from matplotlib import pyplot as plt

import numpy as np

sys.setrecursionlimit(10 ** 7)  # 设置最大递归深度
# 但是仅仅设置递归深度不够，需要栈空间配合
# threading线程模块可以设定线程的栈空间
import threading

threading.stack_size(2 ** 16)  # 把线程的栈空间提上去

class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
    def setPrev(self, newprev):
        self.prev = newprev

class Queue():
    def __init__(self):
        self.head=None
        self.rear=None
        self.length=0
    def size(self):
        return self.length
    def isEmpty(self):
        return self.head==None
    def enqueue(self,item):
        #空集加元素时加在头部
        if self.head==None:
            self.head=Node(item)
        #两个元素时，创建尾巴，避免enqueue时要从头遍历一遍
        elif self.rear==None:
            self.rear=Node(item)
            self.head.setNext(self.rear)
            self.rear.setPrev(self.head)
        else:#接尾巴
            temp=Node(item)
            temp.setPrev(self.rear)
            self.rear.setNext(temp)
            self.rear=temp
        self.length=self.length+1
    def dequeue(self):
        if self.length==0:
            return None
        else:
            head=self.head.getData()
            if self.length==1:
                self.head=None 
            elif self.length==2:
                self.head=self.rear
                self.head.setPrev(None)
                self.rear=None
            else:
                self.head=self.head.getNext()
                self.head.setPrev(None)
            self.length=self.length-1
            return head 
    def __str__(self):
        cNode=self.head
        result=[]
        while cNode!=None:
            result.append(cNode.data)
            cNode=cNode.next
        return str(result)


class Vertex():
    def __init__(self,actor_name):
        self.name=actor_name
        self.connectTo={}#self.connectTo={vertex:{film_name}}
        self.searched=0#0为没搜索，1为正在探索，2为探索完毕
        self.dis=0#相对某个点的距离，没计算前就是相对自己=0
        self.attend=set()#filmname,演员参演过的电影
    def add_nbr(self,actor_vertex,film_name):
        if actor_vertex not in self.connectTo.keys():
            self.connectTo[actor_vertex]={film_name}
        else:
            self.connectTo[actor_vertex].add(film_name)
    
class Graph():
    def __init__(self):
        self.actors={}#self.actors={actor_name:vertex}
        self.films={}#self.films={film_name:film}
        self.scale=0
        self.diameter=0
        self.types={}#self.types={type:[film_name]}注意这里是value是list,为了方便排名
        self.avr=0.0
    def add_connection(self,name_list,film):
        #创建节点
        film_name=film['title']
        #if film_name in self.films.keys():
        #    print(film_name)
        self.films[film_name]=film
        for name in name_list:
            if name not in self.actors.keys():
                self.actors[name]=Vertex(name)
                self.scale+=1
        N=len(name_list)
        if N>1:
            for i in range(N-1):
                for j in range(i+1,N):
                    self.actors[name_list[i]].add_nbr(self.actors[name_list[j]],film_name)
                    self.actors[name_list[j]].add_nbr(self.actors[name_list[i]],film_name)
                    self.actors[name_list[i]].attend.add(film_name)
                    self.actors[name_list[j]].attend.add(film_name)
        else:
            self.actors[name_list[0]].attend.add(film_name)
    def clear_searched(self):
        for vertex in self.actors.values():
            vertex.searched=0
            vertex.dis=0
    def cal_dia(self):
        N=len(self.actors)
        actorlist=list(self.actors.keys())
        for i in range(N):
            v1=self.actors[actorlist[i]]
            self.diameter=max(self.diameter,cal_dis(v1))
            if N>100:
                print("proccessing:",((i+1)/N)*100)
            self.clear_searched()
        return self.diameter
    def cal_avr(self):
        self.avr=sum([film["star"] for film in self.films.values()])/len(self.films)
        return self.avr
    


def make_Graph(film_list):
    g=Graph()
    for film in film_list:
        actor_list=film['actor'].split(',')
        g.add_connection(actor_list,film)
    return g

def get_child_graph(pgraph):
    actors_set=set(pgraph.actors.keys())#获得演员集合
    vertQueue=Queue()#存演员名字的队列
    result_list=[]#存子图
    while len(actors_set)>0:
        if vertQueue.length==0:
            result_list.append(Graph())
            actor_name=actors_set.pop()
            vertQueue.enqueue(actor_name)
        cur_vert=pgraph.actors[vertQueue.dequeue()]#当前探索节点
        #print(repr(cur_vert.name),vertQueue.length)
        result_list[-1].actors[cur_vert.name]=pgraph.actors[cur_vert.name]#添加演员节点
        result_list[-1].scale+=1
        actors_set.discard(cur_vert.name)
        cur_vert.searched=2
        for vert,film_set in cur_vert.connectTo.items():
            if vert.searched==1 or vert.searched==2:
                pass
            else:
                vert.searched=1
                vertQueue.enqueue(vert.name)#添加待探索节点
        for film in cur_vert.attend:
            result_list[-1].films[film]=pgraph.films[film]
    return result_list
                

def cal_dis(v1):
    vertQueue=Queue()
    vertQueue.enqueue(v1)
    result=0
    while vertQueue.length>0:
        cur=vertQueue.dequeue()
        cur.searched=2
        for vert in cur.connectTo.keys():
            if vert.searched==0:
                vert.searched=1
                vert.dis=cur.dis+1
                result=max(result,vert.dis)
                vertQueue.enqueue(vert)
    return result
        
def film_typen(agraph,typeset):
    for typp in typeset:
        agraph.types[typp]=[]#初始化
    for film in agraph.films.values():#往各个类里丢电影
        for typp in film["type"].split(','):
            agraph.types[typp].append(film["title"])
    for typp in typeset:#排序
        agraph.types[typp].sort(key=lambda x:-agraph.films[x]["star"])


def draw(glist):
    #x,y都是list
    #第一张截断图,前20名
    plt.figure()
    plt.title("Scale Picture(ln)")
    plt.xlabel("According to scale,1-20 are first 20 graphs,21-40 are last 20 graphs")
    plt.ylabel("Scale(ln)")
    plt.ylim(0,5)
    plt.grid(axis="y",linestyle='--')
    plt.yticks([0.2*i for i in range(26)])
    x=np.array(list(range(1,41)))
    y1=np.array([np.log10(g.scale) for g in glist[0:20]]+[np.log10(g.scale) for g in glist[4557:4577]])
    plt.bar(x,y1)
    
    #直径
    plt.figure(2)
    plt.title("Diameter Picture")
    plt.xlabel("According to scale,1-20 are first 20 graphs,21-40 are last 20 graphs")
    plt.ylabel("Diameter")
    plt.ylim(0,7)
    plt.grid(axis="y",linestyle='--')
    y2=np.array([g.diameter for g in glist[0:20]]+[g.diameter for g in glist[4557:4577]])
    plt.bar(x,y2)
    
    #星级
    plt.figure(3)
    plt.title("Star Picture")
    plt.xlabel("According to scale,1-20 are first 20 graphs,21-40 are last 20 graphs")
    plt.ylabel("Star")
    plt.yticks(range(0,11,1))
    plt.grid(axis="y",linestyle='--')
    y3=np.array([float(format(g.avr,'.2f')) for g in glist[0:20]]+[float(format(g.avr,'.2f')) for g in glist[4557:4577]])
    plt.bar(x,y3)
    plt.show()
    

def Get(alist):#去重
    count_dict={}
    for i in range(len(alist)):
        if alist[i]["title"] not in count_dict.keys():
            count_dict[alist[i]["title"]]=0#出现第一次的时候赋0
        else:
            count_dict[alist[i]["title"]]+=1#再次出现则+1
            alist[i]["title"]=alist[i]["title"]+' （同名版本 '+str(count_dict[alist[i]["title"]])+'）'
    return alist


'''
1.所有演员分为几个连通分支？+
  每个连通分支有多少演员？+
  每个连通分支电影所属类别的前三名？（按tag出现次数排序，同次数就按tag本身排序)
  （按照连通分支规模从大到小排序，列表前20行，和最后20行，中间省略，下同）
2.每个连通分支的直径（任意节点间最短路径的最大值）多少？（合并到上题列出，最大的连通分支节点过多，不需要计算直径，设为-1）+
3.用matplotlib画出连通分支的规模、直径、电影平均星级（小数点后2位）的柱状图；+
4.周星驰所出演的电影平均星级如何？+
5.周星驰和他的共同出演者，有多少人？+
  他们各自一共出演了多少部电影？+
  所出演的电影平均星级如何？+
  电影所属类别的前三名？（按tag出现次数排序，同次数就按tag本身排序)
6.你还能用课程所学的图算法得出什么有意思的发现？+
'''

def myprog():
    f=open('C:\\Users\\z8203\\Desktop\\课程\\数据结构与算法\\Film.json','r',encoding='UTF-8')
    Film_list=Get(eval(f.read()))
    print(len(Film_list))
    f.close()
    op=open('C:\\Users\\z8203\\Desktop\\课程\\数据结构与算法\\result.txt','w',encoding='UTF-8')
    op.truncate()
    type_set=set()
    for film in Film_list:
        type_set=type_set|set(film['type'].split(','))
    op.write("总的电影类型集合：%s\n"%str(type_set))
    #print("总的电影类型集合：",type_set)
    Total_Graph=make_Graph(Film_list)
    op.write("电影平均星级：%.2f\n"%Total_Graph.cal_avr())
    #print("电影平均星级：%.2f"%Total_Graph.cal_avr())
    op.write("图的大小：%d\n"%Total_Graph.scale)
    #print("图的大小：",Total_Graph.scale)
    op.write("电影总数：%d\n"%len(Total_Graph.films))
    result=get_child_graph(Total_Graph)
    op.write("连通分支数目：%d\n"%len(result))
    #print("连通分支数目：",len(result))
    result.sort(key=lambda x:(-x.scale,list(x.films.keys())[0]))
    for g in result:
        if g.scale>100:
            g.diameter=-1
        else:
            g.cal_dia()
        g.cal_avr()
    #op.write("%s\n"%str([format(x.avr,'.2f') for x in result]))
    #print([format(x.avr,'.2f') for x in result])
    op.write("规模（演员数）从大到小排位，前20名：%s\n"%str([x.scale for x in result][0:20:1]))
    #print("规模（演员数）从大到小排位，前20名：",[x.scale for x in result][0:20:1])
    op.write("连通分支直径（按规模从大到小排位），前20名：%s\n"%str([x.diameter for x in result][0:20:1]))
    #print("连通分支直径（按规模从大到小排位），前20名：",[x.diameter for x in result][0:20:1])
    op.write("规模（演员数）从大到小排位，后20名:%s\n"%str([x.scale for x in result][-1:-21:-1]))
    #print("规模（演员数）从大到小排位，后20名：",[x.scale for x in result][-1:-21:-1])
    op.write("连通分支直径（按规模从大到小排位），后20名：%s\n"%str([x.diameter for x in result][-1:-21:-1]))
    #print("连通分支直径（按规模从大到小排位），后20名：",[x.diameter for x in result][-1:-21:-1])
    #各类别电影前三名，不存在的类别不列出，按星级排名
    count=0
    '''
    for g in result:#电影分类
        film_typen(g,type_set)
        count+=1
        if (count in range(1,21)) or (count in range(4558,4578)):
            op.write("Graph %d\n"%count)
            #print("Graph %d"%count)
            for typp in type_set:
                if len(g.types[typp])>0:
                    N=min(3,len(g.types[typp]))
                    temp=0
                    op.write("---- %s ----\n"%typp)
                    #print("---- %s ----"%typp)
                    for i in range(N):
                        op.write("No.%d:  %s,  star=%.2f\n"%(i+1,g.types[typp][i],g.films[g.types[typp][i]]["star"]))
                        #print("No.%d:  %s,  star=%.2f"%(i+1,g.types[typp][i],g.films[g.types[typp][i]]["star"]))
                        temp+=g.films[g.types[typp][i]]["star"]
                    op.write("平均星级：%.2f\n\n"%(temp/N))
                    #print("平均星级：",temp/N)
            #print('\n')
    '''
    op.write("图表编号\t排名\t类别\t出现次数\t平均星级\n")
    for g in result:#电影分类
        film_typen(g,type_set)
        count+=1
        if (count in range(1,21)) or (count in range(4558,4578)):
            op.write("%d\t"%count)
            #print("Graph %d"%count)
            items=list(g.types.items())
            items.sort(key=lambda x:(-len(x[1]),x[0]))
            for i in range(3):
                if len(items[i][1])>0:
                    if i==0:
                        op.write("%d\t%s\t%d\t%.2f\n"%(i+1,items[i][0],len(items[i][1]),sum([g.films[x]["star"] for x in items[i][1]])/len(items[i][1])))
                    else:
                        op.write("\t%d\t%s\t%d\t%.2f\n"%(i+1,items[i][0],len(items[i][1]),sum([g.films[x]["star"] for x in items[i][1]])/len(items[i][1])))
                else:
                    break
    #周星驰
    op.write("\n周星驰出演电影：%s\n"%str(Total_Graph.actors["周星驰"].attend))
    op.write("周星驰出演电影数：%d\n"%len(Total_Graph.actors["周星驰"].attend))
    #print("周星驰出演电影：",Total_Graph.actors["周星驰"].attend)
    op.write("周星驰参与电影平均星级：%.2f\n"%(sum([Total_Graph.films[name]["star"] for name in Total_Graph.actors["周星驰"].attend])/len(Total_Graph.actors["周星驰"].attend)))
    #print("周星驰参与电影平均星级：%.2f"%(sum([Total_Graph.films[name]["star"] for name in Total_Graph.actors["周星驰"].attend])/len(Total_Graph.actors["周星驰"].attend)))
    op.write("周星驰合作人数：%d\n"%len(Total_Graph.actors["周星驰"].connectTo))
    #print("周星驰合作人数：",len(Total_Graph.actors["周星驰"].connectTo))
    op.write("周星驰电影所属类别前三名：\n")
    op.write("周星驰电影类别前三名：\n")
    #print("周星驰圈子电影前三名：")
    '''
    temp_dict={}
    for typp in type_set:
        temp_dict[typp]=[]
    for name in Total_Graph.actors["周星驰"].attend:
        for typp in Total_Graph.films[name]["type"].split(","):
            temp_dict[typp].append(name)
    for typp in type_set:
        L=len(temp_dict[typp])
        temp_dict[typp].sort(key=lambda x:-Total_Graph.films[x]["star"])
        if L>0:
            op.write("  ---- %s ----\n"%typp)
            #print("  ---- %s ----"%typp)
            N=min(3,L)
            for i in range(N):
                op.write("  No.%d: %s  ,star=%.2f\n"%(i+1,temp_dict[typp][i],Total_Graph.films[temp_dict[typp][i]]["star"]))
                #print("  No.%d: %s  ,star=%.2f"%(i+1,temp_dict[typp][i],Total_Graph.films[temp_dict[typp][i]]["star"]))
    '''
    temp_dict={}
    for typp in type_set:
        temp_dict[typp]=[]
    for name in Total_Graph.actors["周星驰"].attend:
        for typp in Total_Graph.films[name]["type"].split(","):
            temp_dict[typp].append(name)
    items=list(temp_dict.items())
    items.sort(key=lambda x:(-len(x[1]),x[0]))
    for i in range(3):
        if len(items[i][1])>0:
            op.write("No.%d %s\n    出现次数：%d   平均星级:%.2f\n"%(i+1,items[i][0],len(items[i][1]),sum([Total_Graph.films[x]["star"] for x in items[i][1]])/len(items[i][1])))
        else:
            break
    
    op.write("\n周星驰合作者信息：\n")
    #print("周星驰合作者信息：")
    total_films=set()
    for actor in Total_Graph.actors["周星驰"].connectTo.keys():
        #op.write("%s:\n"%actor.name)
        #print("%s:"%actor.name)
        #op.write("  电影总数：%d\n"%len(Total_Graph.actors[actor.name].attend))
        #print("  电影总数：",len(Total_Graph.actors[actor.name].attend))
        #op.write("  电影：%s\n"%str(Total_Graph.actors[actor.name].attend))
        #print("  电影：",Total_Graph.actors[actor.name].attend)
        #op.write("  平均星级：%.2f\n"%(sum([Total_Graph.films[name]["star"] for name in Total_Graph.actors[actor.name].attend])/len(Total_Graph.actors[actor.name].attend)))
        #print("  平均星级：%.2f"%(sum([Total_Graph.films[name]["star"] for name in Total_Graph.actors[actor.name].attend])/len(Total_Graph.actors[actor.name].attend)))
        total_films=total_films|Total_Graph.actors[actor.name].attend
        #每个人出演类别前三名
        #op.write("  各类别前三名：\n")
        act_dict={}#一个字典放电影
        for typp in type_set:
            act_dict[typp]=[]
        for name in actor.attend:
            for typp in Total_Graph.films[name]["type"].split(","):
                act_dict[typp].append(name)
        for typp in type_set:
            L=len(act_dict[typp])
            act_dict[typp].sort(key=lambda x:-Total_Graph.films[x]["star"])
            if L>0:
                #op.write("    ---- %s ----\n"%typp)
                N=min(3,L)
                for i in range(N):
                    pass
                    #op.write("    No.%d: %s  ,star=%.2f\n"%(i+1,act_dict[typp][i],Total_Graph.films[act_dict[typp][i]]["star"]))
    op.write("周星驰圈子电影平均星级：%.2f\n"%(sum([Total_Graph.films[name]["star"] for name in total_films])/len(total_films)))
    op.write("周星驰圈子电影总数：%d\n"%len(total_films))
    temp_dict={}
    for typp in type_set:
        temp_dict[typp]=[]
    for name in total_films:
        for typp in Total_Graph.films[name]["type"].split(","):
            temp_dict[typp].append(name)
    items=list(temp_dict.items())
    items.sort(key=lambda x:(-len(x[1]),x[0]))
    for i in range(3):
        if len(items[i][1])>0:
            op.write("No.%d %s\n    出现次数：%d   平均星级:%.2f\n"%(i+1,items[i][0],len(items[i][1]),sum([Total_Graph.films[x]["star"] for x in items[i][1]])/len(items[i][1])))
        else:
            break
    '''
    op.write("\n周星驰圈子电影类别前三名：\n")
    #print("周星驰圈子电影前三名：")
    temp_dict={}
    for typp in type_set:
        temp_dict[typp]=[]
    for name in total_films:
        for typp in Total_Graph.films[name]["type"].split(","):
            temp_dict[typp].append(name)
    for typp in type_set:
        L=len(temp_dict[typp])
        temp_dict[typp].sort(key=lambda x:-Total_Graph.films[x]["star"])
        if L>0:
            op.write("  ---- %s ----\n"%typp)
            #print("  ---- %s ----"%typp)
            N=min(3,L)
            for i in range(N):
                op.write("  No.%d: %s  ,star=%.2f\n"%(i+1,temp_dict[typp][i],Total_Graph.films[temp_dict[typp][i]]["star"]))
                #print("  No.%d: %s  ,star=%.2f"%(i+1,temp_dict[typp][i],Total_Graph.films[temp_dict[typp][i]]["star"]))
    '''
    op.write("\n川普：\n")
    op.write("总数：%d\n"%len(Total_Graph.actors["唐纳德·特朗普"].attend))
    op.write("%s\n"%str(Total_Graph.actors["唐纳德·特朗普"].attend))
    op.write("川普出演电影平均星级：%.2f\n"%(sum([Total_Graph.films[name]["star"] for name in Total_Graph.actors["唐纳德·特朗普"].attend])/len(Total_Graph.actors["唐纳德·特朗普"].attend)))
    op.write("阿甘正传相关：\n")
    op.write("演员\t出演电影数目\t平均星级\n")
    for name in Total_Graph.films["阿甘正传 Forrest Gump"]["actor"].split(","):
        op.write("%s\t%d\t%.2f\n"%(name,len(Total_Graph.actors[name].attend),sum([Total_Graph.films[x]["star"] for x in Total_Graph.actors[name].attend])/len(Total_Graph.actors[name].attend)))
    op.write("\n肖申克的救赎相关：\n")
    op.write("演员\t出演电影数目\t平均星级\n")
    for name in Total_Graph.films["肖申克的救赎 The Shawshank Redemption"]["actor"].split(","):
        op.write("%s\t%d\t%.2f\n"%(name,len(Total_Graph.actors[name].attend),sum([Total_Graph.films[x]["star"] for x in Total_Graph.actors[name].attend])/len(Total_Graph.actors[name].attend)))
    op.write("卷福大法好（本尼迪克特·康伯巴奇）：")
    op.write("出演电影数：%d\t平均星级:%.2f"%(len(Total_Graph.actors["本尼迪克特·康伯巴奇"].attend),sum([Total_Graph.films[name]["star"] for name in Total_Graph.actors["本尼迪克特·康伯巴奇"].attend])/len(Total_Graph.actors["本尼迪克特·康伯巴奇"].attend)))
    op.close()
            

    #作图
    draw(result)


t = threading.Thread(target=myprog)
t.start()  # 启动线程
t.join()  # 进程等待线程结束


