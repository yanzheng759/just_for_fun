# -*- coding: utf-8 -*-
import random

play_round = 100000
play_people = 100
play_money = 200
player = {}

for i in range(0, play_people):
    player[i] = play_money

for j in range(0, play_round):
    for i in range(0, play_people):
        rnd = random.randint(0, play_people-1)
        while rnd == i:
            rnd = random.randint(0, play_people-1)

        if player[i] > 0:
            player[i] = player[i] - 1
            player[rnd] = player[rnd] + 1

#本金损失人数
deficit_num = 0
#资金总和>80%的人数
rich_num = 0
#资金总和<10%的人数
poor_num = 0

for i in range(0, play_people):
     print "%d, %d" % (i, player[i])
     if player[i] < play_money:
         deficit_num = deficit_num + 1

tmp = sorted(player.iteritems(), key=lambda asd:asd[1], reverse=True)
print tmp

num = 0
rich_gw = int(play_people * play_money * 0.8)
poor_gw = int(play_people * play_money * 0.1)
for var in tmp:
    num += var[0]
    rich_num += 1
    if num >= rich_gw:
        break

tmp = sorted(player.iteritems(), key=lambda asd:asd[1], reverse=False)
print tmp
num = 0
for var in tmp:
    num += var[0]
    poor_num += 1
    if num >= poor_gw:
        break

print 'rich_num=%d, poor_num=%d, deficit_num=%d' % (rich_num, poor_num, deficit_num)
