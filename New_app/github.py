import requests
import json
import time
from datetime import datetime, timedelta

class Github:
  GITHUB_API = "https://api.github.com/"
  client_secret="7639703bd5d8ebca9bbe581ae8909b4cbbc47df0"
  client_id="51560070d2187487a8d1"



  races = {
      "AIAN" : {},
      "BAA" : {},
      "NHOPI" : {},
      "WHI" : {},
      "HL" : {},
      "NHL" : {}
  }

  userDict = None

  def user(self, userName):
    url = "users/" + userName
    url = self.buildurl(url)
    return self.getJson(url)

  def buildurl(self, halfurl):
    return self.GITHUB_API + halfurl \
                  + "?client_id=" + self.client_id \
                  + "&client_secret=" + self.client_secret \
                  + "&per_page=100"

  def buildCommiturl(self, halfurl):
    return halfurl \
          + "?client_id=" + self.client_id \
          + "&client_secret=" + self.client_secret \
          + "&per_page=100"

  def getJson(self, url):
    r = requests.get(url)
    if(r.ok):
      repoItem = json.loads(r.text or r.content)
      r.headers["X-RateLimit-Remaining"]
      return repoItem
    r.headers["X-RateLimit-Remaining"]

  def getRepoFromURL(self, url):
    repoName = url.split('/')[4]
    userName = url.split('/')[3]

    url = "repos/" + userName + "/" + repoName

    url = self.buildurl(url)
    return self.getJson(url)


  def getContributorsFromURL(self, url):
    repoName = url.split('/')[4]
    userName = url.split('/')[3]

    url = "repos/" + userName + "/" + repoName + "/contributors"

    url = self.buildurl(url)
    return self.getJson(url)

  def returnContributors(self, url):
    repoName = url.split('/')[4]
    userName = url.split('/')[3]

    url = "repos/" + userName + "/" + repoName + "/contributors"

    url = self.buildurl(url)
    contributors = self.getJson(url)

    result = []
    for i in contributors:
      newDict = dict()
      newDict["username"] = i["login"]
      newDict["image_url"] = i["avatar_url"]
      newDict["contributions"] = i["contributions"]
      newDict["profile_url"] = i["html_url"]
      result.append(newDict)

    return result

  def getAllCommitsInTheLastMonth(self, url):
    repoName = url.split('/')[4]
    userName = url.split('/')[3]

    dataSince = datetime.now() - timedelta(30) #30 days in a month... only get a month of data

    pageNum = 1

    isMorePages = True

    self.initializeRacesDict();
    while(isMorePages):
      url = "repos/" + userName + "/" + repoName + "/commits"

      url = self.buildurl(url) + "&since=" + dataSince.isoformat() + "&page=" + str(pageNum)

      r = requests.get(url)
      if(r.ok):
        repoItem = json.loads(r.text or r.content)
        headers = ""
        if "link" in r.headers.keys():
          headers = r.headers["link"]
        if 'rel="next"' not in headers.split(' '):
          isMorePages = False
        if repoItem == None:
          print "WTF"
        self.parseCommits(repoItem)
        pageNum += 1

  def parseCommits(self, pageOfCommits):
    for commit in pageOfCommits:
      url = self.buildCommiturl(commit["url"])
      jsonResponse = self.getJson(url)
      time.sleep(.001)

      print str(jsonResponse["stats"])
      userInfo = self.userDict[jsonResponse["author"]]
      self.races[userInfo["race"]] += int(jsonResponse["stats"]["additions"])
      self.races[userInfo["ethnicity"]] += int(jsonResponse["stats"]["deletions"])

  def combineRaces(self, userInfo):
    userInfo = json.loads(userInfo)
    self.userDict = dict()
    for i in userInfo:
      userName = i["username"]
      self.userDict[userName] = dict()
      del i["username"]
      self.userDict[userName] = i

  def initializeRacesDict(self):
    for race in self.races:
      race["ADD"] = 0
      race["DEL"] = 0














