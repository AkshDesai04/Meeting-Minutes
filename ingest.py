import re

def parse_text_file(file_path):
    entries = []
    print("Printing File")
    with open(file_path, 'r') as file:
        entry = {}
        for line in file:
            print(line)
            if '-->' in line:
                start, end = re.findall(r'(\d+:\d+:\d+\.\d+)', line)
                entry['timing'] = (start, end)
            elif line.strip():
                entry['speaker'] = line.strip()
                text = next(file).strip()
                entry['text'] = text
                entry.setdefault('timing', None)  # Ensure 'timing' key exists
                entries.append(entry)
                entry = {}
    print("Printed File")
    return entries

def format_output(entries):
    output_list = []
    for entry in entries:
        output_list.append({
            'timing': entry['timing'],
            'speaker': entry['speaker'],
            'text': entry['text']
        })
    return output_list    

def ingest_target(file_path):
    file_path = file_path
    entries = parse_text_file(file_path)
    output_list = format_output(entries)
    return output_list
