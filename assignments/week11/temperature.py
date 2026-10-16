def get_temperature():
    temp = [36, 56, 43, 41, 40, 39, 37]
    return temp

def analyze_temps(temp):
    avg = sum(temp) / 7
    high = max(temp)
    low = min(temp)

    return (avg, high, low)

def display(avg, high, low):
    print(f"Average: {avg:.1f}")
    print(f"Highest: {high:.1f}")
    print(f"Lowest: {low:.1f}")

temp = get_temperature()
# avg, high, low = analyze_temps(temp)
ana = analyze_temps(temp)
display(ana[0], ana[1], ana[2])