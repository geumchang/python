# import json

# a = dict()
# a['name'] = 'sanghi'
# a['price'] = 4900
# a['brand'] = 'mcdonald'

# #b 는 json(인코딩)
# b = json.dumps(a, indent = 4) #indent 들여쓰기(tab)

# # c는 딕셔너리(디코딩)
# c = json.loads(b)

# print(b)

# print(c)

# f1 = open('mc.json', 'r')  # 절대 경로?
# f2 = open('output.txt', 'w')

# txt = f1.read()
# f2.write(txt)
# print(txt)

# f2.close()
# f1.close()

# txt = ''
# with open('mc.json', 'r') as f1 :
#     txt = f1.read()

# with open('output.txt', 'w') as f2 :
#     f2.write(txt)

# import json
# txt = ''
# with open('mc.json','r') as f1 :
#     txt = f1.read()


# di = json.loads(txt)

# with open('output.txt', 'w') as f2:
#     f2.write(''.join(str(x) for x in di['widget']['window'].keys()) + '\n')
#     f2.write(''.join(str(x) for x in di['widget']['image'].values()) + '\n')
#     f2.write(''.join(str(x) for x in di['widget']['text'].items()) + '\n')


# print(di['widget']['window'].keys())
# print(di['widget']['image'].values())
# print(di['widget']['text'].items())


# import json
# import requests

# url = "https://api.tvmaze.com/singlesearch/shows?q=narcos&embed=episodes"
# r = requests.get(url) # url 응답받아 r 변수에 할당

# # .text ---> json 객체
# print(r.text)

# class Zergling:
#     def __init__(self):
#         self.hp = 20
#         self.mana = 50
    
#     def run(self):
#         print('뛴다')
#         self.hp -= 1
#         self.mana += 1
    
#     def show_status(self):
#         print(f'hp : {self.hp} mana : {self.mana}')

# z1 = Zergling()
# z2 = Zergling()
# z1.run()
# z1.show_status()
# for i in range(5):
#     z2.run()
# z2.show_status()

# class GameMachine:
#     def __init__(self):
#         self.coin = 0 # 현재 보유 코인
    
#     def input_coin(self, amount):
        
#         if(amount > 5):
#             return
#         if(self.coin + amount > 10):
#             return
#         self.coin += amount
    
#     def play_game(self):
#         if(self.coin < 1):
#             print('코인을 넣어주세요')
#             return
#         self.coin -= 1
#         print('게임 재밌다')

#     def show_status(self):
#         print(f'남아있는 코인은 {self.coin}입니다')

# gm = GameMachine()
# gm.input_coin(6)
# gm.show_status()
# gm.play_game()
# gm.show_status()

# class PTIRE:
#     def run(self):
#         print('런')

# class STIRE(PTIRE):
#     def ran(self):
#         print('랜')

# class STIRE2(PTIRE):
#     def ron(self):
#         print('론')

#     def run(self):
#         print('런런')

# a = STIRE2()
# a.run()
# a.ron()

# b = STIRE()
# b.run()
# b.ran()

import numpy as np

lst = [1, 2, 3, 4, 5]
result_lst = lst * 2
print(result_lst)


arr = np.array([1,2,3,4,5])
result_arr = arr * 2
print(result_arr)