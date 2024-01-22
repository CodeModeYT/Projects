from datetime import datetime, timedelta

def calculate_time(start_time):
    start_datetime = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    return start_datetime

def main():
    start_time = '2024-01-22 10:42:03'

    with open('D:\Projekte\Python\WheatherStation_DataValidation\Data\Ecke_Fenster-offen.TXT', 'r') as file:
        lines = file.readlines()

    sensed_time = calculate_time(start_time)
    humidity = None

    for i in range(0, len(lines)):
        line = lines[i].strip()
        
        if "Humidity" in line:
            humidity = line.split(': ')[1]
        elif "Temperature" in line and humidity is not None:
            temperature = line.split(': ')[1]
            
            print(f"Sensed Time: {sensed_time}, Humidity: {humidity}, Temperature: {temperature}")

            sensed_time += timedelta(seconds=1)
            humidity = None

if __name__ == "__main__":
    main()
