import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint as pp
import json

HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'


def get_headers():
    return Headers(browser='firefox', os='win').generate()


def get_html_text():
    return requests.get(HOST, headers=get_headers()).text


def pars():

    my_list = []
    soup = BeautifulSoup(get_html_text(), features='lxml')
    id_main_content = soup.find(id='a11y-main-content')
    for info in id_main_content:
        id_user_content = info.find(class_='g-user-content')
        if id_user_content is not None:
            id_user_content_text = id_user_content.text
            if 'Django' in id_user_content_text or 'django' in id_user_content_text or 'Flask' in id_user_content_text or 'flask' in id_user_content_text:
                main_info = info.find(class_='vacancy-serp-item-body__main-info')
                if main_info is not None:
                    link_info = main_info.find(class_='serp-item__title')
                    link_info_text = link_info.text
                    link = link_info.get('href')
                salary_info = info.find('span', class_='bloko-header-section-3')
                if salary_info is not None:
                    salary = (salary_info.text).replace('\u202f', ' ')
                vacancy_info = info.find('a', class_='bloko-link bloko-link_kind-tertiary')
                if vacancy_info is not None:
                    vacancy = (vacancy_info.text).replace('\xa0',' ')
                city_info = info.find(class_='vacancy-serp-item__info')
                if city_info is not None:
                    city = (city_info.text).replace((vacancy_info.text),'').replace('\xa0', ' ')
                schedule_info = info.find(class_='search-result-label search-result-label_work-schedule')
                if schedule_info is not None:
                    schedule = 'Возможно из дома'
                else:
                    schedule = 'Не указано'
                my_list.append({
                        "Ссылка: ": link,
                        "Вакансия: ": link_info_text,
                        "Зарплата: ": salary,
                        "Город: ": city,
                        "Название фирмы: ": vacancy,
                        "Удаленка: ": schedule
                    })
    return my_list

def create_json():
    with open('data.json', 'w', encoding='utf=8') as f:
        json.dump(pars(), f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    create_json()