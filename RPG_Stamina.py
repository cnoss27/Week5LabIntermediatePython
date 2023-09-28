import pandas as pd
import random as random

def StaminaChange(terrain): #define the StaminaChange function
    Changes = {"Forest" : random.randint(5 , 15), #for character in a forest add between 5 and 15 stamina
               "Mountain" : random.randint(-25 , -15), #for character in a mountain remove between 15 and 25 stamina
               "Swamp" : random.randint(-35 , -25), #for character in a swamp remove between 25 and 35 stamina
               "Village" : random.randint(10 , 20)} #for character in a village add between 10 and 20 stamina
    return Changes.get(terrain , 0)

CharacterInfo = {
    "CharacterName": ["Arwen", "Frodo", "Gimli", "Legolas"],
    "Terrain": ["Forest", "Mountain", "Swamp", "Village"],
    "InitialStamina": [100, 100, 100, 100],  # Assuming each character starts with 100 stamina
    "StaminaChange": [0, 0, 0, 0]
    } #enter initial character info

CharacterInfoDF = pd.DataFrame(CharacterInfo) #make the data into a dataframe

for x in range(0 , int(input("How many turns should be simulated? (Answer with an integer 1, 2, etc.):"))): #for inputted number of turns apply the changes and print the information

    CharacterInfoDF["StaminaChange"] = CharacterInfoDF["Terrain"].apply(StaminaChange) #applying stamina change

    CharacterInfoDF["NewStamina"] = CharacterInfoDF["InitialStamina"] + CharacterInfoDF["StaminaChange"] #Setting new stamina variable

    print("Here is the information for turn " , x+1 , ":") #indicating what turn this information is for

    print(CharacterInfoDF) #print the information

    CharacterInfoDF["InitialStamina"] = CharacterInfoDF["NewStamina"] #set InitialStamina equal to NewStamina to prep for next loop