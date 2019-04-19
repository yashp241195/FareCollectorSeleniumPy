import os

def readStationData():

	stationList = []
	f = open("stationList.csv","r")

	while True:
		line = f.readline()

		if line == "":
			break

		if line[len(line)-1] == "\n":
			line = line[:-1]

		stationList.append(line)
	
	f.close()

	return stationList


def createMainFareList(stationList):
	size = len(stationList)
	f = open("fareList.csv","w")

	fare = "Null"
	for i in range(size):
		for j in range(size):
			line = stationList[i]+"->"+stationList[j]+"->"+fare+"\n"
			f.write(line)

	f.close()

def isExist(fileName,parentFolder):
	fileName = parentFolder+"/"+fileName
	if os.path.exists(fileName):
		return True
	else:
		return False


def updateFareList(stationList):
	size = len(stationList)
	f = open("fareList.csv","r+")

	for i in range(size):
		
		fileName = "fareList"+str(i)+".csv"

		if(isExist(fileName,"fare")):
			
			fInner = open("fare/"+fileName,"r+")
			# write it ..
			for j in range(size):
				f.write(fInner.readline())
		else:
			# skip it ..
			for i in range(size):
				f.readline()

def run(choice):
	stationList = readStationData()
	if choice == "c":
		createMainFareList(stationList)
	if choice == "u":	
		updateFareList(stationList)
		print("patch successful .. \n")

run("u")


