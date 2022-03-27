# oneDemensionalDataVisulizor
将一维数据进行可视化的娱乐向方案，视频讲解版稍后发布：

所需要的库：
    自带库：math，random
    第三方库：matplotlib，pandas

使用方法：
    data：一个序列，最好是pandas.DataFrame类型的，其中`[[<大小>, <类型>]]`，如果不行那就传入`[<大小>]`
    `v = Visulizor(1.0, len(data)) # 创建一个类，需要声明你要画的图中间那个空白圆圈的半径，以及data有多长`
    `v.showTransfercation(data)`

当附带的的`demoData.csv`和`一维数据可视化.py`在同一目录下时可以直接运行，可以参考进行调整
`Figure_1.svg`和`Figure_3.svg`为完整版数据的展示结果
