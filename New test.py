PAGINATION = input('Ввердите число для диапазона: ')
PAGINATION = int(PAGINATION.strip())

for item in range(1, PAGINATION):
    print(f'Число {item}')

test = ['git', 'hub']
for item in test:
    print(item, end=' ')