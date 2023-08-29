from functions import filter_operations, sorts_filtered_operations, receives_five_operations
import datetime

filter_operations = filter_operations('operations.json')
sort_list = sorts_filtered_operations(filter_operations)
five_operations = receives_five_operations(sort_list)

for op in five_operations:
    date = datetime.datetime.fromisoformat(op['date'])
    print(date.strftime("%d.%m.%Y"))

    print(op['description'])

    if 'from' in op:
        to_text = op['to'][-4:]
        print(f"{op['from'][:6]}{op['from'][6:9]}** **** {op['from'][-4:]} -> Счет **{to_text}")
    else:
        print(f"{op['to'][:5]} *************** {op['to'][-4:]}")

    print(f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['name']}")

    print()


