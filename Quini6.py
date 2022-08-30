# ------------------- QUINI6 -------------------
# choose a random element from a list
from random import choice
import time
import keyboard 
key = True

while key:
    print('\n\t\t\t\tPisteando como campeones al premio mayor')
    time.sleep(2)
    print('\n')
    print('Awantiiaaaaaa que estamos preparando el bolillero para que VOS seas el nuevo millonario!')
    time.sleep(3)
    
    # prepare a sequence between 0 an 45 (inclusive)
    sequence = [i for i in range(46)]

    #List for each modality
    num_tradicional = []
    num_segunda = []
    num_revancha = []
    num_siempresale = []

    # make choices from the sequence
    while len(num_tradicional)<6:
        azar = choice(sequence)        
        if azar not in num_tradicional:         
            num_tradicional.append(azar)  
        #print(f'{len(num_tradicional)} y {azar}')
    num_tradicional.sort()#minor to mayor

    #make choices from the sequence
    while len(num_segunda)<6:       
        azar = choice(sequence) 
        if azar not in num_segunda:
            num_segunda.append(azar)    
    num_segunda.sort() 

    #make choices from the sequence
    while len(num_revancha)<6: 
        azar = choice(sequence)
        if azar not in num_revancha:    
            num_revancha.append(azar)
    num_revancha.sort() #minor to mayor
     
    #make choices from the sequence
    while len(num_siempresale)<6:    
        azar = choice(sequence) 
        if azar not in num_siempresale:    
            num_siempresale.append(azar)
    num_siempresale.sort() #minor to mayor
    time.sleep(1)
    # Print on screen    
    print('\nLos números sooooooon...!')
    print('DECILE ENZO!! DECILO!!\n')
    time.sleep(2)
    print(f"Nº para la Tradicional: {num_tradicional}")
    print(f"Nº para la 2º: {num_segunda}")
    print(f"Nº para la Revancha del Quini (Poverty counterattack): {num_revancha}")
    print(f"Nº que salen SI O SI perro: {num_siempresale}")
    print('\n')
    print('Muchisimos Éxitos! Y no te olvides: "El que come y no convida..."\n')  
    time.sleep(1)    
    print('Si querés probar suerte de nuevo, presiona ENTER.')
    print('Sino, ¿Qué estás esperando para apretar ESC y salir ya a jugartela?')

    if keyboard.read_key() == 'enter':
        continue
    else:
        key = False