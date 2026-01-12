import time

# Get current hour in 24-hour format
hour = int(time.strftime("%H"))

# Print current time (optional)
print("Current Hour:", hour)

# Greeting based on time
if hour < 12:
    print("Good Morning Sir 🌅")

elif hour < 17:
    print("Good Afternoon Sir ☀️")

else:
    print("Good Evening Sir 🌙")
