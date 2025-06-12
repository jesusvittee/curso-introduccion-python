# sintaxis del ciclo

# if
if True:
    print('se ejecuto')
"""  
#while
while True:
    print('se ejecuto')
"""
"""
#Ctrl + c para cancelar ejecucion  
counter = 0
 
while counter < 10:
 counter += 1
 print(counter)
"""
"""
#Romper el ciclo
counter = 0
while counter < 20:
   counter +=1
   if counter == 15:
    break # rope con la funcion o el problea no importando si cumplió con la operacion 
   print(counter)
"""
counter = 0
while counter < 20:
    counter += 1
    if counter <15:
        continue  
    print(counter)   
    
    #break... if counter == 5