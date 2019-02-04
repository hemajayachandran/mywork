list = [{"Name":"Player1","Role":"Opener","BatSkill":50,"BowlSkill":0},

{"Name":"Player2","Role":"TopOrder","BatSkill":60,"BowlSkill":0},

{"Name":"Player3","Role":"AllRounder","BatSkill":50,"BowlSkill":15},

{"Name":"Player4","Role":"Bowler","BatSkill":41,"BowlSkill":79},

{"Name":"Player5","Role":"AllRounder","BatSkill":44,"BowlSkill":25},

{"Name":"Player6","Role":"Bowler","BatSkill":10,"BowlSkill":60},

{"Name":"Player7","Role":"Bowler","BatSkill":20,"BowlSkill":55},

{"Name":"Player8","Role":"Bowler","BatSkill":30,"BowlSkill":55},

{"Name":"Player9","Role":"TopOrder","BatSkill":51,"BowlSkill":0},

{"Name":"Player10","Role":"Opener","BatSkill":55,"BowlSkill":0},

{"Name":"Player11","Role":"MiddleOrder","BatSkill":46,"BowlSkill":15},

{"Name":"Player12","Role":"TopOrder","BatSkill":46,"BowlSkill":0},

{"Name":"Player13","Role":"WK","BatSkill":60,"BowlSkill":0},

{"Name":"Player14","Role":"MiddleOrder","BatSkill":46,"BowlSkill":20},

{"Name":"Player15","Role":"WK","BatSkill":50,"BowlSkill":0},

{"Name":"Player16","Role":"Opener","BatSkill":42,"BowlSkill":0},

{"Name":"Player17","Role":"MiddleOrder","BatSkill":46,"BowlSkill":0},

{"Name":"Player18","Role":"Opener","BatSkill":44,"BowlSkill":0}]

list_tmp =[]
n=0
count = 3
top_player =[]
final_list = []

for i in range(0,len(list)):
    if list[i]["Role"] == "Bowler":
        list_tmp.append(list[i])
while (count>=0):
    
    for j in range(0,len(list_tmp)):
        for k in range(0,len(list_tmp)):
            if list_tmp[j]["BowlSkill"] > list_tmp[k]["BowlSkill"] and k!=j:
                top_player.append(list_tmp[j])
            elif list_tmp[j]["BowlSkill"] < list_tmp[k]["BowlSkill"] and k!=j:
                top_player.append(list_tmp[k])
    
            final_list.append(top_player)
            top_player.remove(top_player)
            n+=1
            count-=1

print(list_tmp)
print(final_list)
