from utils import *

def main():
    operations = get_data("operations.json")
    operations = sorted_oprations(operations)
    operations = five_last_operations(operations)
    operations = get_date(operations)
    operations = get_sent_number(operations)
    operations = get_card_number(operations)

    for operation in operations:
        print(f"{operation['date']} {operation['description']}\n"
              f"{operation.get('from', 'Номер счёта')} -> {operation['to']}\n"
              f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
              f"\n")


# print(sorted_oprations(get_data(os.path.join('tests', 'test_file.json'))))

if __name__ == "__main__":
    main()