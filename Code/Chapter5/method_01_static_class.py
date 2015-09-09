#!/usr/bin/env python
# coding: utf-8
# http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return "{0}-{1}-{2}".format(self.year, self.month, self.day)
    
    @classmethod
    def from_string(cls, date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1
    
    @staticmethod
    def is_date_valid(date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999  

    @staticmethod
    def millenium(month, day):
        return Date(month, day, 2000) 
        
        
class DateTime(Date):
    def __str__(self):
        return "{0}-{1}-{2} - 00:00:00PM".format(self.year, self.month, self.day)  

            
if __name__=="__main__":
    
    s='2012-09-11'
    if Date.is_date_valid(s):
        date1 = Date.from_string('2012-09-11')
        print date1
        date2 = DateTime.from_string('2012-09-11')
        print date2
        
    millenium_new_year1 = Date.millenium(1, 1)
    print millenium_new_year1
    
    millenium_new_year2 = DateTime.millenium(10, 10)
    print millenium_new_year2