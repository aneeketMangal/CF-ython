import requests
import json
import random

print(listOfContests['result'][0])


class API:

	def __init__(self):
		self.listOfContests = self.getAllContests()
		self.listOfProblems = self.getAllProblems()

	def getAllProblems(self, id):

		listOfProblems = requests.get("https://codeforces.com/api/problemset.problems")
		listOfProblems = listOfProblems.json()
		if(listOfProblems['status']== "OK"):
			listOfProblems = listOfProblems["result"]
		else:
			listOfProblems = []
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


		pass

	def getProblem(self, contestID, index):
		for i in self.listOfProblems:
			if(i['contestID'] == contestID and i['index'] == index):
				return i









