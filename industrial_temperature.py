temperatures = {
    "sensor_A": 79.0,
    "sensor_B": 81.2,
    "sensor_C": 75.4,
    "sensor_D": 85.7
}

def trigger_alarm(temperatures, threshold=80):
    limitless = []
    for sensor, value in temperatures.items():
        if value > threshold:
            limitless.append(sensor)
    return limitless

print(trigger_alarm(temperatures))