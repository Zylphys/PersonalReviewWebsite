# Create Episode Class
class Episode:
    def __init__(self, id, season, epNum, epName, pc, sc, appears, rating):
        self.id = id  # Incrementing id number
        self.season = season  # What season the episode is in
        self.epNum = epNum  # What number the in the season the episode is in
        self.epName = epName  # Name of the episode
        self.pc = pc  # List of primary characters of the episode using character class
        self.sc = sc  # List of Secondary Characters of the episode using character class
        self.appears = appears  # List of characters that appear in the episode, mix of string with just the name, and the character class
        self.rating = rating  # Rating I give to the episode
        self.displayed = True  # boolean to check if episode is displayed

    # Setter and Getter functions
    def getSeason(self):
        return self.season

    def setSeason(self, season):
        self.season = season

    def getEpnum(self):
        return self.epNum

    def setEpnum(self, epNum):
        self.epNum = epNum

    def getEpName(self):
        return self.epName

    def setEpName(self, epName):
        self.epName = epName

    def getPrimaryCharacter(self):
        return self.pc

    def setPrimaryCharacter(self, pc):
        self.pc = pc

    def getSecondaryCharacter(self):
        return self.sc

    def setSecondaryCharacter(self, sc):
        self.sc = sc

    def getAppears(self):
        return self.appears

    def setAppears(self, appears):
        self.appears = appears

    def getRating(self):
        return self.rating

    def setRating(self, rating):
        self.rating = rating


# Character class

class Character:
    def __init__(self, name, voiceActor, hexColor='#FFFFFF'):
        self.name = name
        self.voiceActor = voiceActor
        self.hexColor = hexColor

# Getter and Setter methods

    def getName(self):
        return self.name

    def getVoiceActor(self):
        return self.voiceActor

    def getHexColor(self):
        return self.hexColor

    def setName(self, name):
        self.name = name

    def setVoiceActor(self, voiceActor):
        self.voiceActor = voiceActor

    def setHexColor(self, hexColor):
        self.hexColor = hexColor


