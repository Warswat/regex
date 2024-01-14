import re
import csv


def read_from_csv(scv_filename):
    with open(scv_filename, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def write_to_csv(csv_filename, contacts_list):
    with open(csv_filename, "w", encoding="utf-8", newline="") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


def fix_phone_numbers(contacts_list):
    pattern = r"(\+7|8)\s*\(*(\d{0,3})\)*[\s-]?(\d{0,3})[\s-]?(\d{0,2})[\s-]?(\d+)[\s-]?(\d{0,2})*\s*\(*(доб.)*\s*(\d*)\)*"
    sub_pattern = r"+7(\2)\3-\4-\5 \7\8"
    for line in contacts_list:
        line[0:3] = " ".join(line[:3]).split(" ")[0:3]
        line[5] = re.sub(pattern, sub_pattern, line[5]).rstrip()


def group_records(contacts_list):
    for record in contacts_list:
        for comparable_entry in contacts_list:
            if record == comparable_entry:
                continue
            elif comparable_entry[0] == record[0] and comparable_entry[1] == record[1]:
                for i in range(len(record)):
                    if not record[i]:
                        record[i] = comparable_entry[i]
                contacts_list.remove(comparable_entry)


if __name__ == "__main__":
    contacts_list = read_from_csv("phonebook_raw.csv")
    fix_phone_numbers(contacts_list)
    group_records(contacts_list)
    write_to_csv("phonebook.csv", contacts_list)
