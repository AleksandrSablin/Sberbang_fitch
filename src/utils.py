import json
from datetime import datetime


def get_data(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def sorted_oprations(operations):
    s_operations = sorted(operations, key=lambda date: date.get("date", "no data"), reverse=True)
    return s_operations


def five_last_operations(operations):
    five_last_operations = []
    for i in operations[1:]:
        if len(five_last_operations) < 5:
            if i["state"] == "EXECUTED":
                five_last_operations.append(i)
    return five_last_operations


def get_card_number(operations):
    for i in operations:
        try:
            key_from = i['from']
            card_number_get = key_from.split(" ")
            card_number = card_number_get[-1]
            if len(card_number) == 16:
                hidden_num = f"{''.join(card_number_get[:-1])} {card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
                i['from'] = hidden_num
            else:
                hidden_num = f"{''.join(card_number_get[:-1])} {card_number[0:4]} {card_number[4:6]}** **** **** {card_number[-4:]}"
                i['from'] = hidden_num
        except KeyError:
            continue
    return operations


def get_sent_number(operations):
    for i in operations:
        key_to = i['to']
        num_get = key_to.split(" ")
        sent_card_num = num_get[-1]
        hidden_sent_num = f"{''.join(num_get[:-1])} **{sent_card_num[-4:]}"
        i['to'] = hidden_sent_num
    return operations


def get_date(operations):
    for i in operations:
        get_out_date = datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f")
        changed_date = get_out_date.strftime('%d.%m.%Y')
        i['date'] = changed_date
    return operations
