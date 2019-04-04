details={

    'name':['Nikhil','Poonam'],
    'Department':['CSE','CSE'],
    'Marks':[[87,87,98],[98,96,96]]
}

for i in range( len(details['name'])):
    print details['name'][i] , 'from',details['Department'][i],'has obtained following marks', str(details['Marks'][i]) ,\
        'and total marks' , sum(details['Marks'][i]) ,'/300'
)
if sum(details['Marks'][0])>sum(details['Marks'][1]):
    print details['name'][0] , 'has topped the exam ' 
else:
    print details['name'][1], 'has topped the exam '
