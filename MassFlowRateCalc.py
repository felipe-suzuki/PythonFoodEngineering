# This program can calculate the inlet/outlet of a liquid that will suffer 
# the process of concentration through evaporation.

# The user should enter the soluble solids content of the inlet, the mass flow rate of water 
# removed by evaporation, and the soluble solids content of the final concentrated outlet product.

# CLASSES AND FUNCTIONS:

class MassFlow:
    # m = mass flow rate in kg/h
    # xs = mass fraction of soluble solids in decimals, xw = mass fraction of water in decimals
    def __init__(self, m, xs, xw):
        self.m = m
        self.xs = xs
        self.xw = xw
    
def getInXS():
    x = 0
    # I did choose the lower and upper limit for the initial soluble solids content.
    while x < 0.10 or x > 0.25:
        try:
            x = float(input('Please insert the initial soluble solids content, ranging from 0.10 to 0.25! \nYour entry: '))
        except:
            print('Please insert a valid value')
    return x

def getOutXS():
    y = 0
    # I did choose the lower and upper limit for the final soluble solids content.
    while y < 0.25 or y > 0.65:
        try:
            y = float(input('Please insert the final soluble solids content, ranging from 0.25 to 0.65! \nYour entry: '))
        except:
            print('Please insert a valid value')
    return y

def get_mWater():
    z = 0
    while z <= 0:
        try:
            z = float(input('Please insert the mass flow rate (kg/h) of the water removed by evaporation. \nYour entry: '))
        except:
            print('Please insert a valid value')
    return z

def run_again():
    
    return input('\nDo you want to calculate again? Enter Yes or No: ').lower().startswith('y')


#----------- SCRIPT -----------#

while True:
    
    print('\nWelcome to the Mass Flow Rate Calculator')
    
    # Get the inlet total soluble solids content
    inlet = MassFlow(0, getInXS(), 0)
    inlet.xw = 1 - inlet.xs
    
    # Get the outlet total soluble solids content
    outlet = MassFlow(0, getOutXS(), 0)
    outlet.xw = 1 - outlet.xs
    
    # Get the mass flow rate of water removed by evaporation
    mw = MassFlow(get_mWater(), 0, 1)
    
    # Calculate the mass flow rate of the inlet and outlet
    inlet.m = (mw.m)/((inlet.xw) - ((outlet.xw)*((inlet.xs)/(outlet.xs))))
    outlet.m = inlet.m - mw.m
    
    #Return the answer to the problem
    print('\nTo concentrate a liquid with total soluble solids content of {} entering \
the system at a mass flow rate of {:.2f} kg/h, you will get a water outlet of {} kg/h \
and a concentrated liquid with total soluble solids content of {} at a mass flow \
rate of {:.2f} kg/h'.format(inlet.xs, inlet.m, mw.m, outlet.xs, outlet.m))
       
    # If run_again = False, stop. If True, restart the script
    if not run_again():
        break