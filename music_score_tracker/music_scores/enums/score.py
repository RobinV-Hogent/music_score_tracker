from enum import Enum

class ScoreSignatures(Enum):
    TWOFOUR = '2/4'
    THREEFOUR = '3/4'
    FOURFOUR = '4/4'
    TWOTWO = '2/2'
    SIXEIGHT = '6/8'
    
class ScoreDifficulty(Enum):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED ='Advanced'
    
class ScoreInstrument(Enum):
    PIANO = 'Piano'
    CELLO = 'Cello'
    VIOLIN = 'Violin'