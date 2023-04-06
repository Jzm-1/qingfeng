import requests

# 王者营地获取指定账号的英雄数量，皮肤数量，所拥有的英雄
def hero(headers,data):

    url = 'https://ssl.kohsocialapp.qq.com:10001/play/h5getherolist'

    resp = requests.post(url, headers=headers, data=data)
    data = resp.json()

    heroNum = data['data']["hasData"]["heroNum"]
    skinNum = data['data']["hasData"]["skinNum"]
    heroList = data['data']["heroList"]

    return heroNum,skinNum,heroList

# 获取所拥有的皮肤
def skin(headers,data):

    url = 'https://ssl.kohsocialapp.qq.com:10001/play/h5getheroskinlist'

    resp = requests.post(url, headers=headers, data=data)

    data = resp.json()['data']["heroSkinList"]

    skinlist = []
    for each in data:
        if each.get("iBuy") != None:
                skinlist.append(each.get("szTitle"))
    return skinlist

# 查询游戏信息
def info(headers,data):
     
    url = 'https://ssl.kohsocialapp.qq.com:10001/game/battleprofile'

    resp = requests.post(url, headers=headers, data=data)
    
    rolecard = resp.json()['data']['rolecard']
    roleName = rolecard['roleName']  # 游戏id
    level = rolecard['level'] # 游戏等级
    district = rolecard['district'] # 游戏区服
    grade = rolecard['jobName'] # 游戏段位
    status = rolecard['liveStatus'] # 状态(0：不在线，1：在线)

    return roleName, level, district, grade, status
        
# 获取当前信誉积分
def get_prestige(headers,data):
     
    url = 'https://ssl.kohsocialapp.qq.com:10001/queryfacility/reputationpoints'

    resp = requests.post(url, headers=headers, data=data)

    prestige = resp.json()['num']

    return prestige

# 查询当前账号处罚信息
def get_punish(headers,data):
     
     url = 'https://ssl.kohsocialapp.qq.com:10001/queryfacility/penaltyinformation'

     resp = requests.post(url, headers=headers, data=data)

     punish = resp.json()['informationlist']

     return punish
     