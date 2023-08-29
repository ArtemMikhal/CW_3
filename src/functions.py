import json


def filter_operations(file_name):
    """Фильтрует только операции со статусом EXECUTED(выполненные)"""

    with open(file_name, encoding='utf-8') as f:
        data = json.load(f)

    executed_operations = []

    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            executed_operations.append(operation)

    return executed_operations


def sorts_filtered_operations(ops):
    """Сортирует отфильтрованные операции по дате в порядке убывания(от новых к старым)"""
    return sorted(ops, key=lambda x: x['date'], reverse=True)


def receives_five_operations(sort):
    """Выбирает первые 5 операций"""
    last_five_operations = sort[:5]
    return last_five_operations
