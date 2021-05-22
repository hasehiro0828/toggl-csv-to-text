import csv
import sys
from typing import Dict, List, TypedDict, cast

TypeAliasProject = str


class CsvRow(TypedDict):
    Project: str
    Client: str
    Title: str
    Duration: str


class TitleAndDuration(TypedDict):
    title: str
    duration: str


filename = sys.argv[1]

records: Dict[TypeAliasProject, List[TitleAndDuration]] = {}
with open(filename, encoding='utf-8-sig') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        csv_row = cast(CsvRow, row)

        time_and_duration = TitleAndDuration(
            title=csv_row['Title'], duration=csv_row['Duration']
        )
        records.setdefault(csv_row['Project'], []).append(time_and_duration)

for project, time_and_duration_array in records.items():
    text = f'- {project}'
    for time_and_duration in time_and_duration_array:
        text += f'\n  [{time_and_duration["duration"]}]: {time_and_duration["title"]}'
    print(text)
