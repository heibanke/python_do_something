#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

class Employee(object):
    def __init__(self, name, job=None, pay=0): # class = data + logic
        self._name = name
        self._job = job
        self._pay = pay
    def giveRaise(self, percent):
        self._pay = int(self._pay * (1 + percent))
    def __str__(self):
        return '[Employee: %s, %s, %s]' % (self._name, self._job, self._pay)


class Manager(Employee):
    def __init__(self, name, pay): # Redefine constructor
        super(Manager,self).__init__(name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        super(Manager,self).giveRaise(percent + bonus)


class Department(object):
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def showAll(self):
        for person in self.members:
            print person 
    def giveRaise(self,percent):
        for person in self.members:
            person.giveRaise(percent)

if __name__ == '__main__':
    a=Employee("xiaoli",'sw_engineer',10000)
    b=Employee("xiaowang",'hw_engineer',12000)
    c=Manager("xiaozhang",8000)

    d=Department(a,b,c)

    d.showAll()
    d.giveRaise(0.1)
    d.showAll()