import os
import time
import random
from bs4 import BeautifulSoup
import requests
class FoodProject:
    def __init__(self, food_kind, store_name, food_name, price, like, time):
        self.food_kind = food_kind
        self.store_name = store_name
        self.food_name = food_name
        self.price = price
        self.like = like
        self.time = time
    
    def print_info(self):
        print(self.time, self.food_kind, self.store_name, self.food_name, self.price, self.like)


def set_food():
    time_time = input('날짜: ')
    food_kind = input('음식종류: ')
    store_name = input('가게이름: ')
    food_name = input('음식명: ')
    price = input('가격: ')
    like = input('평점: ')
    return FoodProject(food_kind,store_name,food_name,price,like,time_time)


def print_portfolio():
    print('1. 오늘 먹은점심 입력하세요')
    print('2. 지금까지 먹은 점심 보여주십쇼')
    print('3. 오늘의 추천')
    print('4. 오늘의 학식')
    print('5. 종료')
    print()
    portfolio = input('고르시오: ')
    return int(portfolio)


def print_food_list(food_list):
    for food in food_list:
        food.print_info()
    

def store_food(food_list):
   
    f = open('food_project.txt', 'wt')
        
    for food in food_list:
        f.write(food.time + '/')
        f.write(food.food_kind + '/')
        f.write(food.store_name + '/')
        f.write(food.food_name + '/')
        f.write(food.price + '/')
        f.write(food.like)
        f.write('\n')
    f.close()


# 이부분은 무조건...... 객체 형식으로 되야된다.
def load_food(food_list):
    f = open('food_project.txt', 'rt')
    lines = f.readlines()
    for i in lines:
        a = i.split('/')
        time = a[0]
        food_kind = a[1]
        store_name = a[2]
        food_name = a[3]
        price = a[4]
        like = a[5][:-2]
        food = FoodProject(food_kind,store_name,food_name,price,like,time)
        food_list.append(food)
    f.close()


def run():
    food_list = []
    if 'food_project.txt'in os.listdir():
        load_food(food_list)
    while 1:
        portfolio = print_portfolio()
        if portfolio ==1:
            food = set_food()
            food_list.append(food)
        elif portfolio == 2:
            print_food_list(food_list)

        elif portfolio == 4:
            print('----------신소재 교직원식당메뉴----------')
            crawling_schoolfood(4)
            print()
            print('----------신소재 학생식당메뉴----------')
            crawling_schoolfood(5)
            print('\n\n\n')
            time.sleep(2)
        elif portfolio == 5:
            store_food(food_list)
            break


def crawling_schoolfood(i):
    url = 'https://www.hanyang.ac.kr/web/www/re'+ str(i)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for link in soup.select('a > img '):
        string = str(link)
        if '[' in string:
            t = string.replace('amp;', '')
            print(t)


if __name__ == "__main__":
    run()

    
# 추후에는, django도 사용해야하고, db연결도 해서
# 입력하는 사람의 name으로
# db접근해서 그사람이 저장한것
# 불러 올수 있도록 하기 일단 여기까지

# 해야할것: 소비한 금액
