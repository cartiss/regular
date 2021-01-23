from pprint import pprint
import re
from collections import Counter
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  contacts_list = contacts_list[1:]


def fix_fio(row):
  i = 0
  for item in row:
    if i < 3:
        split = item.split(' ')
        if len(split) > 1:
            row[1] = split[1]
        if len(split) > 1 and len(split) == 3:
            row[2] = split[-1]
    if i == 0:
        row[0] = split[0]
    i += 1
  return row

def fix_tel(row):
    phone = re.sub(r'(\+7|8)+\s*(\()?(\d{3})(\))?(\s|-)?(\d{3})(-)?(\d{2})(-)?(\d{2})\s*\(?\s*(доб.)*\s*(\d{4})*\s*\)?\s*', r'+7(\3)\6-\8-\10 \11\12', row[5])
    row[5] = phone.strip()
    return row

def smart_append(mylist, row):
  duplicate_found = False
  for item in mylist:
    if item[0] == row[0] and item[1] == row[1]:
      duplicate_found = True
      if row[2]:
        item[2] = row[2]
      if row[3]:
        item[3] = row[3]
      if row[4]:
        item[4] = row[4]
      if row[5]:
        item[5] = row[5]
      if row[6]:
        item[6] = row[6]
      break
  if not duplicate_found:
    mylist.append(row)
  return mylist


contacts_list_fixed = []
for row in contacts_list:
    tmp = fix_fio(row)
    tmp = fix_tel(tmp)
    contacts_list_fixed = smart_append(contacts_list_fixed, tmp)
pprint(contacts_list_fixed)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)