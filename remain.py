import account_time

out =[]
data1 = {
    'week': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14,15,16,17,18],
    'day': [1],
    'jie': [6,7],
    'name': '英语视听说',
    'address': '奉贤4教楼A519',
    'time':'13:00'
}
data2 = {
    'week': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14,15,16,17,18],
    'day': [1],
    'jie': [8,9],
    'name': '初等教育学',
    'address': '奉贤4教楼D204',
    'time':'14:45'
}
data3 = {
    'week': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14,15,16,17,18],
    'day': [2],
    'jie': [3,4],
    'name': '概率论',
    'address': '奉贤4教楼A415',
    'time':'9:45'
}
data4 = {
    'week': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14,15,16,17,18],
    'day': [2],
    'jie': [6,7],
    'name': '中外文化简史',
    'address': '奉贤4教楼B204',
    'time': '13:00'
}
data5 = {
    'week': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14,15,16,17,18],
    'day': [2],
    'jie': [8,9],
    'name': '小学生心理学',
    'address': '奉贤5教楼A111',
    'time': '14:45'
}
data6 = {
    'week': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14,15,16,17,18],
    'day': [2],
    'jie': [10],
    'name': '体育',
    'address': '奉贤老体育馆篮球场1',
    'time': '16:00'
}
data7 = {
    'week': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14,15,16,17,18],
    'day': [4],
    'jie': [3,4],
    'name': '中国文化',
    'address': '奉贤4教楼A219',
    'time': '9:45'
}
data8 = {
    'week': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14,15,16,17,18],
    'day': [4],
    'jie': [6,7],
    'name': '东西方博物馆里的物与谜',
    'address': '奉贤5教楼A106',
    'time': '13:00'
}
data9 = {
    'week': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14,15,16,17,18],
    'day': [4],
    'jie': [8,9],
    'name': '人类与自然',
    'address': '奉贤5教楼A206',
    'time': '14:45'
}
data10 = {
    'week': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14,15,16,17,18],
    'day': [4],
    'jie': [11,12],
    'name': '组合数学',
    'address': '奉贤5教楼A110',
    'time': '18:00'
}
data = [data1, data2,data3, data4,data5, data6,data7, data8,data9, data10]

class Remain:
    def text(self,x, y,*arges):
        out.append('本周是第' + str(x) + '周,' + '星期' + str(y))
        for key in range(len(data)):
            if x in data[key]["week"]:
                if y in data[key]["day"]:
                    s = '宝宝今天第' + str(data[key]['jie']) + '节有' + str(data[key]['name']) + "，上课地点：" + str(
                        data[key]['address'] + "，上课时间：" + str(data[key]['time']))
                    out.append(s)
        if len(out) <= 1:
            out.append("今天没课哦，但是要记得学习啊！")
        return out

remain = Remain()


