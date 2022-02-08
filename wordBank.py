import random


listOf4Letter = {"Hard", "Ship", "Game", "Week", "June", "fart", "poop", "Wall", "Hole", "Nail", 
"Star", "Jeff", "Ring", "Tree", "Ball", "Ammo", "Four", "Fire", "Girl", "Jazz", "File", "Dart", "Page", 
"Sock", "Hate", "Four", "Five", "Main", "Link", "Ammo", "Band", "Case", "Shoe" }
#print(listOf4Letter)

listOf5Letter = {"Apple","Alone","Beach","Beams","Clock","China","Cream", "Dream","Drive", 
"Earth","Enemy","Error","Final","Force","Glass","Guide","Heart","Horse","Image","Index","Japan",
"Judge","Knife","Level","Light","Major","Metal","Music","Night","North","Offer","Order","Peace","Price",
"Peach","Queen","Radio","River","Scene","Shock","Space","Sugar","Theme","Trust","Union","Unity","Value",
"Video","Waste","Watch","Youth","Zebra"}
#print(listOf5Letter)


listO6Letter = {"Bottle", "Letter", "Bridge", "Outlet", "Puzzle", "Hijack", "Backup", "Jungle", 
"Injury", "Jewish", "Mother", "Squirm", "Wizard", "Zodiac", "Jetlag", "Quarry", "Webcam", "Blowup", "Liquor", "Wacked"  }
#print(listO6Letter)

def getListOffDifficulty(diffi):
    if(diffi == "easy"):
        return listOf4Letter
    if(diffi == "medium"):
        return listOf5Letter
    if(diffi == "hard"):
        return listO6Letter

def getRandomWord(dict):
    listOfWords = list(dict)
    randomWord = random.choice(listOfWords)
    print(randomWord + "!!!!!!!!!!!!!!!!!!!!!")
    return randomWord
