import maya.cmds
import random

#time constraints
startTime = maya.cmds.playbackOptions(query = True, min = True)
endTime = maya.cmds.playbackOptions(query = True, max = True)

maya.cmds.currentTime(startTime)

#shapes list instantiation and shapes append
shapes = []

shapes.append(maya.cmds.polySphere()[0])
shapes.append(maya.cmds.polyCube()[0])
shapes.append(maya.cmds.polyCylinder()[0])
shapes.append(maya.cmds.polyCone()[0])
shapes.append(maya.cmds.polyTorus()[0])

#iteration of shapes in list and keyframes before and after translation for movement
for shape in shapes:
    maya.cmds.select(shape, r = True)
    maya.cmds.setKeyframe(shape)
    
    maya.cmds.currentTime(random.randint(startTime, endTime))
    
    maya.cmds.setAttr(shape + ".translateX", random.randint(0, 50))
    maya.cmds.setAttr(shape + ".translateY", random.randint(0, 50))
    maya.cmds.setAttr(shape + ".translateZ", random.randint(0, 50))
    
    maya.cmds.setKeyframe()
    
