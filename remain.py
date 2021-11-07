import account_time

out =[]
data1 = {
   '':'' 
}

data = [data1,...]
class Remain:
    def num_to_char(self,num):#数字转换星期
        num = str(num)
        new_str = ""
        num_dict = {"1": u"一", "2": u"二", "3": u"三", "4": u"四", "5": u"五", "6": u"六", "7": u"日"}
        listnum = list(num)
        shu = []
        for i in listnum:
            shu.append(num_dict[i])
        new_str = "".join(shu)
        return new_str

    def text(self,x, y,*arges):#根据data设置邮寄内容
        out.append('本周是第' + str(x) + '周,' + '星期' + self.num_to_char(y))
        for key in range(len(data)):
            if x in data[key]["week"]:
                if y in data[key]["day"]:
                    s = '今天第' + str(data[key]['jie']) + '节有' + str(data[key]['name']) + "，上课地点：" + str(
                        data[key]['address'] + "，上课时间：" + str(data[key]['time']))
                    out.append(s)
        if len(out) <= 1:
            out.append(" ")#随意添加
        return out

remain = Remain()


