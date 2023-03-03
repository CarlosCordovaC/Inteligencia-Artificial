x=0

while x <= 30:
    x += 1
    
    if x == 4 or x == 6 or x ==7:
        print('Se saltó el valor ', x ,' de x')
        continue
    
    if x ==15:
        print('Se rompió la ejecución del bucle cuando x valía ',x)
        break
    
  
    print(x)
    