from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
# from vk_api.bot_longpoll import VkBotLongPoll

if __name__ == '__main__':
    print('main is working, time -', datetime.datetime.now())
    get_employees()
    calculate_salary()

