############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
#_________________________________________________________________________________________________________________________
sick = 1
y = "yes"
n = "no"

while(sick == 1):

    print "-------------------------------------------------------------------------------------------"
    print "Hello there! Lets take your temperature! Type only the number of your temperature."

    userTemp = int(raw_input())

    print "Your temperature is " + str(userTemp) + " degrees fahrenheit."
    print "Have you been sick within the last 24 hours? Type only yes or no."

    areYouSick = raw_input()

    print "Have you recently travelled to West Africa? Type only yes or no."

    recentTravel = raw_input()

    if userTemp > 105:
        sick = 1

    if userTemp < 106:
        if userTemp > 99:
            if areYouSick == "n":
                sick = 0
                
    if recentTravel == "y":
        if temp > 99:
            sick = 1
        if areYouSick == "y":
            sick = 1    

    if sick == 1:
        print 'You have the disease!'
        
print 'You don\'t have it.'