
def ttip(tip, bill):
    tip = tip /100
    t= bill + bill * tip
    return ('your total with ' + str(tip) + '% tip is ' + str(t))

tip = int(input('enter tip percentage (10%,15%,20% or custom): '))
bill = float(input('enter bill as a float: '))
print(ttip(tip,bill))
