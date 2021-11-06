import account_time

out =[]
data1 = {
   '':'' 
}

data = [data1,...]

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


