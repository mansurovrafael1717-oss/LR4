import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    result = []

    with open(INPUT_FILENAME, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for row in reader:
            result.append(row)

        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as jsonfile:
            json.dump(result, jsonfile, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
