"""
Lists preserves the order - insertion order
"""

states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
                     "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
                     "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
                     "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
                     "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
                     "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
                     "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# Read List
print(states_of_america[0])
print(states_of_america[2])
the_state = states_of_america[5]
print(states_of_america[-1])

# Modify List
print(states_of_america[37])
states_of_america[37] = "Pencilvania"
print(states_of_america[37])

# Insert End of the List
states_of_america.append("State 51")
print(states_of_america[-1])

# Append a list
states_of_america.extend(["State 52", "State 53"])
print(states_of_america[-3:])

