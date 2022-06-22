weight = input("Weight: ")
option = input('(L)bs or (K)g: ')

if option == 'l' or option == "L":
    print((int(weight) / 0.45) , 'pounds')

elif option == 'k' or option == 'K':
    print((int(weight) * 0.45),'kg')
    
else:
    print("You enter wrong option")