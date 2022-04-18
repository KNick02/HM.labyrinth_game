import random
import time
ways = [[[False,False,False,False]for j in range(7)]for i in range(7)]
for x in range(7):
    for y in range(7):
        if (x+2)%2==0 and (y+2)%2==0:
            if x==0:
                ways[x][y][1]=True
            if x==6:
                ways[x][y][3]=True
            if y==0:
                ways[x][y][2]=True
            if y==6:
                ways[x][y][0]=True
            if x>0 and x<6 and (y==0 or y==6):
                ways[x][y][1],ways[x][y][3]=True,True
            if y>0 and y<6 and (x==0 or x==6):
                ways[x][y][0],ways[x][y][2]=True,True
ways[2][2][0],ways[2][2][1],ways[2][2][2]=True,True,True
ways[4][4][0],ways[4][4][3],ways[4][4][2]=True,True,True
ways[2][4][0],ways[2][4][1],ways[2][4][3]=True,True,True
ways[4][2][3],ways[4][2][1],ways[4][2][2]=True,True,True
cx = {'Ae':0,'BC':0,'Bk':0,'Bl':0,'Bn':0,'Br':0,'Ce':0,'Cp':0,'Cs':0,'Ct':0,'Cy':0,'Dd':0,'Dr':0,'Ed':0,'Fh':0,'GC':0,'Gd':0,'Gs':0,'Lf':0,'Ln':0,'Lt':0,'Mn':0,'RC':0,'Rw':0,'Sl':0,'Sr':0,'Wn':0,'YC':0}
cy = {'Ae':0,'BC':0,'Bk':0,'Bl':0,'Bn':0,'Br':0,'Ce':0,'Cp':0,'Cs':0,'Ct':0,'Cy':0,'Dd':0,'Dr':0,'Ed':0,'Fh':0,'GC':0,'Gd':0,'Gs':0,'Lf':0,'Ln':0,'Lt':0,'Mn':0,'RC':0,'Rw':0,'Sl':0,'Sr':0,'Wn':0,'YC':0}

from tkinter import *
root = Tk()
root.title('Labyrinth Game')
cardsphoto = {}
cardslabel = {}
for name in cx.keys():
    cardsphoto[name] = PhotoImage(file='cards/'+name+'.png')
    cardslabel[name] = Label(root,image = cardsphoto[name],bd = 0)

cx['RC'],cy['RC'] = 6,0
cx['GC'],cy['GC'] = 0,6
cx['BC'],cy['BC'] = 6,6
cx['YC'],cy['YC'] = 0,0
cx['Ae'],cy['Ae']=2,0
cx['Bk'],cy['Bk']=4,0
cx['Bl'],cy['Bl']=6,2
cx['Bn'],cy['Bn']=6,4
cx['Br'],cy['Br']=2,6
cx['Ce'],cy['Ce']=4,6
cx['Cp'],cy['Cp']=0,2
cx['Cs'],cy['Cs']=0,4
cx['Ct'],cy['Ct']=2,2
cx['Cy'],cy['Cy']=4,2
cx['Dd'],cy['Dd']=4,4
cx['Dr'],cy['Dr']=2,4
glike = ['Ed','Fh','Gd','Gs','Lf','Ln']
tlike = ['Lt','Mn','Rw','Sl','Sr','Wn']
straight = 12
t = 6
g = 16
for x in range(7):
    for y in range(7):
        if (x+2)%2==1 or (y+2)%2==1:
            choice = []
            if straight>0:
                choice.append('str')
            if t>0:
                choice.append('t')
            if g>0:
                choice.append('g')
            choice = random.choice(choice)
            if choice=='str':
                straight-=1
                if random.randint(0,1)==0:
                    ways[x][y][0],ways[x][y][2]=True,True
                else:
                    ways[x][y][1],ways[x][y][3]=True,True
            if choice=='t':
                t-=1
                card = random.choice(tlike)
                cx[card],cy[card] = x,y
                tlike.remove(card)
                side = random.randint(0,3)
                if side==0:
                    ways[x][y][3],ways[x][y][0],ways[x][y][1]=True,True,True
                if side==1:
                    ways[x][y][0],ways[x][y][1],ways[x][y][2]=True,True,True
                if side==2:
                    ways[x][y][2],ways[x][y][3],ways[x][y][1]=True,True,True
                if side==3:
                    ways[x][y][2],ways[x][y][3],ways[x][y][0]=True,True,True
            if choice=='g':
                g-=1
                if len(glike)>0:
                    card = random.choice(glike)
                    cx[card],cy[card]=x,y
                    glike.remove(card)
                corner = random.randint(0,3)
                if corner==0:
                    ways[x][y][0],ways[x][y][1]=True,True
                if corner==1:
                    ways[x][y][1],ways[x][y][2]=True,True
                if corner==2:
                    ways[x][y][2],ways[x][y][3]=True,True
                if corner==3:
                    ways[x][y][3],ways[x][y][0]=True,True 
if g==1:
    ext_ways = [False,True,True,False]
elif t==1:
    ext_ways = [True,True,True,False]
else:
    ext_ways = [True,False,True,False]
c = []

def get_card(x,y):
    for name in cx.keys():
        if cx[name]==x and cy[name]==y:
            return name
    return False
        
def pict(way):
    name = ''
    if way[0]==True:
        name+='0'
    if way[1]==True:
        name+='1'
    if way[2]==True:
        name+='2'
    if way[3]==True:
        name+='3'
    if way==[False,False,False,False]:
        name='cl'
    return (name+'.png')

def draw_cards():
    for name in cardslabel.keys():
        cardslabel[name].place(x=30+cx[name]*84,y=30+cy[name]*84)
        cardslabel[name].lift()
    root.update()

def lift_cards():
    for name in cardslabel.keys():
        cardslabel[name].lift()
temp = [[''for k in range(7)]for n in range(7)]
labels = [[''for k in range(7)]for n in range(7)]

def redraw_grid():   
    for i in range(7):
        for j in range(7):
            temp[i][j] = PhotoImage(file = pict(ways[i][j]))
            Label(root,image = temp[i][j],borderwidth=0).grid(row=j, column=i,padx=0,pady=0)

def hide(event):
    fut_ext = [value for value in ways[1][0]]
    for ro in range(7):
        if ro==6:
            global ext_ways
            ways[1][ro] = [value for value in ext_ways]
            temp[1][ro] = PhotoImage(file = pict(ways[1][ro]))
            Label(root,image = temp[1][ro],borderwidth=0).grid(row=ro, column=1)
        else:
            ways[1][ro] = [value for value in ways[1][ro+1]]
            temp[1][ro] = PhotoImage(file = pict(ways[1][ro]))
            Label(root,image = temp[1][ro],borderwidth=0).grid(row=ro, column=1)
    ext_ways = [value for value in fut_ext]

def turn_extra(ext):
    part_res = ['','','','']
    for value in range(4):
        part_res[value] = ext[(value-1)%4]
    return part_res
redraw_grid()
images = {}

for value in ['01','02','03','12','23','13','012','123','023','013']:
    images[value+'.png']=PhotoImage(file=value+'.png')

img_extra = images[pict(ext_ways)]
label_extra = Label(root,image = img_extra,borderwidth=0)
label_extra.grid(row=3,column=10)

def redraw_extra():
    global ext_ways
    ext_ways = [value for value in turn_extra(ext_ways)]
    img_extra = images[pict(ext_ways)]
    label_extra = Label(root,image = img_extra,borderwidth=0)
    label_extra.grid(row=3,column=10)
    if get_card(8,3)!=False:
        cardslabel[get_card(8,3)].lift()
button1 = Button(root,text='Turn',width=6,height=5,borderwidth=0,command=redraw_extra)
button1.grid(row=3,column=9)

def variant(ext):
    res = ['','','','']
    part_res = ['','','','']
    for count in range(4):
        for value in range(4):
            part_res[value] = ext[(value-count)%4]
        res[count] = [i for i in part_res]
    return res

def insert(x,y):
    if y==6:
        fut_ext = [value for value in ways[x][0]]
        for ro in range(7):
            if ro==6:
                global ext_ways
                ways[x][ro] = [value for value in ext_ways]
                temp[x][ro] = PhotoImage(file = pict(ways[x][ro]))
                Label(root,image = temp[x][ro],borderwidth=0).grid(row=ro, column=x)
            else:
                ways[x][ro] = [value for value in ways[x][ro+1]]
                temp[x][ro] = PhotoImage(file = pict(ways[x][ro]))
                Label(root,image = temp[x][ro],borderwidth=0).grid(row=ro, column=x)
        ext_ways = [value for value in fut_ext]
        img_extra = images[pict(ext_ways)]
        label_extra = Label(root,image = img_extra,borderwidth=0)
        label_extra.grid(row=3,column=10)
    if y==0:
        fut_ext = [value for value in ways[x][6]]
        for ro in range(7)[::-1]:
            if ro==0:
                ways[x][ro] = [value for value in ext_ways]
                temp[x][ro] = PhotoImage(file = pict(ways[x][ro]))
                Label(root,image = temp[x][ro],borderwidth=0).grid(row=ro, column=x)
            else:
                ways[x][ro] = [value for value in ways[x][ro-1]]
                temp[x][ro] = PhotoImage(file = pict(ways[x][ro]))
                Label(root,image = temp[x][ro],borderwidth=0).grid(row=ro, column=x)
        ext_ways = [value for value in fut_ext]
        img_extra = images[pict(ext_ways)]
        label_extra = Label(root,image = img_extra,borderwidth=0)
        label_extra.grid(row=3,column=10)
    if x==6:
        fut_ext = [value for value in ways[0][y]]
        for co in range(7):
            if co==6:
                ways[co][y] = [value for value in ext_ways]
                temp[co][y] = PhotoImage(file = pict(ways[co][y]))
                Label(root,image = temp[co][y],borderwidth=0).grid(row=y, column=co)
            else:
                ways[co][y] = [value for value in ways[co+1][y]]
                temp[co][y] = PhotoImage(file = pict(ways[co][y]))
                Label(root,image = temp[co][y],borderwidth=0).grid(row=y, column=co)
        ext_ways = [value for value in fut_ext]
        img_extra = images[pict(ext_ways)]
        label_extra = Label(root,image = img_extra,borderwidth=0)
        label_extra.grid(row=3,column=10)
    if x==0:
        fut_ext = [value for value in ways[6][y]]
        for co in range(7)[::-1]:
            if co==0:
                ways[co][y] = [value for value in ext_ways]
                temp[co][y] = PhotoImage(file = pict(ways[co][y]))
                Label(root,image = temp[co][y],borderwidth=0).grid(row=y, column=co)
            else:
                ways[co][y] = [value for value in ways[co-1][y]]
                temp[co][y] = PhotoImage(file = pict(ways[co][y]))
                Label(root,image = temp[co][y],borderwidth=0).grid(row=y, column=co)
        ext_ways = [value for value in fut_ext]
        img_extra = images[pict(ext_ways)]
        label_extra = Label(root,image = img_extra,borderwidth=0)
        label_extra.grid(row=3,column=10)
def save_insert2(x,y):
    if y==6:
        fut_ext = [value for value in ways[x][0]]
        for ro in range(7):
            if ro==6:
                global ext_ways
                ways[x][ro] = [value for value in ext_ways]
            else:
                ways[x][ro] = [value for value in ways[x][ro+1]]
        ext_ways = [value for value in fut_ext]
    if y==0:
        fut_ext = [value for value in ways[x][6]]
        for ro in range(7)[::-1]:
            if ro==0:
                ways[x][ro] = [value for value in ext_ways]
            else:
                ways[x][ro] = [value for value in ways[x][ro-1]]
        ext_ways = [value for value in fut_ext]
    if x==6:
        fut_ext = [value for value in ways[0][y]]
        for co in range(7):
            if co==6:
                ways[co][y] = [value for value in ext_ways]
            else:
                ways[co][y] = [value for value in ways[co+1][y]]
        ext_ways = [value for value in fut_ext]
    if x==0:
        fut_ext = [value for value in ways[6][y]]
        for co in range(7)[::-1]:
            if co==0:
                ways[co][y] = [value for value in ext_ways]
            else:
                ways[co][y] = [value for value in ways[co-1][y]]
        ext_ways = [value for value in fut_ext]
def check(start,finish,ways,mode):
    choose = [value for value in start]
    current = []
    poss = []
    current.append(choose)
    poss.append(choose)
    while current!=[]:
        x = current[-1][0]
        y = current[-1][1]
        choice = []
        if mode==1 and x==finish[0] and y==finish[1]:
            return current
        if x+1<7 and ways[x+1][y][3]==True and ways[x][y][1]==True and [x+1,y] not in poss:
                choice.append([x+1,y])		
        if y+1<7 and ways[x][y+1][0]==True and ways[x][y][2]==True and [x,y+1]not in poss:
                choice.append([x,y+1])
        if x-1>=0 and ways[x-1][y][1]==True and ways[x][y][3]==True and [x-1,y]not in poss:
                choice.append([x-1,y])
        if y-1>=0 and ways[x][y-1][2]==True and ways[x][y][0]==True and [x,y-1]not in poss:
                choice.append([x,y-1])
        if len(choice) == 0:
                current.pop()
                continue
        choice = choice[random.randint(0,len(choice)-1)]
        current.append(choice)
        poss.append(choice)
    if finish in poss:
        return True

def save_insert(x,y):
    if y==6:
        fut_ext = [value for value in ways[x][0]]
        for ro in range(7):
            if ro==6:
                global ext_ways
                ways[x][ro] = [value for value in ext_ways]
            else:
                ways[x][ro] = [value for value in ways[x][ro+1]]
        ext_ways = [value for value in fut_ext]
    if y==0:
        fut_ext = [value for value in ways[x][6]]
        for ro in range(7)[::-1]:
            if ro==0:
                ways[x][ro] = [value for value in ext_ways]
            else:
                ways[x][ro] = [value for value in ways[x][ro-1]]
        ext_ways = [value for value in fut_ext]
    if x==6:
        fut_ext = [value for value in ways[0][y]]
        for co in range(7):
            if co==6:
                ways[co][y] = [value for value in ext_ways]
            else:
                ways[co][y] = [value for value in ways[co+1][y]]
        ext_ways = [value for value in fut_ext]
    if x==0:
        fut_ext = [value for value in ways[6][y]]
        for co in range(7)[::-1]:
            if co==0:
                ways[co][y] = [value for value in ext_ways]
            else:
                ways[co][y] = [value for value in ways[co-1][y]]
        ext_ways = [value for value in fut_ext]

def button10():
    anim_card(1,0)
    insert(1,0)
    lift_cards()
def button30():
    anim_card(3,0)
    insert(3,0)
    lift_cards()
def button50():
    anim_card(5,0)
    insert(5,0)
    lift_cards()
def button16():
    anim_card(1,6)
    insert(1,6)
    lift_cards()
def button36():
    anim_card(3,6)
    insert(3,6)
    lift_cards()
def button56():
    anim_card(5,6)
    insert(5,6)
    lift_cards()
def button01():
    anim_card(0,1)
    insert(0,1)
    lift_cards()
def button03():
    anim_card(0,3)
    insert(0,3)
    lift_cards()
def button05():
    anim_card(0,5)
    insert(0,5)
    lift_cards()
def button61():
    anim_card(6,1)
    insert(6,1)
    lift_cards()
def button63():
    anim_card(6,3)
    insert(6,3)
    lift_cards()
def button65():
    anim_card(6,5)
    insert(6,5)
    lift_cards()

button10=Button(text=u'\u2193',command=button10)
button10.grid(row=8, column=1)
button30=Button(text=u'\u2193',command=button30)
button30.grid(row=8, column=3)
button50=Button(text=u'\u2193',command=button50)
button50.grid(row=8, column=5)
button16=Button(text=u'\u2191',command=button16)
button16.grid(row=7, column=1)
button36=Button(text=u'\u2191',command=button36)
button36.grid(row=7, column=3)
button56=Button(text=u'\u2191',command=button56)
button56.grid(row=7, column=5)
button01=Button(text=u'\u2192',command=button01)
button01.grid(row=1, column=8)
button03=Button(text=u'\u2192',command=button03)
button03.grid(row=3, column=8)
button05=Button(text=u'\u2192',command=button05)
button05.grid(row=5, column=8)
button61=Button(text=u'\u2190',command=button61)
button61.grid(row=1, column=7)
button63=Button(text=u'\u2190',command=button63)
button63.grid(row=3, column=7)
button65=Button(text=u'\u2190',command=button65)
button65.grid(row=5, column=7)
def search(pos,goal):
    global ways,ext_ways
    solve = []
    min_se = 37
    ways_copy = [value for value in ways]
    ext_ways_copy = [value for value in ext_ways]   
    for ins1,ins2 in [(0,1),(0,3),(0,5),(6,1),(6,3),(6,5),(1,0),(3,0),(5,0),(1,6),(3,6),(5,6)]:
        for ext_ways in variant(ext_ways):
            save_insert2(ins1,ins2)
            new_pos=[]
            new_goal=[]
            if pos[0]==ins1 and pos[0]>0 and pos[0]<6:
                if ins2==6:
                    new_pos = [ins1,(pos[1]-1)%7]
                if ins2==0:
                    new_pos = [ins1,(pos[1]+1)%7]
            elif pos[1]==ins2 and pos[1]>0 and pos[1]<6:
                if ins1==6:
                    new_pos = [(pos[0]-1)%7,ins2]
                if ins1==0:
                    new_pos = [(pos[0]+1)%7,ins2]
            elif new_pos==[]:
                new_pos=pos
            if goal[0]==ins1 and goal[0]>0 and goal[0]<6:
                if ins2==6:
                    new_goal = [ins1,(goal[1]-1)%7]
                if ins2==0:
                    new_goal = [ins1,(goal[1]+1)%7]
            elif goal[1]==ins2 and goal[1]>0 and goal[1]<6:
                if ins1==6:
                    new_goal = [(goal[0]-1)%7,ins2]
                if ins1==0:
                    new_goal = [(goal[0]+1)%7,ins2]
            elif new_goal==[]:
                new_goal=goal
            for i in range(7):
                for j in range(7):
                    if check(new_pos,[i,j],ways,0)==True and ((i-new_goal[0])**2+(j-new_goal[1])**2)<min_se:
                        solve = [ext_ways,ins1,ins2,i,j]
                        min_se = (i-new_goal[0])**2+(j-new_goal[1])**2
            ways = [value for value in ways_copy]
            ext_ways = [value for value in ext_ways_copy]
    return solve
def moving_player(x,y):
    stx = pl_lab.winfo_x()
    sty = pl_lab.winfo_y()
    for j in range(83):
        stx+=x
        sty+=y
        pl_lab.place(x=stx,y=sty)
        pl_lab.lift()
        root.update()
player = PhotoImage(file='cards/player.png')
pl_lab = Label(root,image = player,bd=0)
pl_lab.place(x=30,y=30)
pl_x,pl_y = 0,0
def click(event):
    global pl_x,pl_y
    x,y = event.x_root,event.y_root
    window = root.geometry().split('+')
    winx = int(window[1])
    winy = int(window[2])
    x,y = (x-winx)//83,(y-winy)//83
    anim_way = check([pl_x,pl_y],[x,y],ways,1)
    if anim_way!=None:
        for i in range(len(anim_way)-1):
            moving_player(anim_way[i+1][0]-anim_way[i][0],anim_way[i+1][1]-anim_way[i][1])
        pl_x,pl_y = x,y
    if get_card(pl_x,pl_y)==fplay[0]:
        del fplay[0]
        task()
    
def anim_card(column,row):
    global pl_x,pl_y,e_card,move
    move_list = []
    e_card = get_card(8,3)
    if column==0 or column==6:
        anim = [temp[i][row] for i in range(7)]
    else:
        anim = [temp[column][i]for i in range(7)]
    anim.append(images[pict(ext_ways)])
    anim_lab = [Label(root,image = card,borderwidth=0) for card in anim]
    if column==0:
        for name in cx.keys():
            if cy[name]==row and cx[name]<7:
                move_list.append(name)
        if pl_y==row:
            pl_x=(pl_x+1)%7
        for move in range(84):
            if e_card!=False:
                if move<=42:
                    cardslabel[e_card].place(x=30+84*cx[e_card]+move,y=30+84*cy[e_card])
                    cardslabel[e_card].lift()
                else:
                    cardslabel[e_card].place(x=30-84+move,y=30+84*row)
                    cardslabel[e_card].lift()
                    if move==83:
                        cx[e_card],cy[e_card]=0,row
            for name in move_list:
                if cx[name]<6:
                    cardslabel[name].place(x=30+84*cx[name]+move,y=30+84*cy[name])
                    cardslabel[name].lift()
                    if move==83:
                        cx[name]+=1
                else:
                    if move<=42:
                        cardslabel[name].place(x=30+84*cx[name]+move,y=30+84*cy[name])
                        cardslabel[name].lift()
                    else:
                        cardslabel[name].place(x=30+84*8,y=30+84*3)
                        cardslabel[name].lift()
                        if move==83:
                            cx[name],cy[name]=8,3
            for j in range(-1,7):
                anim_lab[j].place(x=84*j+move,y=84*row)
            if pl_y==row:
                pl_lab.place(x = (pl_lab.winfo_x()+1)%588,y = (pl_lab.winfo_y())%588)
                pl_lab.lift()
            root.update()
    if column==6:
        for name in cx.keys():
            if cy[name]==row and cx[name]<7:
                move_list.append(name)
        if pl_y==row:
            pl_x=(pl_x-1)%7
        for move in range(84):
            if e_card!=False:
                if move<=42:
                    cardslabel[e_card].place(x=30+84*cx[e_card]-move,y=30+84*cy[e_card])
                    cardslabel[e_card].lift()
                else:
                    cardslabel[e_card].place(x=30+84*7-move,y=30+84*row)
                    cardslabel[e_card].lift()
                    if move==83:
                        cx[e_card],cy[e_card]=6,row
            for name in move_list:
                if cx[name]>0:
                    cardslabel[name].place(x=30+84*cx[name]-move,y=30+84*cy[name])
                    cardslabel[name].lift()
                    if move==83:
                        cx[name]-=1
                else:
                    if move<=42:
                        cardslabel[name].place(x=30+84*cx[name]-move,y=30+84*cy[name])
                        cardslabel[name].lift()
                    else:
                        cardslabel[name].place(x=35+84*8,y=30+84*3)
                        cardslabel[name].lift()
                        if move==83:
                            cx[name],cy[name]=8,3
            for j in range(8):
                anim_lab[j].place(x=84*j-move,y=84*row)
            if pl_y==row:
                pl_lab.place(x = (pl_lab.winfo_x()-1)%588,y = (pl_lab.winfo_y())%588)
                pl_lab.lift()
            root.update()
    if row==0:
        for name in cx.keys():
            if cx[name]==column:
                move_list.append(name)
        if pl_x==column:
            pl_y=(pl_y+1)%7
        for move in range(84):
            if e_card!=False:
                if move<=42:
                    cardslabel[e_card].place(x=30+84*cx[e_card],y=30+84*cy[e_card]+move)
                    cardslabel[e_card].lift()
                else:
                    cardslabel[e_card].place(x=30+84*column,y=30-84+move)
                    cardslabel[e_card].lift()
                    if move==83:
                        cx[e_card],cy[e_card]=column,0
            for name in move_list:
                if cy[name]<6:
                    cardslabel[name].place(x=30+84*cx[name],y=30+84*cy[name]+move)
                    cardslabel[name].lift()
                    if move==83:
                        cy[name]+=1
                else:
                    if move<=42:
                        cardslabel[name].place(x=30+84*cx[name],y=30+84*cy[name]+move)
                        cardslabel[name].lift()
                    else:
                        cardslabel[name].place(x=35+84*8,y=30+84*3)
                        cardslabel[name].lift()
                        if move==83:
                            cx[name],cy[name]=8,3
            for j in range(-1,7):
                anim_lab[j].place(x=84*column,y=84*j+move)
            if pl_x==column:
                pl_lab.place(x = (pl_lab.winfo_x())%588,y = (pl_lab.winfo_y()+1)%588)
                pl_lab.lift()
            root.update()
    if row==6:
        for name in cx.keys():
            if cx[name]==column:
                move_list.append(name)
        if pl_x==column:
            pl_y=(pl_y-1)%7
        for move in range(84):
            if e_card!=False:
                if move<=42:
                    cardslabel[e_card].place(x=30+84*cx[e_card],y=30+84*cy[e_card]-move)
                    cardslabel[e_card].lift()
                else:
                    cardslabel[e_card].place(x=30+84*column,y=30+84*7-move)
                    cardslabel[e_card].lift()
                    if move==83:
                        cx[e_card],cy[e_card]=column,6
            for name in move_list:
                if cy[name]>0:
                    cardslabel[name].place(x=30+84*cx[name],y=30+84*cy[name]-move)
                    cardslabel[name].lift()
                    if move==83:
                        cy[name]-=1
                else:
                    if move<=42:
                        cardslabel[name].place(x=30+84*cx[name],y=30+84*cy[name]-move)
                        cardslabel[name].lift()
                    else:
                        cardslabel[name].place(x=35+84*8,y=30+84*3)
                        cardslabel[name].lift()
                        if move==83:
                            cx[name],cy[name]=8,3
            for j in range(8):
                anim_lab[j].place(x=84*column,y=84*j-move)
            if pl_x==column:
                pl_lab.place(x = (pl_lab.winfo_x())%588,y = (pl_lab.winfo_y()-1)%588)
                pl_lab.lift()
            root.update()
    for lab in anim_lab:
        lab.destroy()
    for name in move_list:
        cardslabel[name].lift()
root.bind('<ButtonPress>',click)
draw_cards()

#card giving
kit = []

for name in cx.keys():
    if name!='GC' and name!='RC' and name!='BC' and name!='YC':
        kit.append(name)
random.shuffle(kit)
fplay = kit[:12]
splay = kit[12:]
def task():
    global current_picture
    current_picture = PhotoImage(file = 'cards/'+fplay[0]+'.png')
    current_card = Label(root,image = current_picture,bd=5)
    current_card.grid(column=11,row=3)
task()
root.mainloop()


