
'''
练习：假设某公司维护着一些客户资料，需要在该公司有新产品上市或者举行新活动的时候，通知客户

现通知客户的方式有两种：电话通知，邮件通知  type

应如何设计该系统的客户通知部分
'''
#采用策略设计模式  ---把算法放在一个类中


class Msgsenter(object):
    #发送信息的方式
    type = ""
    #保存给客户的信息
    info = ""
    #保存客户姓名
    name = ""

    def send(self):
        pass


class Phonesender(Msgsenter):
    def send(self):
        print("给{}打电话说：{}".format(self.name,self.info))

class Emailsender(Msgsenter):
    def send(self):
        print("给{}发送邮件内容：{}".format(self.name, self.info))

class Customer(object):
    name = ""
    phone = ""
    email = ""
    send_way = None

    #设置发送方式
    def set_send_way(self, send_way):
        self.send_way = send_way

    #设置发送内容
    def sent_message(self):
        self.send_way.send()

if __name__ == '__main__':
    #创建一个客户 - 录入他的信息
    customer = Customer()
    customer.name = "zs"
    customer.phone = "110"
    customer.email = "110@qq.com"

    #1,打电话给客户
    phone_sender = Phonesender()
    phone_sender.name = customer.name
    phone_sender.type = customer.phone
    phone_sender.info = "新活动开始"
    customer.set_send_way(phone_sender)
    customer.sent_message()

    #2,发邮件给客户
    email_sender = Emailsender()
    email_sender.name = customer.name
    email_sender.type = customer.email
    email_sender.info = "新活动开始"
    customer.set_send_way(email_sender)
    customer.sent_message()
