# 创建者：29249
# 创建时间：2022/11/17 16:23 星期四
# ！！！！！！请运行前，先在同级目录里创建两个名称分别为“随机密码.txt”、“指纹密码.txt”的文件，否者部分内容将不能实现或将报错。
import numpy as np
import random
import time


class Shuiji:
    @staticmethod
    def shengcheng():
        numb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        word = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'q', 'w', 'e', 'r', 't', 'u', 'i', 'o', 'p', 'Y', 'K', 'L', '@']
        print("===============================")
        w = int(input("请输入期望密码位数："))
        k = str(input("请输入关键字："))
        s = int(input("请输入期望密码类型（0为纯数字，1为混合型）："))
        print("-------------------------------")
        m = str()
        # '''纯数字密码生控区'''
        if s == 0:
            for i in range(w):  # 随机从列表numb中抽取一个值添加到 m 最后
                m = m + random.choice(numb)
        elif s == 1:  # 混合密码生控区
            for _ in range(w):
                From = random.randint(1, 2)
                if From == 1:
                    # 随机从列表numb中抽取一个值添加到m的最后
                    m = m + random.choice(numb)
                elif From == 2:
                    # 随机从列表word中抽取一个值添加到m的最后
                    m = m + random.choice(word)
        txt = open("随机密码.txt", 'r', encoding='UTF-8').read()
        with open("随机密码.txt", 'w', encoding='UTF-8') as f:
            f.write(txt)
            f.write(k + ' 生成密码为:' + m)
            f.write('\n')
        print("-----------正在生成密码，请稍后--------------")
        for ti in range(1, 5):
            time.sleep(0.5)
            print('===已进行{}%==='.format(ti * 25))
        time.sleep(0.5)
        print("{}的密码是：{}".format(k, m))
        time.sleep(2)
        print("--------------密码生成完毕-----------------")
        print('1-继续生成')
        print('2-读取历史')
        print('3-返回主界面')
        xiangmu = int(input('请选择项目：'))
        print("--------------正在执行-----------------")
        time.sleep(1.5)
        if xiangmu == 1:
            Shuiji.shengcheng()
        elif xiangmu == 2:
            Shuiji.duqu()
        elif xiangmu == 3:
            Mainpg.main()

    @staticmethod
    def duqu():
        print("--------------正在读取历史记录-----------------")
        time.sleep(1.5)
        print('以下为历史记录：')
        d = open('随机密码.txt', 'r', encoding='UTF-8')
        print(d.read())
        print("======密码展示完毕======")
        time.sleep(2)
        print("-----------------------------------")
        print('1-生成密码')
        print('2-返回主界面')
        xiangmu = int(input('请选择项目：'))
        print("--------------正在执行-----------------")
        time.sleep(0.5)
        if xiangmu == 1:
            Shuiji.shengcheng()
        elif xiangmu == 2:
            Mainpg.main()

    @staticmethod
    def huanying():
        print("-----------------------------------")
        print('1-生成密码')
        print('2-读取历史')
        print('3-返回主界面')
        xiangmu = int(input('请选择项目：'))
        print("--------------正在执行-----------------")
        time.sleep(0.5)
        if xiangmu == 1:
            Shuiji.shengcheng()
        elif xiangmu == 2:
            Shuiji.duqu()
        elif xiangmu == 3:
            Mainpg.main()


class Mima:
    @staticmethod
    def jiami():
        data = input('请输入关键字：')
        lit = []
        for i in data:
            lit.append(ord(i))
        long = len(lit)
        lit = [j + long for j in lit]
        a = 'zw'.join(str(h) for h in lit)

        diary = open('指纹密码.txt', 'r', encoding='UTF-8').read()
        cv = open('指纹密码.txt', 'w', encoding='UTF-8')
        cv.write(diary)
        cv.write(data + '的指纹密码是：' + data)
        cv.write('\n')
        cv.close()
        print("-----------正在生成密码，请稍后--------------")
        for ti in range(1, 5):
            time.sleep(0.5)
            print('===已进行{}%==='.format(ti * 25))
        print(data + '的指纹密码是：{}'.format(a))
        time.sleep(2)
        print("--------------密码生成完毕-----------------")
        Mima.xuanze()

    @staticmethod
    def duqu2():
        print("--------------正在读取历史记录-----------------")
        time.sleep(1.5)
        print('以下为历史记录：')
        d = open('指纹密码.txt', 'r', encoding='UTF-8')
        print(d.read())
        print("======密码展示完毕======")
        time.sleep(2)
        Mima.xuanze()

    @staticmethod
    def jiemi():
        data2 = input("加密的原文：")
        w = data2
        data2 = data2.split("zw")  # 去除间隔符，并生成一个名为data2的列表
        data2 = list(map(int, data2))  # 由于前面列表data2里的元素还是str型，后面还原运算没法进行，所以变成int型
        long = len(data2)  # 用于data2列表长度，以进行解密运算
        data2 = [j - long for j in data2]  # 还原出原文对应编码
        c = ''.join(chr(h) for h in data2)
        print("--------------正在解密-----------------")
        for ti in range(1, 5):
            time.sleep(0.5)
            print('===已进行{}%==='.format(ti * 25))
        print(w + '的原文是：' + c)
        print("======解密完毕======")
        time.sleep(2)
        Mima.xuanze()

    @staticmethod
    def xuanze():
        print("--------------------------------------")
        print('1-生成密码')
        print('2-解读密码')
        print('3-读取历史')
        print('4-返回主界面')
        xiangmu = int(input('请选择项目：'))
        print("--------------正在执行-----------------")
        time.sleep(1.5)
        if xiangmu == 1:
            Mima.jiami()
        elif xiangmu == 2:
            Mima.jiemi()
        elif xiangmu == 3:
            Mima.duqu2()
        elif xiangmu == 4:
            Mainpg.main()


class Matrix:
    @staticmethod
    def jiami():
        # 用于后面填充原文的矩阵，
        A = np.array([[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]])
        # 密钥矩阵,由我们的成员生日及编译当天日期组成
        key = np.array([[9, 12, 5, 12],
                        [12, 12, 5, 11],
                        [11, 5, 1, 21],
                        [20, 22, 11, 16]])
        k, j = 0, 0  # 准备
        print('&*&*&*&*指纹加密*&*&*&*&')
        cher = input("输入需加密文本：")  # 输入原文
        lit = []
        for i in cher:
            lit.append(ord(i))  # 以数字的形式转入列表
        lit_long = int(len(lit))

        # 列表中的元素依次转入矩阵
        for c in lit:
            A[k, j] = c
            j += 1
            if j == 4:
                j = 0
                k += 1
        # 获取密键，使密码发生变化，不易根据数量统计而破解
        xkey = int(A[0, 1] / 230)
        """-------------"""
        # 加密过程
        if lit_long % 2 == 0:
            key = key.T
        xE = np.dot(xkey, key)
        mimatrix = A - xE
        # 输出
        print("-----------正在进行指纹加密，请稍后--------------")
        for ti in range(1, 5):
            time.sleep(0.5)
            print('===已进行{}%==='.format(ti * 25))
        time.sleep(0.5)
        hang = 0
        lie = 0
        print("加密结果为：")
        for h in range(lit_long):
            word = int(mimatrix[lie, hang])
            print(chr(word), end='')
            hang += 1
            if hang == 4:
                hang = 0
                lie += 1
        print(chr(xkey))
        time.sleep(2)
        print("--------------加密完毕，请继续-----------------")
        return Matrix.miwen()

    @staticmethod
    def huanyuan():
        # 用于后面填充原文的矩阵，
        A = np.array([[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]])
        # 密钥矩阵,由我们的成员生日及编译当天日期组成
        key = np.array([[9, 12, 5, 12],
                        [12, 12, 5, 11],
                        [11, 5, 1, 21],
                        [20, 22, 11, 16]])
        p, o = 0, 0
        print('&*&*&*&*指纹加密*&*&*&*&')
        data = input("输入文本：")
        lit = []
        for i in data:
            lit.append(ord(i))
        lit_long = int(len(lit)) - 1
        if lit_long % 2 == 0:
            key = key.T

        for c in lit:
            A[p, o] = c
            o += 1
            if o == 4:
                o = 0
                p += 1

        xkey = lit[lit_long]
        xE = np.dot(xkey, key)
        back = A + xE
        print("-----------正在进行指纹解密，请稍后--------------")
        for ti in range(1, 5):
            time.sleep(0.5)
            print('===已进行{}%==='.format(ti * 25))
        time.sleep(0.5)
        hang = 0
        lie = 0
        print("解密结果为：")
        for h in range(lit_long):
            word = int(back[lie, hang])
            print(chr(word), end='')
            hang += 1
            if hang == 4:
                hang = 0
                lie += 1
        time.sleep(2)
        print()
        print("--------------解密完毕，请继续-----------------")
        return Matrix.miwen()

    @staticmethod
    def miwen():
        print("-----------------------------------")
        print('1-指纹加密')
        print('2-指纹解密')
        print('3-返回主界面')
        a = int(input('请选择项目：'))
        print("--------------正在执行-----------------")
        time.sleep(0.5)
        if a == 1:
            Matrix.jiami()
        elif a == 2:
            Matrix.huanyuan()
        elif a == 3:
            Mainpg.main()
        else:
            print('Error:无法识别，请重试！')
            return Matrix.miwen()


class Mainpg:
    @staticmethod
    def main():
        print('《-----欢迎使用-----》')
        print('1-生成随机密码')
        print('2-指纹密码')
        print('3-指纹密语')
        print('4-关闭')
        fuwu = int(input('请选择服务：'))
        print("--------------正在执行-----------------")
        time.sleep(0.5)
        if fuwu == 1:
            Shuiji.huanying()
        elif fuwu == 2:
            Mima.xuanze()
        elif fuwu == 3:
            Matrix.miwen()
        elif fuwu == 4:
            print('《-----谢谢使用-----》')
            print('《----GOOD  BY----》')
        else:
            print('Error:无法识别，请重试！')
            return Mainpg.main()


Mainpg.main()
