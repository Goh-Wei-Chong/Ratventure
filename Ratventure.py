import random
c1 = 0
c2 = 0
#Name: Goh Wei Chong
#Class: P10
#ID: S10204647A
#Week 1 - Finished the basic features
#Week 2 - Added several addtional features(For every 10 days that passes,the enemies attacks will be 1 damage higher)
#Week 2 - Two advanced features(program validation and view top scores)
#Week 3 - Finished adding the last two advanced features and one more additional feature(when orb is found hero's health goes up by 5)
#Week 3 - This is due to the increase of enemies attacks, making them too powerful to defeat without the health buff
#-----------------------------------------------------------------------------------                
#lists
hy = []
hx = []
main = ['New Game', 'Resume Game', 'Exit Game', 'View Top Scores']
menu_1 = ['View Character', 'View Map', 'Move', 'Rest', 'Save Game', 'Exit Game']
menu_2 = ['View Character', 'View Map', 'Move', 'Sense Orb', 'Exit Game']
d_map = ['+---+---+---+---+---+---+---+---+', '| T |   |   |   |   |   |   |   |',
         '+---+---+---+---+---+---+---+---+', '|   |   |   |   |   |   |   |   |',
         '+---+---+---+---+---+---+---+---+', '|   |   |   |   |   |   |   |   |',
         '+---+---+---+---+---+---+---+---+', '|   |   |   |   |   |   |   |   |',
         '+---+---+---+---+---+---+---+---+', '|   |   |   |   |   |   |   |   |',
         '+---+---+---+---+---+---+---+---+', '|   |   |   |   |   |   |   |   |',
         '+---+---+---+---+---+---+---+---+', '|   |   |   |   |   |   |   |   |',
         '+---+---+---+---+---+---+---+---+', '|   |   |   |   |   |   |   | K |',
         '+---+---+---+---+---+---+---+---+']
#town
t0 = {'x':2,'y':1}
t1 = {'x':0,'y':3}
t2 = {'x':0,'y':7}
t3 = {'x':0,'y':9}
t4 = {'x':0,'y':13}
k = {'x':30,'y':15}
places = [t1,t2,t3,t4,k]
placing = [t0,t1,t2,t3,t4]
#-----------------------------------------------------------------------------------
#original placement
hori = 2
verti = 1
num = 0

#hero stats
hero = {'daL':2,'daH':4,'de':1,'hp':20}

#rat king stats
king = {'daL':6,'daH':10,'de':5,'hp':25}

#rat stats
rat = {'daL':1,'daH':3,'de':1,'hp':10}

#-----------------------------------------------------------------------------------
#fuctions
#move
def a(hori,verti,num):
    o = 0
    if hori < 2:
        hori += 4
    elif hori >= len(d_map[0]):
        hori -= 4
    elif verti < 1:
        verti += 2
    elif verti >= len(d_map):
        verti -= 2
    else:
        o = 1
        #hero/town to town
        if 'H/T' in d_map[verti + num]:
            d_map[verti + num] = d_map[verti + num].replace('H/T', ' T ')
        #hero/king to king
        if 'H/K' in d_map[verti + num]:
            d_map[verti + num] = d_map[verti + num].replace('H/K', ' K ')
        #remove H in tile
        if 'H' in d_map[verti + num]:
            d_map[verti + num] = d_map[verti + num].replace('| H |', '|   |')
        d_map[verti] = list(d_map[verti])
        #town to hero/town
        if d_map[verti][hori] == 'T':
            d_map[verti].insert(hori-1,'H/T')
            for f in range(3):
                d_map[verti].pop(hori)
        #king to hero/king
        elif d_map[verti][hori] == 'K':
            d_map[verti].insert(hori-1,'H/K')
            for f in range(3):
                d_map[verti].pop(hori)
        #move a tile
        elif d_map[verti][hori] == ' ':
            d_map[verti].pop(hori)
            d_map[verti].insert(hori,'H')
        d_map[verti] = ''.join(str(j) for j in d_map[verti])
    maps(d_map)
    if o == 0:
        print('Unable to move any further, try again')
    return [verti,hori,o]

#day
def day(i):
    if 'H/T' in d_map[verti]:
        return print('Day {}: You are in a town'.format(i))
    else:
        return print('Day {}: You are out in the open'.format(i))
    
#map
def maps(d_map):
    for m in range(17):
        print('{}'.format(d_map[m]))
        
#battle
def battles(hero,rat,king):
    #type of enemy
    if 'H/K' in d_map[verti]:
        name_enemy = king
        n_enemy = 'Rat king'
        health = 25
    else:
        name_enemy = rat
        n_enemy = 'Rat'
        health = 10
    while True:
        print('''Encounter! - {}
Damage: {}-{}
Defence:   {}
HP: {}
1) Attack
2) Run'''.format(n_enemy,name_enemy['daL'],name_enemy['daH'],name_enemy['de'],name_enemy['hp']))
        attacker = random.randint(name_enemy['daL'],name_enemy['daH'])
        hero_attack = random.randint(hero['daL'],hero['daH'])
        damage = attacker
        #choice
        battle_choice = input('Enter choice: ')
        print()
        #attack
        if battle_choice == '1':
            damage2 = hero_attack - name_enemy['de']
            if damage2 < 0:
                damage2 = 0
            print('You deal {} damage to the {}'.format(damage2,n_enemy))
            name_enemy['hp'] = name_enemy['hp'] + name_enemy['de'] - hero_attack
            #win
            if name_enemy['hp'] <= 0:
                print('The {} is dead! You are victorious!'.format(n_enemy))
                break
            #damaged
            else:
                damage1 = damage - hero['de']
                if damage1 < 0:
                    damage1 = 0
                print('Ouch! The {} hit you for {} damage!'.format(n_enemy,damage1))
                hero['hp'] = hero['hp'] + hero['de'] - damage
            #lose
            if hero['hp'] <= 0:
                print('You have been defeated!')
                print('GAME OVER')
                break
            #hp left
            else:
                print('You have {} HP left.'.format(hero['hp']))
        #run
        elif battle_choice == '2':
            print('You run and hide')
            print()
            name_enemy['hp'] = health
            break
        #wrong input
        else:
            print('Wrong input, try again')
    return [hero['hp'],king['hp']]

#Hero stats
def caf(hero):
    print('''The Hero
  Damage: {}-{}
 Defence: {}
      HP: {}'''.format(hero['daL'],hero['daH'],hero['de'],hero['hp']))
#-----------------------------------------------------------------------------------
#main menu
print('Welcome to Ratventure!')
print('----------------------')

for i in range(4):
    #main menu
    print('{}) {}'.format(i+1, main[i]))
while True:
    #first choice
    mc = input('Enter choice: ')
    print()
    #New Game
    if mc == '1':
        for h in range(18,31):
            hx.append(h)
        #randomised Town coordinates
        for kp in range(1,5):
            hy = []
            for h in range(2,31):
                hy.append(h)
            #how many spaces is the town far away from each other in terms of y-axis
            if placing[kp]['y'] - placing[kp-1]['y'] == 2:
                hd = 8
                if placing[kp-1]['x']+hd > 30:
                    oi = 0
                    if placing[kp-1]['x']+4 == 30:
                        oi = 4
                else:
                    oi = 8
                if placing[kp-1]['x']-hd < 2:
                    oy = 0
                    if placing[kp-1]['x']-4 == 2:
                        oy = 4
                else:
                    oy = 8
            if placing[kp]['y'] - placing[kp-1]['y'] == 4:
                hd = 4
                if placing[kp-1]['x']+hd > 30:
                    oi = 0
                else:
                    oi = 4
                if placing[kp-1]['x']-hd < 2:
                    oy = 0
                else:
                    oy = 4
            for uj in range(placing[kp-1]['x']-oy,placing[kp-1]['x']+oi+1):
                hy.remove(uj)
            while True:
                placing[kp]['x'] = random.choice(hy)
                if placing[kp]['x']%4 == 2 or placing[kp]['x'] == 2:
                    break
            hy = []
            for h in range(2,31):
                hy.append(h)
            d_map[placing[kp]['y']] = list(d_map[placing[kp]['y']])
            d_map[placing[kp]['y']].pop(placing[kp]['x'])
            d_map[placing[kp]['y']].insert(placing[kp]['x'],'T')
            d_map[placing[kp]['y']] = ''.join(str(j) for j in d_map[placing[kp]['y']])
        
        #randomised orb location
        #y-coordinates
        while True:
            y = random.randint(1,15)
            if y%2 == 1:
                break
        #check the coordinates the towns are in and remove coordinates to prevent orb to be in same coordinates as towns
        for f in places:
            if y == f['y']:
                if y < 8 and f['x'] > 18:
                    hx.remove(f['x'])
                else:
                    hy.remove(f['x'])
        #x-coordinates
        while True:
            if y < 8:
                x = random.choice(hx)
                if x%4 == 2:
                    break
            else:
                x = random.choice(hy)
                if x%4 == 2 or x == 2:
                    break
        #Hero Stats
        hero = {'daL':2,'daH':4,'de':1,'hp':20}
        i = 1
        d_map[verti] = list(d_map[verti])
        #hero location
        if d_map[verti][hori] == 'T':
            d_map[verti].insert(hori-1,'H/T')
            for f in range(3):
                d_map[verti].pop(hori)
        d_map[verti] = ''.join(str(j) for j in d_map[verti])
        break
        
    #saved game
    elif mc == '2':
        #data file
        file = open('data.txt','r')
        for q in file:
            q = q.strip().split(',')
            #hero stats
            hero['daL'] = int(q[0])
            hero['daH'] = int(q[1])
            hero['de'] = int(q[2])
            hero['hp'] = int(q[3])
            #days
            i = int(q[4])
            #orb location
            x = int(q[5])
            y = int(q[6])
            #town location
            t1 = {'x':int(q[7]),'y':int(q[8])}
            t2 = {'x':int(q[9]),'y':int(q[10])}
            t3 = {'x':int(q[11]),'y':int(q[12])}
            t4 = {'x':int(q[13]),'y':int(q[14])}
            places = [t1,t2,t3,t4]
            verti = int(q[15])
            hori = int(q[16])
            #form map
            for place in range(4):
                d_map[places[place]['y']] = list(d_map[places[place]['y']])
                d_map[places[place]['y']].pop(places[place]['x'])
                d_map[places[place]['y']].insert(places[place]['x'],'T')
                d_map[places[place]['y']] = ''.join(str(j) for j in d_map[places[place]['y']])
        file.close()
        d_map[verti] = list(d_map[verti])
        #hero location
        if d_map[verti][hori] == 'T':
            d_map[verti].insert(hori-1,'H/T')
            for f in range(3):
                d_map[verti].pop(hori)
        d_map[verti] = ''.join(str(j) for j in d_map[verti])
        break
    #Exit       
    elif mc == '3':
        print('+++++Exit Game+++++')
        break

    #Top scores
    elif mc == '4':
        #speed file
        speed = open('speed.txt','r')
        t = []
        for time in speed:
            time = time.strip('\n').split('\n')
            t.append(time)
            t.sort()
        if len(t) > 5:
            leng = 6
        else:
            leng = len(t)
        #list out days(only 5 or less)
        for r in range(1,leng):
            print('{}) {} days'.format(r,t[r-1][0]))
        speed.close()
            
    #wrong input
    else:
        print('Wrong input, try again')
#-----------------------------------------------------------------------------------
#adventure
if mc == '1' or mc == '2':
    while True:
        c1 = 0
        c2 = 0
        day(i)
        if 'H/T' in d_map[verti]:
            #second menu
            for c in range(6):
                print('{}) {}'.format(c+1, menu_1[c]))
            #choices
            c1 = input('Enter choice: ')
        else:
            #third menu
            for p in range(5):
                print('{}) {}'.format(p + 1,menu_2[p]))
            #choices
            c2 = input('Enter choice: ')
        print()
        
        #view character - menu 2 and 3
        if c1 == '1' or c2 == '1':
            caf(hero)
            #display found orb
            if hero['de'] == 6:
                print('You are holding the orb of power')
            if 'H/T' not in d_map[verti]:
                print()
                hp_list = battles(hero,rat,king)
                hero['hp'] = hp_list[0]
                king['hp'] = hp_list[1]
            print()
            
        #view map - menu 2 and 3
        elif c1 == '2' or c2 == '2':
            maps(d_map)
            if 'H/T' not in d_map[verti]:
                print()
                hp_list = battles(hero,rat,king)
                hero['hp'] = hp_list[0]
                king['hp'] = hp_list[1]
            print()

        #move - menu 2 and 3
        elif c1 == '3' or c2 == '3':
            maps(d_map)
            print('W = up; A = left; S = down; D = right')
            while True:
                move = input('Your move: ')
                move.lower()
                #left
                if move == 'a':
                    num = 0
                    hori -= 4
                #right
                elif move == 'd':
                    num = 0
                    hori += 4
                #up
                elif move == 'w':
                    num = 2
                    verti -= 2
                #down
                elif move == 's':
                    num = -2
                    verti += 2
                #wrong input
                else:
                    print('Wrong input, try again')
                    continue
                if move == 'a' or move == 'd' or move == 's' or move == 'w':
                    yt = a(hori,verti,num)
                    verti = yt[0]
                    hori = yt[1]
                    if yt[2] == 1:
                        i += 1
                    if 'H/T' not in d_map[verti]:
                        day(i)
                        hp_list = battles(hero,rat,king)
                        hero['hp'] = hp_list[0]
                        king['hp'] = hp_list[1]
                break

        #Rest - menu 2
        elif c1 == '4':
            hero['hp'] = 20
            i += 1
            print('You are fully healed.')

        #save game - menu 2
        elif c1 == '5':
            print()
            file = open('data.txt','w')
            file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(hero['daL'],hero['daH'],hero['de'],hero['hp'],i,x,y,t1['x'],t1['y'],t2['x'],t2['y'],t3['x'],t3['y'],t4['x'],t4['y'],verti,hori))
            file.close()
            print('Game saved.')
            
        #sense orb - menu 3
        elif c2 == '4':
            i += 1
            #found orb
            if verti == y and hori == x:
                print('''You found the Orb of Power!
Your attack increases by 5!
Your defense increases by 5!''')
                hero['daL'] += 5
                hero['daH'] += 5
                hero['de'] += 5
                x = -1
            #if orb is already found
            elif x == -1:
                print('Orb has already been found')
            #direction of orb
            else:
                if verti == y:
                    if hori < x:
                        direction = 'east'
                    elif hori > x:
                        direction = 'west'

                elif verti < y:
                    if hori < x:
                        direction = 'southeast'
                    elif hori > x:
                        direction = 'southwest'
                    else:
                        direction = 'south'

                elif verti > y:
                    if hori < x:
                        direction = 'northeast'
                    elif hori > x:
                        direction = 'northwest'
                    else:
                        direction = 'north'
                print('You sense that the Orb of Power is to the {}'.format(direction))

        #Exit - menu 2 and 3
        elif c1 == '6' or c2 == '5':
            print('+++++Exit Game+++++')
            break
        #wrong input
        else:
            print('Wrong input, try again')
        #enemy health reset
        rat['hp'] = 10
        #king killed
        if king['hp'] <= 0:
            print('Congratulations, you have defeated the Rat King!')
            print('The world is saved! You win!')
            speed = open('speed.txt','a')
            speed.write('{}\n'.format(i))
            speed.close()
            break
        #hero killed
        if hero['hp'] <= 0:
            break
            
        
        
