import requests
import json

class Github:
  GITHUB_API = "https://api.github.com/"
  client_secret="7639703bd5d8ebca9bbe581ae8909b4cbbc47df0"
  client_id="51560070d2187487a8d1"

  def user(self, userName):
    url = "users/" + userName
    url = self.buildurl(url)
    return self.getJson(url)

  def buildurl(self, halfurl):
    return self.GITHUB_API + halfurl + "?client_id=" + self.client_id + "&client_secret=" + self.client_secret

  def getJson(self, url):
    r = requests.get(url)
    if(r.ok):
      repoItem = json.loads(r.text or r.content)
      return repoItem

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
      result.append(newDict)

    return result