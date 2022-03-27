import math
import random
import matplotlib.pyplot as plt
import pandas as pd

class Visulizor():
    def __init__(self, baseR, dataLen):
        self.baseR = baseR
        self.figLim = baseR * 0.75

        self.X, self.Y = [], []
        self.Areas, self.Colors = [], []
        self.stepOfTheta = 6.28 / dataLen# * 1.1 # 2 * pi == 6.28
        self.R = []

        self.EventAndColorDict = {'摸鱼待机': '#436EEE', '睡觉': '#00EE76', '代码': '#CD6090', '打游戏': '#1874CD', '家务事': '#B452CD',
                                  '碎片化时间': '#7D26CD', '学习': '#FF4500', '文字工作': '#FF0000', '隐私相关的事情': '#00CD00',
                                  '业余爱好': '#63B8FF', '与人交际': '#8B0000', '构思': '#FF3030', '杂务事': '#551A8B'}

    def setNewCircleOfEvent(self, duration, type, theta):
        def tanh(x):
            return 1 - 2 / (1 + math.e ** (2 * (x)))

        d = round(math.log((duration / 15) + random.random()), 4) * 0.17 # 应该再加个系数，一种权重，别让现在这种分层分得过于明显
        r = round(tanh(d), 8) * 7
        self.R.append(r)
        rho = self.baseR * 0.1 + d

        x = round(rho * math.cos(theta), 4)
        y = round(rho * math.sin(theta), 4)
        area = round(3.1416 * r * r * 97, 4)

        color = 0
        if type == None:
            if r != 0.0:
                color = area * r**(-1) * 6.2
        else:
            color = self.EventAndColorDict[type]

        self.X.append(x)
        self.Y.append(y)
        self.Areas.append(area)
        self.Colors.append(color)

    def showTransfercation(self, data):
        if type(data) == pd.DataFrame:
            for i, v in data.iterrows():
                theta = 6.28 - i * self.stepOfTheta
                self.setNewCircleOfEvent(v['duration'], v['event'], theta)
        else:
            for i in range(len(data)):
                theta = 6.28 - i * self.stepOfTheta
                self.setNewCircleOfEvent(data[i], None, theta)

        plt.ion()
        plt.figure(figsize=(8, 8))

        plt.xlim(-self.figLim, self.figLim)
        plt.ylim(-self.figLim, self.figLim)
        # plt.scatter(self.X, self.Y, c='none', edgecolors=self.Colors, s=self.Areas, marker="o")
        plt.scatter(self.X, self.Y, c=self.Colors, s=self.Areas, marker="o")

        plt.ioff()
        plt.show()

data = pd.read_csv("./demoData.csv")[['duration', 'event']]
v = Visulizor(1.0, data.shape[0])
v.showTransfercation(data)



