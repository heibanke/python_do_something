#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

#--------用dict直接生成, 
name_age=(('xiaoli',33),('xiaowang',20),('xiaozhang',40))
a=dict(name_age)
b=dict(xiaoli=33,xiaowang=20,xiaozhang=40)

#--------如何将两个等长度的list合并成dict
text = 'c++ python shell ruby java javascript c'
code_num = [38599, 100931, 26153, 93142, 84275, 184220, 46843]

text_list=text.split(' ')
code_dict = dict(zip(text_list,code_num))

#--------key, keys, items, values
code_dict['python']
code_dict.keys()
code_dict.values()
code_dict.items()

#--------get
a=code_dict.get('fortran',None)

#------- ref and copy
a_ref = code_dict
a_copy = code_dict.copy()

#--------update, del, copy, clear
other_code = {'php':78014,'objective-c':34444}
code_dict.update(other_code)
del code_dict['c++']
a_ref
a_copy
a_ref.clear()

#--------sort key and value
[(k,a_copy[k]) for k in sorted(a_copy.keys())]



