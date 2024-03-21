from engi1020.arduino.api import *
from time import sleep

# Function to get distance from the Ultrasonic Ranger
def get_distance():
	return ultra_get_centimeters(7)

"""This whole code will alert the user and any other nearby vehicles about potential accidents due to objects or vehicles in close proximity"""
"""It will also let the driver know if the ambient light conditions are suitable for driving or not."""

threshold_light = 600  # Adjust the light sensor threshold as needed
lcd_color_set = False  # Flag to track if the RGB LCD color has been set

while True:
	# Read data from the proximity sensor
	x = get_distance()
	print(f'{x} cm, no object is in close proximity')
	oled_message = f'{x} cm, no object is in close proximity'
   

	# Set the initial color to green only if it hasn't been set yet
	if not lcd_color_set:
    	rgb_lcd_colour(0, 255, 0)  # Set initial color to green
    	digital_write(4, False)
    	digital_write(4, True)
    	lcd_color_set = True  # Set the flag to indicate the color has been set

	# Wait for a short duration to avoid excessive updates
	sleep(0.5)

	# Check distance conditions and update the display and RGB LCD accordingly
	if x <= 200 and x > 50:
    	oled_message = f'{x} cm, an object is in close proximity, Take caution!'
    	oled_print(oled_message)  # Print the message for the OLED display
    	print(f'{x} cm, an object is in close proximity, Take caution!')
    	rgb_lcd_colour(255, 255, 0)  # Yellow
    	digital_write(4, False)
    	buzzer_frequency(5, 500)
    	sleep(1)
    	buzzer_stop(5)
    	digital_write(4, True)
    	lcd_color_set = True  # Set the flag to indicate the color has been set for this condition
 	 
	elif x <= 50:
    	oled_message = f'{x} cm, Vehicle will crash, brace for impact!'
    	print(f'{x} cm, Vehicle will crash, brace for impact!')
    	rgb_lcd_colour(255, 0, 0)  # Red
    	digital_write(5, True)
    	buzzer_frequency(5, 1000)
    	sleep(0.5)
    	buzzer_stop(5)
    	digital_write(5, False)
    	lcd_color_set = True  # Set the flag to indicate the color has been set for this condition

	else:
    	# Reset the color to green only if the previous condition was not triggered
    	rgb_lcd_colour(0, 255, 0)  # Set color back to green
    	digital_write(4, False)
    	digital_write(4, True)
    	lcd_color_set = False  # Reset the flag since the color has been reset to green

	# Read data from the light sensor
	light_value = analog_read(6)

	# Check light sensor conditions and update the display accordingly
	if light_value > threshold_light:
    	print('Sunlight is bright, visibility of the road will not be affected')
    	digital_write(2, False)  # Turn off the LED when sunlight is bright
   	 
	elif 600 >= light_value > 400:
    	print('Sunlight is dim, manually turn on light if visibility is poor')
    	if digital_read(6) == True:
        	digital_write(2, True)
    	else:
        	digital_write(2, False)
	else:
    	print("It's Night time, Lights would be put on automatically except you turn it off ")
    	if digital_read(6) == True:
        	digital_write(2, True)
    	else:
        	digital_write(2, True)







