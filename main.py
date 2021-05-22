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
    total_hours, total_minutes, total_seconds = 0, 0, 0

    title_text = ''
    for time_and_duration in time_and_duration_array:
        title_text += f'\n  -  [{time_and_duration["duration"]}]: {time_and_duration["title"]}'

        hours, minutes, seconds = [
            int(x) for x in time_and_duration["duration"].split(':')
        ]
        total_hours += hours
        total_minutes += minutes
        total_seconds += seconds

    additional_minutes, total_seconds = divmod(total_seconds, 60)
    additional_hours, total_minutes = divmod(
        total_minutes + additional_minutes, 60
    )
    total_hours += additional_hours

    project_text = f'- [{str(total_hours).zfill(2)}:{str(total_minutes).zfill(2)}:{str(total_seconds).zfill(2)}] {project}'
    text = project_text + title_text
    print(text)
