#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import random

secret = random.randint(1, 100)
guess,tries = 0,0

print u"你好, 你很幸运, 我是一个路过的神仙, 我有一个秘密!"
print u"我的秘密是一个从1到99的数字, 我只会给你6次机会来猜。"
print u"如果你猜到它, 那说明你真的很幸运, 赶紧去买彩票吧!"

while guess != secret and tries <6:
    print u"你猜这个数字是多少? (1-100)"
    guess_str = raw_input()

    try:
        guess = int(guess_str)
    except:
        print u"你输入的不是整数，请重新输入："
        continue
        
    if guess == secret:
        print u"哇~~~, 真的假的！你居然发现了我的秘密! 它就是: ", str(secret)
        break
    elif guess < secret:
        print str(guess),u"太小了, 你还差点运气! "
    elif guess > secret:
        print str(guess),u"太大了, 你还差点运气! "
    tries += 1
     
else:
    print u"你唯一的机会已被你用完了！看来你还需要再攒点人品！"
    print u"还是让我告诉你吧！这个数字是: ", str(secret)