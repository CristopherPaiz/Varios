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

def find_unused_json_keys(base_path, json_path, exclude_dir):
    js_files = get_js_and_jsx_files(base_path, exclude_dir)
    json_keys = get_json_keys(json_path)
    pattern = re.compile(r't\("([^"]+)"\)')

    used_keys = set()
    key_usage = {}  # Store file and line number information for each key

    for file in js_files:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                matches = pattern.findall(line)
                for match in matches:
                    used_keys.add(match)
                    if match not in key_usage:
                        key_usage[match] = []
                    key_usage[match].append((file, i + 1))

    unused_keys = json_keys - used_keys
    return unused_keys, key_usage

def main():
    base_path = r'C:\Users\acapaizlo\Desktop\Proyectos\React Native\1.0.5 (IOS y Android) New Stepper'
    json_path = r'C:\Users\acapaizlo\Desktop\Proyectos\React Native\1.0.5 (IOS y Android) New Stepper\locales\es.json'
    exclude_dir = os.path.join(base_path, 'node_modules')

    unused_keys, key_usage = find_unused_json_keys(base_path, json_path, exclude_dir)

    for key in unused_keys:
        print(f'Unused key in JSON: {key}')
        if key in key_usage:
            for file, line in key_usage[key]:
                print(f'  Found in {file} on line {line}')

if __name__ == '__main__':
    main()
