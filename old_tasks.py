def first_task():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    answer = []
    for id, dicts in enumerate(geo_logs):
        if 'Россия' in list(dicts.values())[0]:
            answer.append(dicts)

    return answer


def second_task():
    ids = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}

    new_ids = set(ids['user1']) | set(ids['user2']) | set(ids['user3'])
    return new_ids

def third_task():
    stats = {
        'facebook': 55,
        'yandex': 120,
        'vk': 115,
        'google': 99,
        'email': 42,
        'ok': 98
    }

    max_val = max(stats.values())
    for name_company, stats_company in stats.items():
        if stats_company == max_val:
            # print(name_company, stats_company)
            return name_company, stats_company
#
# third_task()