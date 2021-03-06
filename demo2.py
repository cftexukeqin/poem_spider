import re

# findall 查找所有符合条件的字符串
# text = "apple's price is $299,orange's price is $10"
# ret = re.findall('\$\d+',text)
# print(ret)

# sub 进行替换
# text = "apple's price is $299,orange's price is $10"
# ret = re.sub('\$\d+',"$0",text)
# print(ret)

#
# html = """
# <div>
# <p>基本要求：</p>
# <p>1、精通HTML5、CSS3、 JavaScript等Web前端开发技术，对html5页面适配充分了解，熟悉不同浏览器间的差异，熟练写出兼容各种浏览器的代码；</p>
# <p>2、熟悉运用常见JS开发框架，如JQuery、vue、angular，能快速高效实现各种交互效果；</p>
# <p>3、熟悉编写能够自动适应HTML5界面，能让网页格式自动适应各款各大小的手机；</p>
# <p>4、利用HTML5相关技术开发移动平台、PC终端的前端页面，实现HTML5模板化；</p>
# <p>5、熟悉手机端和PC端web实现的差异，有移动平台web前端开发经验，了解移动互联网产品和行业，有在Android,iOS等平台下HTML5+CSS+JavaScript（或移动JS框架）开发经验者优先考虑；6、良好的沟通能力和团队协作精神，对移动互联网行业有浓厚兴趣，有较强的研究能力和学习能力；</p>
# <p>7、能够承担公司前端培训工作，对公司各业务线的前端（HTML5\CSS3）工作进行支撑和指导。</p>
# <p><br></p>
# <p>岗位职责：</p>
# <p>1、利用html5及相关技术开发移动平台、微信、APP等前端页面，各类交互的实现；</p>
# <p>2、持续的优化前端体验和页面响应速度，并保证兼容性和执行效率；</p>
# <p>3、根据产品需求，分析并给出最优的页面前端结构解决方案；</p>
# <p>4、协助后台及客户端开发人员完成功能开发和调试；</p>
# <p>5、移动端主流浏览器的适配、移动端界面自适应研发。</p>
# </div>
# """

# ret = re.sub('<.+?>',"",html)
# print(ret.strip())

# split进行分割
# 利用取反的方式，巧妙解决任意字符的分割

# text = "Hello world,my dear"
# ret = re.split("[^a-zA-Z]",text)
# print(ret)

# compile
# 将常用的正则表达式先编译，不需要每次都写一遍正则表达式，提高效率

# text = "my computer cost 5000.00 RMB"
# r = re.compile('\d+\.?\d+')
# ret = re.search(r,text)
# print(ret.group())