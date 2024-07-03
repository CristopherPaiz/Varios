import os
import re
import json

def get_js_and_jsx_files(base_path, exclude_dir):
    js_files = []
    for root, dirs, files in os.walk(base_path):
        if exclude_dir in root:
            continue
        for file in files:
            if file.endswith('.js') or file.endswith('.jsx'):
                js_files.append(os.path.join(root, file))
    return js_files

def get_json_keys(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return set(data.keys())

def find_unmatched_keys(base_path, json_path, exclude_dir):
    js_files = get_js_and_jsx_files(base_path, exclude_dir)
    json_keys = get_json_keys(json_path)
    pattern = re.compile(r't\("([^"]+)"\)')

    unmatched_keys = []

    for file in js_files:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                matches = pattern.findall(line)
                for match in matches:
                    if match not in json_keys:
                        unmatched_keys.append((file, match, i + 1))

    return unmatched_keys

def main():
    base_path = r'C:\Users\acapaizlo\Desktop\Proyectos\React Native\1.0.4 (IOS y Android)'
    json_path = r'C:\Users\acapaizlo\Desktop\Proyectos\React Native\1.0.4 (IOS y Android)\locales\es.json'
    exclude_dir = os.path.join(base_path, 'node_modules')

    unmatched_keys = find_unmatched_keys(base_path, json_path, exclude_dir)

    for file, key, line in unmatched_keys:
        print(f'{file}: "{key}" on line {line}\n')

if __name__ == '__main__':
    main()
