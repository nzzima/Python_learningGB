import re

def output_result(input_result):
    for match in input_result:
        print(match.split(';'))
            
                
n = int(input("Enter count of matches: "))
input_result = []
for match in range(n):
    input_string = input("Enter match like < First_com;count_gols;Second_com;count_gols > --> ")
    input_result.append(input_string)
    
output_result(input_result)