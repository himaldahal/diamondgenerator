print('Type q to quit.')
while True:
 inp = input("Please input side length of diamond: ").lower()
 if inp == 'q':
     print('Thanks for using diamond generator')
     break
 else:
    side = int(inp)
    for x in list(range(side)) + list(reversed(range(side-1))):
       print('{: <{width1}}{:*<{width2}}'.format('', '', width1=side-x-1,width2=x*2+1))
