import requests

# 查询游戏信息
def info(headers,data):

    url = 'https://formal.api.gp.qq.com/game/rolecard3'

    resp = requests.post(url, headers=headers, data=data)
    roleCard = resp.json()['data']['roleCard']

    roleName = roleCard['roleName']
    roleArea = roleCard['roleArea']  # 手q安卓或手q苹果
    type = roleCard['type'] #0:不在线，1：在线
    mainRecord = roleCard['mainRecord']
    divName = mainRecord['divName'] # 段位
    level = mainRecord['level'] # 等级

    return roleName, level, roleArea, divName, type

# 获取套装
def get_suit(headers,data):

    url = 'https://formal.api.gp.qq.com/game/getdepotdetail'

    resp = requests.post(url, headers=headers, data=data)
    items = resp.json['data']['items'][0]['items']
    suitNum = len(items)
    
    suit = []
    for each in items :
        suit.append(each.get('itemName'))
    
    return suitNum,suit

# 获取枪械
def get_firearms(headers,data):

    url = 'https://formal.api.gp.qq.com/game/getdepotdetail'

    resp = requests.post(url, headers=headers, data=data)
    items = resp.json['data']['items'][0]['items']
    firearmsNum = len(items)
    
    firearms = []
    for each in items :
        firearms.append(each.get('itemName'))
    
    return firearmsNum,firearms

# 获取载具
def get_car(headers,data):

    url = 'https://formal.api.gp.qq.com/game/getdepotdetail'

    resp = requests.post(url, headers=headers, data=data)
    items = resp.json['data']['items'][0]['items']
    carsNum = len(items)
    
    cars = []
    for each in items :
        cars.append(each.get('itemName'))

    return carsNum,cars

# 获取滑翔尾迹及僚机
def get_fly(headers,data):

    url = 'https://formal.api.gp.qq.com/game/getdepotdetail'

    resp = requests.post(url, headers=headers, data=data)
    items = resp.json['data']['items'][1]['items']
    glidingwakeNum = len(items)

    glidingwake = []
    for each in items :
        glidingwake.append(each.get('itemName'))

    items = resp.json['data']['items'][2]['items']
    wingplaneNum = len(items)
    
    wingplane = []
    for each in items :
        wingplane.append(each.get('itemName'))

    return glidingwakeNum, wingplaneNum, glidingwake, wingplane

# 查询账号当前处罚
def get_punish(headers,data):
     
     url = 'https://formal.api.gp.qq.com/queryfacility/penaltyinformation'

     resp = requests.post(url, headers=headers, data=data)
     punish = resp.json()['informationlist']

     return punish
     