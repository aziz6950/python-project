import random

subjects = [
    
    "Nurul Aziz Sohel",
    "Shakib Khan",
    "Litton Das",
    "A group of model",
    "A little girl",
    "Truck driver bai",
    "Dr. yunus ",
]

actions = [
    "reads",
    "acting",
    "stop working",
    "run",
    "advice",
    "order",
    "enjoying",
]

places_or_things =[
    "in black building",
    "in Sylhet city",
    "a plate of kacci",
    "at working office",
    "in house",
    "after footbal match",
    "before cricket match",
]
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    
    user_input= input("\nDo you want another headline? (yes/no):"). strip().lower()
    if user_input == "no":
          break
      
      
print("\nThanks for using the Fake News Headline Generator. Have a fun day")