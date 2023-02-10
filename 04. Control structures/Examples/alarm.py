import time

# Define a counter and set to five
counter = 5

# As long as counter is not zero:
while counter != 0:

    print("Tick")
	
	# Decrement counter
    counter = counter - 1

    # Sleep for one second
    time.sleep(1)


# Make beep sound
print("Beep")
print('\a')