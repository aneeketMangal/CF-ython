import requests
import json
import random
import webbrowser



class CfApi:
	def __init__(self):
		self.listOfProblems = self.getAllProblems()

	def getAllProblems(self):

		listOfProblems = requests.get("https://codeforces.com/api/problemset.problems")
		listOfProblems = listOfProblems.json()
		if(listOfProblems['status']== "OK"):
			listOfProblems = listOfProblems["result"]["problems"]
		else:
			listOfProblems = []
		# print(listOfProblems)
		return listOfProblems
	def getAllContests(self):
		listOfContests = requests.get("https://codeforces.com/api/contest.list")
		listOfContests = listOfContests.json()
		if(listOfContests['status']== "OK"):
			listOfContests = listOfContests["result"]
		else:
			listOfContests = []
		return listOfContests

	def getProblemsByContestID(self, id):
		problemset = []
		for i in self.listOfProblems:
			if(i['contestID'] == id):
				problemset.insert(i)

		return problemset

	def getRandomProblem(self, rating1):
		problemset = []
		for i in self.listOfProblems:
			if(i['rating'] == rating):
				problemset.insert(i)

		return random.choice(problemset)


	def getProblemsInRange(self, low, high):
		
		try:
			low = int(low)
			high = int(high)
			print(low, high)
			out = []
			
			if(low<=high):
				for i in self.listOfProblems:
					if 'rating' in i:
						if(i['rating']<=high and i['rating']>=low):
							out.append(i)

				return out
			return self.listOfProblems




		except:
			return self.listOfProblems

	def getProblemStatement(self, problemId):
		contestID = problemId[:-1]
		problemIndex = problemId[-1]
		problemUrl = "https://codeforces.com/problemset/problem/"+contestID+"/"+problemIndex
		webbrowser.open(problemUrl)
		return









