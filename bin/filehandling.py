import os
with open(r'C:\pkk8199\Cognizant\Linked in Summary.txt') as f:
    print(*f.readlines())
print(os.listdir(r'C:\pkk8199\Cognizant'))
print(os.getenv('PATH'))
