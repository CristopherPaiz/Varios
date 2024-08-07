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
    # Modificamos el patrón para que coincida solo con t("...") sin letras antes de la 't'
    pattern = re.compile(r'(?<![a-zA-Z])t\("([^"]+)"\)')
    unmatched_keys = []
    for file in js_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = pattern.finditer(content)
            for match in matches:
                key = match.group(1)
                if key not in json_keys:
                    line_number = content[:match.start()].count('\n') + 1
                    unmatched_keys.append((file, key, line_number))
    return unmatched_keys

def main():
    base_path = r'C:\Users\acapaizlo\Desktop\Proyectos\React Native\1.0.5 (IOS y Android) New Stepper'
    json_path = r'C:\Users\acapaizlo\Desktop\Proyectos\React Native\1.0.5 (IOS y Android) New Stepper\locales\es.json'
    exclude_dir = os.path.join(base_path, 'node_modules')
    unmatched_keys = find_unmatched_keys(base_path, json_path, exclude_dir)
    for file, key, line in unmatched_keys:
        print(f'{file}: "{key}" on line {line}\n')

if __name__ == '__main__':
    main()