racer_name=input("Input the racer's name: ")
racer_number=input("Input the racer's number: ")
position=int(input("Input the racer's placement in the qualifier: "))
if position%3<1.5:
    row=int((21-position)//3+1)
else:
    row=int((21-position)//3)
if position%3==0:
    row_position=1
elif position%3==2:
    row_position=2
else:
    row_position=3
if row==1 and row_position==1:
    print(racer_name+'(number '+racer_number+') starts in the pole position.')
else:
    print(racer_name+'(number '+racer_number+') starts in row '+str(row)+', column '+str(row_position))