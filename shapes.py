import random


shapes = [[[0,0,0,0]
          ,[0,0,0,0]
          ,[0,0,1,1]
          ,[0,1,1,0]],
          [[0,0,1,0]
           ,[0,0,1,0]
           ,[0,0,1,0]
           ,[0,0,1,0]]
          ,[[0,0,0,0]
            ,[0,1,1,0]
            ,[0,1,1,0]
            ,[0,0,0,0]]
          ,[[0,0,0,0]
            ,[0,1,1,0]
            ,[0,1,1,0]
            ,[0,0,0,0]]
          ,[[0,0,0,0]
            ,[0,0,0,0]
            ,[0,0,1,0]
            ,[0,1,1,1]]]

def getRandomShape():
    return random.choices(shapes)

