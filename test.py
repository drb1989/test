for i in range(1,101):
    
    if i%15 == 0:
        print('FuzzBuzz\n')
        continue
    
    if i%5 == 0:
        print('Buzz\n')
        continue
    
    if i%3 == 0:
        print('Fuzz\n')
        continue
    
    print(i)

