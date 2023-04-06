import requests

# 查询游戏信息
def info(headers,data):

    url = 'https://smilegate.api.cfm.qq.com/game/rolecard'

    resp = requests.post(url, headers=headers, data=data)
    roleCard = resp.json()['data']['roleCard']

    roleName = roleCard['roleName']
    roleArea = roleCard['roleArea']  # 手q安卓或手q苹果
    type = roleCard['type'] #0:不在线，1：在线
    mainRecord = roleCard['mainRecord']
    divName = mainRecord['divName'] # 段位
    level = mainRecord['level'] # 等级

    return roleName, level, roleArea, divName, type

# 查询账号当前处罚
def get_punish(headers,data):
     
     url = 'https://smilegate.api.cfm.qq.com/queryfacility/penaltyinformation'

     resp = requests.post(url, headers=headers, data=data)
     punish = resp.json()['informationlist']

     return punish

# 查询枪皮
def get_firearms(headers,data):

    url = 'https://smilegate.api.cfm.qq.com/game/getdepotdetail'

    resp = requests.post(url, headers=headers, data=data)
    items = resp.json['data']['items'][0]['items']
    firearmsNum = len(items)
    
    firearms = []
    for each in items :
        firearms.append(each.get('itemName'))
    
    return firearmsNum,firearms

# 查询人物
def get_hero(headers,data):

    url = 'https://formal.api.gp.qq.com/game/getdepotdetail'

    resp = requests.post(url, headers=headers, data=data)
    items = resp.json['data']['items'][0]['items']
    heroNum = len(items)
    
    hero = []
    for each in items :
        hero.append(each.get('itemName'))
    
    return heroNum,hero

     