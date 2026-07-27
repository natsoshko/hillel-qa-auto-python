import csv
import json
import xml.etree.ElementTree as ET
import pathlib
import logging

'''Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх. Результат запишіть у файл result_<your_second_name>.csv'''

SECOND_NAME = "Soshko"

base = pathlib.Path(__file__).parent
csv_dir = base / "work_with_csv"

file1 = csv_dir / "random-michaels.csv"
file2 = csv_dir / "r-m-c.csv"
result_file = base / f"result_{SECOND_NAME}.csv"
#print(base)

all_rows = []
unique_rows = set()
for file in (file1, file2):
    with open(file, "r", newline="", encoding="utf-8") as csvfile:
        reader = list(csv.reader(csvfile))
        all_rows += reader
        for row in reader:
            unique_rows.add(tuple(row))  # tuple можна додати в set


with open(result_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(sorted(unique_rows))

print(f"All rows: {len(all_rows)}")
print(f"Unique rows: {len(unique_rows)}")
print(f"Duplicates: {len(all_rows) - len(unique_rows)}")
print()

'''Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log'''

base = pathlib.Path(__file__).parent
json_dir = base / "work_with_json"
log_file = base / f"json__{SECOND_NAME}.log"

logger_v1 = logging.getLogger(__name__)
logger_v1.setLevel(logging.ERROR)
handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger_v1.addHandler(handler)

for json_file in sorted(json_dir.glob("*.json")):
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            json.load(f)
            print(f"{json_file.name}: is valid")
    except json.JSONDecodeError as e:
        logger_v1.error(f"Invalid JSON file: {json_file.name}. "
        f"Line: {e.lineno}, Column: {e.colno}, Error: {e.msg}")
        print(f"{json_file.name}: is invalid (check logfile {log_file.name})")
print()

'''Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо'''

base = pathlib.Path(__file__).parent
xml_file = base / "work_with_xml" / "groups.xml"

logger_v2 = logging.getLogger(__name__)
logger_v2.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s | %(message)s"))
logger_v2.addHandler(handler)

def func_find_by_group_number(xml_path, group_number):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.findtext("number")
        if number is not None and number == str(group_number):
            incoming = group.find("timingExbytes/incoming")
            # logger_v2.info("group %s: timingExbytes/incoming = %s", group_number, incoming)

            if incoming is not None:
                logger_v2.info("group %s: timingExbytes/incoming = %s", group_number, incoming.text)
            else:
                logger_v2.info("group %s: no timingExbytes/incoming", group_number)
            return incoming

    logger_v2.info("group %s: not found", group_number)
    return None


func_find_by_group_number(xml_file, 0)
func_find_by_group_number(xml_file, 5)
func_find_by_group_number(xml_file, 4)
func_find_by_group_number(xml_file, 1)
func_find_by_group_number(xml_file, 13)