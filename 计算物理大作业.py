#!/usr/bin/python
#coding:utf8
 
import random
import time
 
def get_dice():
    return random.randint(1,6)
 
def the_open(player_dice,computer_dice):
    print '双方开：'
    time.sleep(1)
    print '玩家：' + str(player_dice)
    time.sleep(1)
    print '对手：' + str(computer_dice)
    time.sleep(1)
 
def every_game(player_money,computer_money):
    print 'Get Ready~~~'
    time.sleep(1)
    print '3!'
    time.sleep(1)
    print '2!'
    time.sleep(1)
    print '1!'
    time.sleep(1)
    print 'Go!'
    time.sleep(2)
    print "双方筹码："
    print '玩家：' + str(player_money)
    print '对手：' + str(computer_money)
    time.sleep(2)
    print '玩家掷点：',
    time.sleep(1)
    player_dice = get_dice()
    print '您得到的点数为' + str(player_dice)
    time.sleep(2)
    print '对手掷点：',
    time.sleep(1)
    computer_dice = get_dice()
    print '对手掷点完毕！'
    time.sleep(1)
    result = raw_input('玩家方先下注，是否下注？[y/N]')
    if result.lower() == 'y':
        while True:
            player_bets = input('请选择下注筹码数目：[1-{0}]'.format(player_money))
            if player_bets >= 1 and player_bets <= player_money:
                break
        print '玩家下注{0}'.format(player_bets)
        time.sleep(1)
        print '对手思考中...',
        time.sleep(2)
        if random.choice('yn') == str('y'):
            computer_bets = random.randint(1,computer_money)
            print '对手下注：{0}'.format(computer_bets)
            time.sleep(1)
            the_open(player_dice,computer_dice)
            if player_dice==1 and computer_dice==6:
                print '恭喜反杀！玩家胜！玩家赢得筹码{0}'.format(computer_money)
                player_money += computer_money
                computer_money -= computer_money
            elif player_dice==6 and computer_dice==1:
                print '对手胜！玩家输掉筹码{0}'.format(player_money)
                player_money -= player_money
                computer_money += player_money
            elif player_dice > computer_dice:
                print '玩家胜！玩家赢得筹码{0}'.format(computer_bets)
                player_money += computer_bets
                computer_money -= computer_bets
            elif player_dice == computer_dice:
                print '平局！双方收回各自筹码！'
            else:
                print '对手胜！玩家输掉筹码{0}'.format(player_bets)
                player_money -= player_bets
                computer_money += player_bets
        else:
            print '对手·放弃下注！玩家收回自己的筹码！'
            time.sleep(1)
            the_open(player_dice,computer_dice)
        
    else:
        print '玩家放弃下注，本局放弃！'
        time.sleep(1)
        the_open(player_dice,computer_dice)
    return [player_money,computer_money]
 
def play_game():
    print '---------------汪凌涛诚意出品，童叟无欺---------------'
    print '掷骰子游戏开始！'
    player_money = 100
    computer_money = 100
    time.sleep(1)
    while player_money != 0 and computer_money != 0:
        money_list = every_game(player_money,computer_money)
        player_money = money_list[0]
        computer_money = money_list[1]
    if player_money == 0:
        print '游戏失败！'
    else:
        print '恭喜获胜！'
 
if __name__ == '__main__':
    play_game()

