<<<<<<< HEAD
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
=======
"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
    
>>>>>>> upstream/main
