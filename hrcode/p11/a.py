import untangle

# 将文件解析成对象
obj = untangle.parse('data.xml')


obj.root.title.__dict__['cdata']


obj.root.body.section[0]


obj.root.body.section[2]
obj.root.body.section[3]
obj.root.body.section[4]