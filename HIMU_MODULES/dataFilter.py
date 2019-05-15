def filtFood(userVoice):
    pizza     = ['pizza', 'piz', 'lisa', 'visa']
    sandwitch = ['sandwitch']
    burger    = ['burger']
    gb        = ['garlic bread', 'garlic' , 'bread', 'bred']
    pasta     = ['pasta']    
    
    finalItem = "Not Found!"
    
    if any(word in userVoice for word in pizza):
        finalItem = "Pizza"
    elif any(word in userVoice for word in sandwitch):
        finalItem = "Sandwitch"
    elif any(word in userVoice for word in burger):
        finalItem = "Burger"
    elif any(word in userVoice for word in gb):
        finalItem = "Garlic bread"
    elif any(word in userVoice for word in pasta):
        finalItem = "Pasta"        
    else:
        print("Which item you want?")
        finalItem = "Did't get!"    
    return finalItem

def filtExtra(userVoice):
    cheese  = ['cheese', 'chiz']
    water   = ['water']
    toping  = ['toping']
    
    finalExtra = "Not Found!"
    
    if any(word in userVoice for word in cheese):
        finalExtra = "Cheese"
    elif any(word in userVoice for word in water):
        finalExtra = "Water"
    elif any(word in userVoice for word in toping):
        finalExtra = "Toping"
    else:        
        finalExtra = "No Extra Item!"    
    return finalExtra


def filtNo(userVoice):
    no1  = ['1','one', 'on']
    no2  = ['2', 'two', 'to', 'tu']
    no3  = ['3', 'three','tree']
    no4  = ['4', 'four', 'for']
    no5  = ['5', 'fi', 'five']
    no6  = ['6', 'six']
    no7  = ['7', 'saven', 'seven']
    no8  = ['8', 'eight']
    no9  = ['9', 'nine']
    no10 = ['10', 'ten']

    finalNO = 0
    
    if any(word in userVoice for word in no1):
        finalNo = 1
    elif any(word in userVoice for word in no2):
        finalNo = 2
    elif any(word in userVoice for word in no3):
        finalNo = 3
    elif any(word in userVoice for word in no4):
        finalNo = 4
    elif any(word in userVoice for word in no5):
        finalNo = 5
    elif any(word in userVoice for word in no6):
        finalNo = 6
    elif any(word in userVoice for word in no7):
        finalNo = 7
    elif any(word in userVoice for word in no8):
        finalNo = 8
    elif any(word in userVoice for word in no9):
        finalNo = 9
    elif any(word in userVoice for word in no10):
        finalNo = 10
    else:
        print("How much you want?")
        finalNo = 0    
    return finalNo

	


