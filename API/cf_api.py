from imports import *
class CfApi:
	def __init__(self):
		self.listOfProblems = self.getAllProblems()
		self.filePath = "Local/problem.html"
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
		if(contestID[-1]<="Z" and contestID[-1]>="A"):
			problemIndex = contestID[-1]+problemIndex
			contestID = contestID[:-1]
		problemUrl = "https://codeforces.com/problemset/problem/"+contestID+"/"+problemIndex
		# webbrowser.open(problemUrl)
		self.scrapeData2(problemUrl)
		print("loaded")
		return 1


	def submit(self, problemId):
		contestId = problemId[:-1]
		problemUrl = "https://codeforces.com/problemset/problem/"+contestID+"/submit"
		print(problemUrl)
		webbrowser.open(problemUrl)
		return 1


	def scrapeData2(self, URL):
		print(URL)
    	
		text_file = open(self.filePath, "w")
		n = text_file.write("<html><head><title>test</title></head><body>")
		text_file.close()
		problem = self.scrapeData(URL)
		
		# r = requests.get(URL)
		# soup = BeautifulSoup(r.content, 'html5lib')
		# table = soup.find('div', attrs = {'class':'problem-statement'}) 
		# table = str(table)
		# table = re.sub('\$\$\$([^\$]*)\$\$\$', '<b>\\1</b>',table)
		# table = table.replace("\leq", "<=")
		# table = table.replace("\eq", "=")
		text_file = open(self.filePath, "a")
		for i in problem:
			problem[i] = re.sub('\$\$\$([^\$\n]*)\$\$\$', '<b>\\1</b>',problem[i])
			problem[i] = problem[i].replace("\leq", "<=")
			problem[i] = problem[i].replace("\le", "<=")

			problem[i] = problem[i].replace("\eq", "=")
			n = text_file.write(problem[i])
		text_file.close()
		
		text_file = open(self.filePath, "a")
		n = text_file.write("</body></html>")
		text_file.close()

	def scrapeData(self, URL):
		r = requests.get(URL)
		soup = BeautifulSoup(r.content, 'html5lib')
		problem = {}
		problem['header'] = "<h1><b><center>"+str(soup.find('div', attrs = {'class':'title'}))+"</center></b></h1>"
		problem['time-limit'] = "<center><div>Time: "+str(soup.find('div', attrs = {'class':'time-limit'}).text[19:])+"</div></center>"
		problem['memory-limit'] = "<center><div>Memory: "+str(soup.find('div', attrs = {'class':'memory-limit'}).text[21:])+"</div></center>"
		problem['b1'] = "<hr><hr>"
		table = soup.find('div', attrs = {'class':'problem-statement'}) 
		for row in table.findAll('div'):
			try:
				if(row['class'] is None):
					pass
			except:
				problem['statement'] = row.text
		problem['statement'] ="<h3>Statement</h3><div>"+str(problem['statement'])+"</div>"
		problem['input-specification'] = "<h3>Input Specification</h3><div>"+soup.find('div', attrs = {'class':'input-specification'}).find('p').text+"</div>"
		problem['output-specification'] = "<h3>Output Specification</h3><div>"+soup.find('div', attrs = {'class':'output-specification'}).find('p').text+"</div>"
		# problem['sample-tests'] = str(soup.find('div', attrs = {'class':'sample-test'}))
		problem['sample-tests'] = ""
		sampleTests = soup.find('div', attrs = {'class':'sample-test'})
		for test in sampleTests.findAll('div'):
			if(test['class'][0] == 'input'):
				problem['sample-tests'] += "<div><h3>Input</h3></div>"
				problem['sample-tests']+="<div>"+str(test.pre)+"</div>"
			elif(test['class'][0] == 'output'):
				problem['sample-tests']+="<div><h3>Output</h3></div>"
				problem['sample-tests']+="<div>"+str(test.pre)+"</div>"

			else:
				continue

		# with open('person.json', 'w') as json_file:
		#     json.dump(problem, json_file)
    			
		return problem










