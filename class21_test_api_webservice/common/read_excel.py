"""
=============================
Author  : lsw
Time    : 2019-09-02
E-mail  :591271859@qq.com
=============================
"""
import openpyxl


class CaseData(object):
    """
    测试用例数据类
    """

    def __init__(self, zip_obj):
        # 变量zip对象
        for i in zip_obj:
            # 将表头作为属性，值作为属性值
            setattr(self, i[0], i[1])


class ReadExcel(object):
    """
    读取Excel中的用例数据
    """
    def __init__(self, file_name, sheet_name):
        """

        :param file_name: Excel文件名
        :param sheet_name: sheet表单名
        """
        self.file_name = file_name
        self.sheet_name = sheet_name

    def open(self):
        """
        打开Excel工作簿和表单
        :return: 工作簿、表单对象
        """
        # 打开Excel文件，返回一个工作簿对象
        self.wb = openpyxl.load_workbook(self.file_name)
        # 通过工作簿选择表单对象
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        """
        读取所有测试用例数据
        :return: 读取出来的测试用例
        """
        self.open()
        # 按行获取所有的表格对象，每一行的内容放在一个元组中，以列表形式返回
        rows = list(self.sh.rows)
        # 创建一个列表用来存放所有测试用例
        cases = []
        # 获取表头
        titles = [r.value for r in rows[0]]
        # 遍历其他的数据行，和表头进行打包并转换为字典，存放动创建的列表中
        for row in rows[1:]:
            # 获取行数据
            data = [r.value for r in row]
            # 和表头进行打包，并转换为字典
            case = dict(zip(titles, data))
            cases.append(case)
        # 将读取出来的数据进行返回
        return cases

    def read_data_obj(self):
        """
        读取所有测试用例数据
        :return: 读取出来的测试用例对象
        """
        self.open()
        # 按行获取所有的表格对象，每一行的内容放在一个元组中，以列表形式返回
        rows = list(self.sh.rows)
        # 创建一个列表用来存放所有测试用例
        cases = []
        # 获取表头
        titles = [r.value for r in rows[0]]
        # 遍历其他的数据行，和表头进行打包并转换为字典，存放动创建的列表中
        for row in rows[1:]:
            # 获取行数据
            data = [r.value for r in row]
            zip_obj = zip(titles, data)
            # 将没一条用例的数据，存储为一个对象
            # 通过CaseData这个类来创建一个对象，传参zip_obj
            case_data = CaseData(zip_obj)
            cases.append(case_data)
        return cases

    def write_data(self,row, column, value):
        """
        写入数据(写入数据的时文件不能打开)
        :param row: 写入的行
        :param column: 写入的列
        :param value: 写入的数据
        """
        self.open()
        # 按照传入的行、列、内容进行写入
        self.sh.cell(row=row, column=column, value=value)
        # 保存
        self.wb.save(self.file_name)


if __name__ == '__main__':
    pass
