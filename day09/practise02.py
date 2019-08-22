"""
工资结算系统

某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
import abc


class Employe(object, metaclass=abc.ABCMeta):
    # 员工
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abc.abstractmethod
    def get_salary(self):
        pass


class Manager(Employe):

    def get_salary(self):
        return 15000


class Programmer(Employe):
    def __init__(self, name, work_hours=0):
        super().__init__(name)
        self._work_hours = work_hours

    @property
    def work_hours(self):
        return self._work_hours

    @work_hours.setter
    def work_hours(self, work_hours):
        self._work_hours = work_hours if work_hours > 0 else 0

    def get_salary(self):
        return self._work_hours * 150


class Salesman(Employe):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200 + self._sales * 0.05


def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]

    for employe in emps:
        if isinstance(employe, Programmer):
            work_hours = int(input("请输入%s工作时长" % employe.name))
            employe.work_hours = work_hours
        elif isinstance(employe, Salesman):
            sales = float(input("请输入%s的销售业" % employe.name))
            employe.sales = sales
        print("%s 的薪水是 %d" % (employe.name, employe.get_salary()))


if __name__ == '__main__':
    main()
