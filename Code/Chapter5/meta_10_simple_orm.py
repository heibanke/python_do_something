#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820064557c69858840b4c48d2b8411bc2ea9099ba000


' Simple ORM using metaclass '

__author__ = 'Michael Liao'

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        print "name is ",name
        print "bases is ",bases
        print "attrs is ",attrs
        
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        print "Model instance __init__"
        super(Model, self).__init__(**kw)

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('%s')
            args.append(self[k])
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    @classmethod
    def find_all(cls, *args):


        sql = 'select * from %s' % cls.__table__
        print('SQL: %s' % sql)
# testing code:

class User(Model):
    id = IntegerField('uid')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

    
u1 = User(id=12345, name='Michael', email='test1@orm.org', password='my-pwd')
u2 = User(id=22345, name='Richael', email='test2@orm.org', password='my-pwd')
u3 = User(id=32345, name='Hichael', email='test3@orm.org', password='my-pwd')

u1.save()
u2.save()
u3.save()