from functions import filter_operations, sorts_filtered_operations, receives_five_operations

import datetime

filtered_ops = filter_operations('operations.json')
sorted_ops = sorts_filtered_operations(filtered_ops)
top5_ops = receives_five_operations(sorted_ops)

def outputs_information():
    """Выводит информацию согласно поставленной задаче"""
    for op in top5_ops:
        date_str = op['date']
        date = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        print(date.strftime("%d.%m.%Y"))
        print(op["description"])
        if 'from' in op:
            to_text = op['to'][-4:]
            print(f"{op['from'][:6]}{op['from'][6:9]} **** **** **** {op['from'][-4:]} -> Счет **{to_text}")

        else:
            print(f"{op['to'][:5]} *************** {op['to'][-4:]}")
        print(f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['name']}")
        print()

outputs_information()
