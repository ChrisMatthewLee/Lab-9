############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer
#----------------------------------------------------------------------


#ask
print "Put in the amount of degrees celcius that you would like to convert to fahrenheit"

#define variable
cel = int(raw_input())

#calculate
def fahcalc(cel):
    fah = cel * 9
    fah = fah / 5
    fah = fah + 32
    return fah
    
#Give answer
print "It is " + str(fahcalc(cel)) + " degrees fahrenheit."