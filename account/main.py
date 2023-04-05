from account.build.build import last_five_executed_operations, print_info

# запуск программы, функция выводит пять последних успешных операций
print_info(last_five_executed_operations('account/requests/operations.json'))
quit()
