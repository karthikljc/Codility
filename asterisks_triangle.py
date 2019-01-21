import sys

print('Asterisk Triangle')
n = int(sys.argv[1])
for i in range(1,n+1):
  stars = ''
  for j in range(1,i):
    stars = stars + '*'
  print(stars)

