from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def phone():
    pattern_phone = r"(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})(\s?)\(?(доб\.)?(\s?)(\d+)?(\)?)"
    new_pattern_phone = r"+7(\2)-\3-\4-\5 \7\9"
    for column in contacts_list:
        column[5] = re.sub(pattern_phone, new_pattern_phone, column[5])
    return


def correct_name():
    name_pattern = r'([А-Я])'
    new_pattern_name = r' \1'
    for column in contacts_list[1:]:
        line = column[0] + column[1] + column[2]
        if len((re.sub(name_pattern, new_pattern_name, line).split())) == 3:
            column[0] = re.sub(name_pattern, new_pattern_name, line).split()[0]
            column[1] = re.sub(name_pattern, new_pattern_name, line).split()[1]
            column[2] = re.sub(name_pattern, new_pattern_name, line).split()[2]
        elif len((re.sub(name_pattern, new_pattern_name, line).split())) == 2:
            column[0] = re.sub(name_pattern, new_pattern_name, line).split()[0]
            column[1] = re.sub(name_pattern, new_pattern_name, line).split()[1]
            column[2] = ''
    return

def table():
    contacts = [['lastname','firstname','surname','organization','position','phone','email']]
    list_of_contacts = []
    for column in contacts_list[1:]:
        surname = column[0]
        name = column[1]
        second_name = column[2]
        organization = column[3]
        job = column[4]
        phone = column[5]
        email = column[6]
        list_of_contacts = [surname,name,second_name,organization,job,phone,email]
        for names in contacts:
            if names[0] == surname:
                if names[1] == name:
                    if second_name != '':
                        names[2] = second_name
                    if organization != '':
                        names[3] = organization
                    if job != '':
                        names[4] = job
                    if phone != '':
                        names[5] = phone
                    if email != '':
                        names[6] = email
                    list_of_contacts = []
                else:
                  continue
        if list_of_contacts != []:
            contacts.append(list_of_contacts)
    return contacts

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    correct_name()
    phone()
    table()
    datawriter.writerows(table())



