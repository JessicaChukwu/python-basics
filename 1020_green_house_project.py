from engi1020.arduino.api import *
from time import sleep
import matplotlib.pyplot as plt


# Function to save readings to a file
def save_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(','.join(map(str, data)) + '\n')

# Function to plot readings
def plot_readings(filename):
    data = {'Light': [], 'Temperature': [], 'Pressure': []}

    with open(filename, 'r') as file:
        for line in file:
            values = list(map(float, line.strip().split(',')))
            data['Light'].append(values[0])
            data['Temperature'].append(values[1])
            data['Pressure'].append(values[2])

    plt.figure(figsize=(10, 6))
    plt.plot(data['Light'], label='Light')
    plt.plot(data['Temperature'], label='Temperature')
    plt.plot(data['Pressure'], label='Pressure')
    plt.xlabel('Time (Iterations)')
    plt.ylabel('Readings')
    plt.title('Condition Readings Over Time')
    plt.legend()
    plt.show()

#getting condition readings
def light_monitor(pin,time,samples=6):
    """ This function reads samples from the chosen analog pin, for a certain time interval and returns our light data readings in a list """
    
    light=[]
    
    for i in range (samples):
        light_read = analog_read(pin)
        light.append(light_read)
        sleep(time)
       
    return light
print(f" 1). Light_read={light_monitor(6,1, 6)}")
x= light_monitor(6,1, 6)
    
def temp_monitor(pin,time,samples):
    """ This function reads samples from the chosen analog pin, for a certain time interval and returns our light data readings in a list """
    
    temp=[]
    
    for i in range (samples):
        temp_read = pressure_get_temp()
        temp.append(temp_read)
        sleep(time)
        
    return temp
print(f" 2). Temp_read={temp_monitor(6,1,10)}")
y=temp_monitor(6,1,10)
   

def pressure_monitor(time,samples):
    """ This function reads samples from the chosen analog pin, for a certain time interval and returns our light data readings in a list """
    voltageat0psi= 0.5
    voltageat100psi= 4.5
    
    pressureread=[]
     
    for i in range (samples):
        sensorvoltage= pressure_get_pressure()*(5.0/1023.0)
        pressure= (sensorvoltage - voltageat0psi) / (voltageat100psi - voltageat0psi) * 100.0
        pressureread.append(pressure)
        sleep(time)
        
    return pressureread
print(f" 3). Pressure_read={pressure_monitor(1,10)}")
z= pressure_monitor(1,10)

#assigning optimum conditions
oplight= list(range(350,370))
optemp= 18 #in degree celcius
oppressure = 15 #in psi
lcd_color_set= False #to check if the rgblcd clor has been set
iteration =0

while True:
    
    if not lcd_color_set:
        rgb_lcd_colour(0,255,0)
#checking light conditions        
    averagelight= sum(x)/ len(x)
    for i in oplight:
        if averagelight < i:
            buzzer_frequency(5,500)
            digital_write(4,True)
            rgb_lcd_colour(0,255,0) #green
            lcd_color_set= True
            oled_print('OPEN DOORS OR WINDOW!')
            print('OPEN DOORS OR WINDOW!')
            sleep (1)
            break
        elif averagelight > i:
            buzzer_frequency(5,500)
            digital_write(4,True)
            rgb_lcd_colour(0,255,0) #green
            lcd_color_set= True
            oled_print('CLOSE DOORS OR WINDOW!')
            sleep (1)
            print('CLOSE DOORS OR WINDOW!')
            break
        else:
            oled_print('light is perfect')
            print('light is perfect')


#checking temperature
    averagetemp= sum(y)/ len(y)

    if averagetemp < optemp:
        buzzer_frequency(5,1000)
        digital_write(4,True)
        rgb_lcd_colour(255,255,0) #yellow
        lcd_color_set= True
        oled_print('Temperature is low')
        sleep (1)
        print('Temperature is low')
  
    elif averagetemp > optemp:
        buzzer_frequency(5,1000)
        digital_write(4,True)
        rgb_lcd_colour(255,255,0) #yellow
        lcd_color_set= True
        oled_print('Temperature is high')
        sleep (1)
        print('Temperature is high')
  
    else:
        oled_print("Temp is perfect")
        sleep (1)
        print("Temperature is perfect")
    
#checking pressure
    averagepressure= sum(z)/ len(z)

    if averagepressure < oppressure:
        buzzer_frequency(5,500)
        digital_write(4,True)
        rgb_lcd_colour(255,0,0) #red
        lcd_color_set= True
        oled_print('Pressure is low')
        print('Pressure is low')
    
    elif averagepressure > oppressure:
        buzzer_frequency(5,500)
        digital_write(4,True)
        rgb_lcd_colour(255,0,0) #red
        lcd_color_set= True
        oled_print('Pressure is high')
        print('Pressure is high')
    
    else:
        oled_print('Pressure is perfect')
        print('Pressure is perfect')
        lcd_color_set= False
        
        
        
    button= digital_read(6)
    
    if button ==True:
        buzzer_stop(5)
        digital_write(4,False)
        break
    
    
    current_readings = [averagelight, averagetemp, averagepressure]
    save_to_file('condition_readings.csv', current_readings)
    
    " " " the save_to_file function calls bot the conditipn_readings.csv as well as the current_readings " " "
    
    
     # Plot readings
    if iteration % 5 == 0:  # Plot every 5 iterations
        plot_readings('condition_readings.csv')

    iteration += 1
    
