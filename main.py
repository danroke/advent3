# regex module
import re

Total_sum = 0
matches_all = []

with open('input.txt', 'r') as file:
    for line in file:    

        pattern = r"mul\(\d{1,3},\d{1,3}\)"
        matches = re.findall(pattern, line)
        
        for match in matches:
            match_string = re.split(r",",match)
            x = re.split(r"\(",match_string[0])
            y = re.split(r"\)", match_string[1])
            result = int(x[1]) * int(y[0])
            Total_sum = Total_sum + result
        
    print("Total Sum:", Total_sum)