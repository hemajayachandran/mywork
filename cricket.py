list = [{"Name":"Player1","Role":"Opener","BatSkill":50,"BowlSkill":0},

{"Name":"Player2","Role":"TopOrder","BatSkill":60,"BowlSkill":0},

{"Name":"Player3","Role":"AllRounder","BatSkill":50,"BowlSkill":15},

{"Name":"Player4","Role":"Bowler","BatSkill":41,"BowlSkill":60},

{"Name":"Player5","Role":"AllRounder","BatSkill":44,"BowlSkill":25},

{"Name":"Player6","Role":"Bowler","BatSkill":10,"BowlSkill":79},

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

list_tmp,tmp_list, final_list =[],[],[]
for i in range(0,len(list)):
  if list[i]["Role"] == "Opener":
    list_tmp.append(list[i])
#print("The full list of Openers:",list_tmp)
k,j=0,0
while(k<len(list_tmp)):
  while(j<len(list_tmp)):
    if k==j:
      j+=1
    elif list_tmp[k]["BatSkill"] < list_tmp[j]["BatSkill"]:
      k=j
      j+=1
    elif list_tmp[k]["BatSkill"] > list_tmp[j]["BatSkill"]:
      j+=1
    else:
      if list_tmp[k]["BowlSkill"] < list_tmp[j]["BowlSkill"]:
        k=j
        j+=1
      elif list_tmp[k]["BowlSkill"] > list_tmp[j]["BowlSkill"]:
        j+=1
      else:
        break
  tmp_list.append(list_tmp[k])
  final_list.append((list_tmp[k]["Name"],list_tmp[k]["Role"]))
  list_tmp.remove(list_tmp[k])
  k,j=0,0
  if len(tmp_list) == 2:
    break
#print("\nThe final opener's list:",tmp_list)

list_tmp,tmp_list =[],[]
for i in range(0,len(list)):
  if list[i]["Role"] == "TopOrder":
    list_tmp.append(list[i])
#print("The full list of TopOrder:",list_tmp)
k,j=0,0
while(k<len(list_tmp)):
  while(j<len(list_tmp)):
    if k==j:
      j+=1
    elif list_tmp[k]["BatSkill"] < list_tmp[j]["BatSkill"]:
      k=j
      j+=1
    elif list_tmp[k]["BatSkill"] > list_tmp[j]["BatSkill"]:
      j+=1
    else:
      if list_tmp[k]["BowlSkill"] < list_tmp[j]["BowlSkill"]:
        k=j
        j+=1
      elif list_tmp[k]["BowlSkill"] > list_tmp[j]["BowlSkill"]:
        j+=1
      else:
        break
  tmp_list.append(list_tmp[k])
  final_list.append((list_tmp[k]["Name"],list_tmp[k]["Role"]))
  list_tmp.remove(list_tmp[k])
  k,j=0,0
  if len(tmp_list) == 2:
    break
#print("\nThe final TopOrder's list:",tmp_list)

list_tmp,tmp_list =[],[]
for i in range(0,len(list)):
  if list[i]["Role"] == "MiddleOrder":
    list_tmp.append(list[i])
#print("The full list of MiddleOrder:",list_tmp)
k,j=0,0
while(k<len(list_tmp)):
  while(j<len(list_tmp)):
    if k==j:
      j+=1
    elif list_tmp[k]["BatSkill"] < list_tmp[j]["BatSkill"]:
      k=j
      j+=1
    elif list_tmp[k]["BatSkill"] > list_tmp[j]["BatSkill"]:
      j+=1
    else:
      if list_tmp[k]["BowlSkill"] < list_tmp[j]["BowlSkill"]:
        k=j
        j+=1
      elif list_tmp[k]["BowlSkill"] > list_tmp[j]["BowlSkill"]:
        j+=1
      else:
        break
  tmp_list.append(list_tmp[k])
  final_list.append((list_tmp[k]["Name"],list_tmp[k]["Role"]))
  list_tmp.remove(list_tmp[k])
  k,j=0,0
  if len(tmp_list) == 2:
    break
#print("\nThe final MiddleOrder's list:",tmp_list)

list_tmp,tmp_list =[],[]
for i in range(0,len(list)):
  if list[i]["Role"] == "AllRounder":
    list_tmp.append(list[i])
#print("The full list of AllRounder:",list_tmp)
k,j=0,0
while(k<len(list_tmp)):
  while(j<len(list_tmp)):
    if k==j:
      j+=1
    elif (list_tmp[k]["BatSkill"]+list_tmp[k]["BowlSkill"])/2 < (list_tmp[j]["BatSkill"]+list_tmp[j]["BowlSkill"])/2:
      k=j
      j+=1
    elif (list_tmp[k]["BatSkill"]+list_tmp[k]["BowlSkill"])/2 > (list_tmp[j]["BatSkill"]+list_tmp[j]["BowlSkill"])/2:
      j+=1
    else:
      break
  tmp_list.append(list_tmp[k])
  final_list.append((list_tmp[k]["Name"],list_tmp[k]["Role"]))
  list_tmp.remove(list_tmp[k])
  k,j=0,0
  if len(tmp_list) == 1:
    break
#print("\nThe final AllRounder's list:",tmp_list)

list_tmp,tmp_list =[],[]
for i in range(0,len(list)):
  if list[i]["Role"] == "WK":
    list_tmp.append(list[i])
#print("The full list of WK:",list_tmp)
k,j=0,0
while(k<len(list_tmp)):
  while(j<len(list_tmp)):
    if k==j:
      j+=1
    elif list_tmp[k]["BatSkill"] < list_tmp[j]["BatSkill"]:
      k=j
      j+=1
    elif list_tmp[k]["BatSkill"] > list_tmp[j]["BatSkill"]:
      j+=1
    else:
      break
  tmp_list.append(list_tmp[k])
  final_list.append((list_tmp[k]["Name"],list_tmp[k]["Role"]))
  list_tmp.remove(list_tmp[k])
  k,j=0,0
  if len(tmp_list) == 1:
    break
#print("\nThe final WK's list:",tmp_list)

list_tmp,tmp_list =[],[]
for i in range(0,len(list)):
  if list[i]["Role"] == "Bowler":
    list_tmp.append(list[i])
#print("The full list of bowlers:",list_tmp)
k,j=0,0
while(k<len(list_tmp)):
  while(j<len(list_tmp)):
    if k==j:
      j+=1
    elif list_tmp[k]["BowlSkill"] < list_tmp[j]["BowlSkill"]:
      k=j
      j+=1
    elif list_tmp[k]["BowlSkill"] > list_tmp[j]["BowlSkill"]:
      j+=1
    else:
      if list_tmp[k]["BatSkill"] < list_tmp[j]["BatSkill"]:
        k=j
        j+=1
      elif list_tmp[k]["BatSkill"] > list_tmp[j]["BatSkill"]:
        j+=1
      else:
        break
  tmp_list.append(list_tmp[k])
  final_list.append((list_tmp[k]["Name"],list_tmp[k]["Role"]))
  list_tmp.remove(list_tmp[k])
  k,j=0,0
  if len(tmp_list) == 3:
    break
#print("\nThe final bowler's list:",tmp_list)

print("The Final List:",final_list)

  
  


    
