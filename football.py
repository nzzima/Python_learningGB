def Get_team_index(data, team):
    for index in range(len(data)):
        if team == data[index]: return index
        else: continue

def sum_points(output_res, team_index, match_result):
    if match_result == 'win':
        output_res[team_index + 1] += 1
        output_res[team_index + 2] += 1
        output_res[team_index + 3] += 0
        output_res[team_index + 4] += 0
        output_res[team_index + 5] += 3
    elif match_result == 'lose':
        output_res[team_index + 1] += 1
        output_res[team_index + 2] += 0
        output_res[team_index + 3] += 0
        output_res[team_index + 4] += 1
        output_res[team_index + 5] += 0
    elif match_result == 'no_one':
        output_res[team_index + 1] += 1
        output_res[team_index + 2] += 0
        output_res[team_index + 3] += 1
        output_res[team_index + 4] += 0
        output_res[team_index + 5] += 1
        
def create_output_result(data):
    teams = []
    match_stats = []
    output_result = []
    for match in data:
        teams_and_goals = match.split(";")
        if teams_and_goals[1] > teams_and_goals[3]:
            if teams_and_goals[0] not in teams:
                match_stats += teams_and_goals[0], 1, 1, 0, 0, 3
                output_result  += match_stats
                match_stats.clear()
                teams.append(teams_and_goals[0])
            else:
                team_ind = Get_team_index(output_result, teams_and_goals[0])
                sum_points(output_result, team_ind, 'win')
                
            if teams_and_goals[2] not in teams:
                match_stats += teams_and_goals[2], 1, 0, 0, 1, 0
                output_result += match_stats
                match_stats.clear()
                teams.append(teams_and_goals[2])
            else:
                team_ind = Get_team_index(output_result, teams_and_goals[2])
                sum_points(output_result, team_ind, 'lose')
                
        elif teams_and_goals[1] < teams_and_goals[3]:
            if teams_and_goals[0] not in teams:
                match_stats += teams_and_goals[0], 1, 0, 0, 1, 0
                output_result  += match_stats
                match_stats.clear()
                teams.append(teams_and_goals[0])
            else:
                team_ind = Get_team_index(output_result, teams_and_goals[0])
                sum_points(output_result, team_ind, 'lose')
                
            if teams_and_goals[2] not in teams:
                match_stats += teams_and_goals[2], 1, 1, 0, 0, 3
                output_result += match_stats
                match_stats.clear()
                teams.append(teams_and_goals[2])
            else:
                team_ind = Get_team_index(output_result, teams_and_goals[2])
                sum_points(output_result, team_ind, 'win')
        
        else:
            if teams_and_goals[0] not in teams:
                match_stats += teams_and_goals[0], 1, 0, 1, 0, 1
                output_result  += match_stats
                match_stats.clear()
                teams.append(teams_and_goals[0])
            else:
                team_ind = Get_team_index(output_result, teams_and_goals[0])
                sum_points(output_result, team_ind, 'no_one')
                
            if teams_and_goals[2] not in teams:
                match_stats += teams_and_goals[2], 1, 0, 1, 0, 1
                output_result += match_stats
                match_stats.clear()
                teams.append(teams_and_goals[2])
            else:
                team_ind = Get_team_index(output_result, teams_and_goals[2])
                sum_points(output_result, team_ind, 'no_one')
                
    print(output_result)
    print(teams)

macthes_count = int(input("Enter count of matches: "))
input_result = []
for _ in range(macthes_count):
    match = input("Enter match like |Team;gole_score_per_match;Team;gole_score_per_match| --> ")
    input_result.append(match)

create_output_result(input_result)