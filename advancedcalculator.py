import re
print('magical calculator')
print('type quit to exit')
previous=0
run=True
def performMath():
    global run
    global previous
    equation=""
    if(previous==0):
        equation=input('enter equation:')
    else:
        equation=input(str(previous))
    if equation=='quit':
        print('goodbye')
        run=False
    else:
       equation=re.sub('[a-zA-Z,.:()" "]','',equation)
       if previous==0:
        previous=eval(equation)
       else:
           previous=eval(str(previous)+equation)

while run:
    performMath()