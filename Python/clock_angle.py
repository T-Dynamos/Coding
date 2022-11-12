time = "4:30" #input("Enter the time = ")

hour = int(time.split(":")[0])
mm = int(time.split(":")[-1])

def get_angle(hour: int, minute: int) -> int:
    hour_angel = (hour if hour <= 12 else hour - 12) * 30
    minute_angle = minute * 6
    angle = abs(hour_angel - minute_angle)
    if angle > 180:
        angle = 360 - angle
    return angle


print(get_angle(hour, mm), "degree")
