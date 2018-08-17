import re
import requests
# 取消SSL警告
import urllib3
urllib3.disable_warnings()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
}

def parse_page(url):
    poem = {}
    poems = []
    response = requests.get(url,headers=headers,verify=False)
    text = response.text
    # 因为.不能匹配换行符，因此添加re.DOTALL ，可以使.匹配任意字符
    titles = re.findall('<div class="cont">.+?<b>(.*?)</b>',text,re.DOTALL)
    dynsties = re.findall('<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall('<p class="source">.*?<a.*?/a>.*?<a.*?>(.*?)</a>',text,re.S)
    content_tags = re.findall('<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in content_tags:
        content = re.sub('<.+?>',"",content)
        contents.append(content.strip())
    for value in zip(titles,dynsties,authors,contents):
        title, dynsty, author, content = value
        poem['title'] = title
        poem['dynsty'] = dynsty
        poem['author'] = author
        poem['content'] = content
    poems.append(poem)
    print(poems)



def main():
    base_url = "https://www.gushiwen.org/default_{}.aspx"
    for i in range(1,20):
        new_url = base_url.format(i)
        parse_page(new_url)

if __name__ == '__main__':
    main()