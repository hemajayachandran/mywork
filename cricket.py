class CricketTeam:
	def total_players(list,role):
		rolewise_list =[]
		for player in range(0,len(list)):
			if list[player]["Role"] == role:
				rolewise_list.append(list[player])
		return rolewise_list
				
	def batsmen(list,role,number):
		total_batsmen=CricketTeam.total_players(list,role)
		best_batsmen = []
		total_players = []
		outer_index,inner_index = 0,0
		while outer_index < len(total_batsmen):
			while inner_index < len(total_batsmen):
				if outer_index == inner_index:
					inner_index+=1
				elif total_batsmen[outer_index]["BatSkill"] > total_batsmen[inner_index]["BatSkill"]:
					inner_index+=1
				elif total_batsmen[outer_index]["BatSkill"] < total_batsmen[inner_index]["BatSkill"]:
					outer_index = inner_index
					inner_index+=1
				else:
					if total_batsmen[outer_index]["BowlSkill"] > total_batsmen[inner_index]["BowlSkill"]:
						inner_index+=1
					elif total_batsmen[outer_index]["BowlSkill"] < total_batsmen[inner_index]["BowlSkill"]:
						outer_index = inner_index
						inner_index+=1
					else:
						break
			if len(best_batsmen) == number:
				break
			best_batsmen.append(total_batsmen[outer_index])
			total_players.append((total_batsmen[outer_index]["Name"],total_batsmen[outer_index]["Role"]))
			total_batsmen.remove(total_batsmen[outer_index])
			outer_index,inner_index = 0,0
		return total_players	
				
	def players(list):
		final,final_list = [],[]
		final_list=CricketTeam.batsmen(list,"Opener",2)
		final.append(final_list)
		final_list=CricketTeam.batsmen(list,"TopOrder",2)
		final.append(final_list)
		final_list=CricketTeam.batsmen(list,"MiddleOrder",2)
		final.append(final_list)
		return final

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
team = CricketTeam()
print(CricketTeam.players(list))
