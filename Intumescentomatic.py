#Python 3.7.2
#Intumescentomatic

print('Input intumescent material:');

intMat = input();

print('Input intumescent position:');

intPos = input();

print ('How many interruptions are there? ');

intBool = input(int);

intFinal = '';

for i in range(int(intBool)):
        print ('Where is intumescent interrupted?')
        intWhere = input();
        print ('What is the remaining percentage?')
        intRem = input();
        if intRem == '0':
            intomatic = ('Fully interrupted by '+intWhere + '. ')
        else:
            intomatic = ('Partially interrupted by '+intWhere + ' with ' + intRem + '% remaining. ')
        intFinal = intFinal + intomatic

print ('A ' + intMat + ' based intumescent set ' + intPos + ' from hinge knuckle face. ' + intFinal)  

        
##while intBool != 'No':
##    intBool = input();
##
##    if intBool == 'Yes':
##        print ('Where is intumescent interrupted?')
##        intWhere = input();
##        print ('What is the remaining percentage?')
##        intRem = input();
##    elif intBool == 'No':
##        print ('A ' + intMat + ' based intumescent set ' + intPos + ' from hinge knuckle face')    
##    else:
##        print('Please enter \'Yes\' or \'No\'')


