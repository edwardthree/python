# coding:utf-8
#author 1378399640@qq.com
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

def myDearWeiboCrawler(url):
    headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection': 'Keep-Alive',
               'Host': 'zhannei.baidu.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    requests.head(url, headers=headers)
    wbdata = requests.get(url).text

    # 对获取到的文本进行解析
    soup = BeautifulSoup(wbdata, 'lxml')
    # 从解析文件中过滤本页的微博正文
    rootContents = soup.find(id="talkList").find_all("li")

    # 对返回的列表进行遍历
    for n in rootContents:
        # 提取出标题和链接信息
        content = n.find("div", class_="msgCnt")
        time = n.find("a", class_="time")
        platform = n.find("i", class_="sico")
        if platform!=None:
            platform=platform["title"]
        else:
            platform=""
        # contents = content.get_text()+"|"+time.get_text()+"|"+platform
        contents = content.get_text()
        with open('yancanfashi.txt', 'a+') as f:
            try:
                # print(contents)
                f.write(contents)
                f.write("\r")
            except UnicodeEncodeError as e:
                print(contents)
                # print(e)


    nextPageUrlSuffix = soup.find(id="pageNav").find_all("a", "pageBtn")
    nextPageUrl=None
    for page in nextPageUrlSuffix:
        if page.get_text()=="下一页":
            nextPageUrl = rootUrl + page["href"]

    return nextPageUrl

rootUrl = "http://t.qq.com/yancanfashi"
# nextPageUrl=myDearWeiboCrawler(rootUrl)
# while nextPageUrl !=None:
#     nextPageUrl=myDearWeiboCrawler(nextPageUrl)


text_from_file_with_apath = open('yancanfashi.txt').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(
font_path="STXINGKA.TTF",

background_color='white',
width=1000, height=800, margin=12
).generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()