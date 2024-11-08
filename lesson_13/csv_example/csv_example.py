import csv


with open("random.csv", newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))
        header = reader[0]


def read_csv_to_set(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return set(tuple(row) for row in reader)


random_rows = read_csv_to_set('random.csv')
random_michaels_rows = read_csv_to_set('random-michaels.csv')


unique_rows = random_rows.union(random_michaels_rows)


with open('result_file.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(unique_rows)

print("Унікальні рядки записані у файл result_file.csv")
