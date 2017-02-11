print("hello")

import re

str_strt = "^"
str_end = "$"

mat_any = "."
mat_times_01 = "?"
mat_times_1P = "+"
mat_all = "*"

conv_esc = "\ "



print(re.split(r'\s*','here are some words!'))

print(re.split(r'(\s*)','here are some words!'))

print(re.split(r'(s*)','here are some words!'))

print(re.split(r'[a-f]','rsedfhjtujFGHDHSRTHFKGHJLUOLSADyujyikd6gghedftg'))

print(re.split(r'[a-fA-F0-9p-qs]','rsedfhjtujFGHDHSRTHFKGHJLUOLSADyujyikd6gghedftg', re.I, re.M))

print(re.split(r'[a-f][a-f]','rsedfhjtujFcdGHDHSRTHFKGHJLUOLSADyujyikd6gghedftg', re.I, re.M))

print(re.findall(r'\d','ocenia 234 sasd3267 hal 32'))

print(re.findall(r'\d{1,5}','ocenia 234 8986978967 678678 sasd3267 hal 32'))

print(re.findall(r'\d{1,5}\s\w+\s\w+\.','ocenia  234sd assfart2323 8986978967 678678 sasd3267 hal 32'))




