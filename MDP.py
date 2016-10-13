#!/usr/bin/python

#state : tuple of reward and a list of actions, which are themselves lists of probabilities and resultant states
# (reward, [ (action, [(state,prob), (state,prob)]), (action, [(state,prob)]) ])

import sys

def dot (p, r):
	print("p",p)
	print("r",r)
	return sum([px * rx for px,rx in zip(p,r)])	

def discountedRewards (rewards, state, dRate, jValues):
	return [dot(p,rewards)+dRate*dot(p,jValues) for p in state]

def j (state_transitions, rewards, dRate, jValues):
	return [(j.index(max(j)),max(j)) for j in [discountedRewards (rewards, state, dRate, jValues) for state in state_transitions]]

def readFile (fileName, numStates, numActions):
	stateNames = []
	actionNames = []
	transitionMatrix = [[[0]*numStates for x in range(0,numActions)] for x in range(0,numStates)]
	rewards = [0 for x in range(0,numStates)]
	with open(fileName, "r") as f:
		for line in f:
			parsedLine = [l.strip().strip(')').split() for l in line.split('(')]
			if parsedLine[0][0] not in stateNames:
				stateNames.append(parsedLine[0][0])
			stateNumber = stateNames.index(parsedLine[0][0])
			rewards[stateNames.index(parsedLine[0][0])] = float(parsedLine[0][1])
			print(rewards)
			for action in parsedLine[1:]:
				if action[0] not in actionNames:
					actionNames.append(action[0])
				if action[1] not in stateNames:
					stateNames.append(action[1])
				transitionMatrix[stateNumber][actionNames.index(action[0])][stateNames.index(action[1])] = float(action[2])

	return (transitionMatrix,stateNames,actionNames,rewards)

def main ():
	tm,stateName,actionName,rewards = readFile(sys.argv[3],int(sys.argv[1]),int(sys.argv[2]))
	jVector = [0 for x in range(0,int(sys.argv[1]))]
	jVector = j(tm, rewards, float(sys.argv[4]), jVector)
	for x in range(0,20):
		print(jVector)
		print(stateName)
		print("After iteration %d:  %s"%(x+1," ".join(["(%s %s %.3f)"%(name,actionName[jVector[]],jV[0]) for name in stateName])))
		jVector = j(tm, rewards, sys.argv[4],list(zip(*jVector))[0])

main()
