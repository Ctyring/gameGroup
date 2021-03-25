# @功能描述：
# @作者：CTYring
# @QQ：173479693
# @创建时间:  2021/03/21/16:41
import requests
import time
from lxml import etree
def sentMsg(msg):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    }
    api_url = "https://qmsg.zendee.cn/send/af83ed8cfbb3e7a2ea86f286c86e5c86?msg= %s" % msg
    return requests.post(api_url, headers=headers, timeout=None).content
page = 1
def seek(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    }
    url1 = 'https://www.yystv.cn/games/game_tags/1?page=' + str(page) + '&order=score'
    res1 = requests.get(url=url1, headers=headers).text
    tree = etree.HTML(res1)
    names = tree.xpath('//*[@id="page-container"]/ul/li/a/h3/text()')
    file = open('count.txt','r',encoding='utf-8')
    url_list = tree.xpath('//*[@id="page-container"]/ul/li/a/@href')
    s_list = tree.xpath('//*[@id="page-container"]/ul/li/a/div/div[1]')
    had_list = file.readlines()
    file.close()
    # print(had_list)
    # print(names)
    temp = (page-1)*15
    print(temp)
    for i in range(0,15):
        if((i + temp < len(had_list)) and names[i].strip() == had_list[i + temp].strip()):
            continue
        else:
            print(i)
            # time.sleep(1)
            # url = 'https://www.yystv.cn' + url_list[i]
            # print(url)
            # res2 = requests.get(url=url,headers=headers).text
            # tree = etree.HTML(res2)
            print(s_list[i].text)
            sentMsg("每日高分游戏推荐" + '\n' + names[i] + '\n' + s_list[i].text + '分')
            file = open('count.txt', 'a', encoding='utf-8')
            file.write(names[i] + '\n')
            file.close()
            return True
    return False
if __name__ == '__main__':
    while not seek(page):
        page += 1