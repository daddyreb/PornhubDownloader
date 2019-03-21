import requests
import re
import io
import sys
import json
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url = "https://www.pornhub.com/playlist/39220041"
url = "https://www.pornhub.com/playlist/88657031"
# url = input("请输入链接: ")
already = []

def get_videolist(list_url):
	list_page = requests.get(list_url, verify=False).content
	list_page = str(list_page, encoding="utf8").replace("\t", "")
	list_page = re.findall('playlistSectionWrapper(.*?)cmtPlaylist', list_page, re.S)[0]
	all_list = re.findall('(\/view_video\.php\?viewkey=.*?)"', list_page)
	video_list = []
	for i in all_list:
		if i not in video_list:
			video_list.append("https://www.pornhub.com" + i)
	return video_list, len(video_list)


def get_videopage(video_url):
	#print(video_url)
	video_page = requests.get(video_url, verify=False).content
	video_page = str(video_page, encoding="utf8").replace("\t", "")
	video_page = json.loads(re.findall('var flashvars.*?= (.*?});', video_page, re.S)[0])
	title = video_page["video_title"].replace('/', '-').replace('\\', '-').replace(':', '-').replace('*', '-').replace(':', '-').replace('"', '-').replace('<', '-').replace('>', '-').replace('|', '-').replace('?', '-')
	video = {"title": video_page["video_title"]}
	index = 0
	for qxd in video_page["mediaDefinitions"]:
		if qxd["quality"] == "720":
			quality = qxd["quality"]
			link = qxd["videoUrl"]
			break
		elif qxd["quality"] == "480":
			quality = qxd["quality"]
			link = qxd["videoUrl"]
			break
		elif qxd["quality"] == "240":
			quality = qxd["quality"]
			link = qxd["videoUrl"]
			index += 1	

	video["quality"] = quality
	video["link"] = link
	#print("aria2c --out=%s -s 8 -x 8 %s" % (title, video["link"]))
	#os.system('aria2c --out="%s" -s 8 -x 8 %s' % (title, video["link"]))
	#print(video_page["mediaDefinitions"][0]["videoUrl"])
	if title not in already:
		already.append(title)
		return 'idman /d "%s" /p "C:\\Users\\24265\\Downloads\\Video\\软萌萝莉小仙" /f "%s" /a' % (video["link"], title+".mp4")
	return False

vl = get_videolist(url)[0]
for v in vl:
	cmd = get_videopage(v)
	if cmd:
		print(cmd)