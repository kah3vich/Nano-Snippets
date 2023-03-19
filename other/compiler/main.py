import json
import os
import re

#| Variables

#|💡 ru: Получаем из системы путь до папки с сниппетами.
#|💡 en: We get the path to the folder with snippets from the system.

current_dir = os.getcwd().replace('other\\compiler', 'snippets')

#| Functions

#|💡 ru: Получаем массив с объектами всех путей до сниппетов.
#|💡 en: We get an array with objects of all paths to snippets.

def get_subfolder_files():
    subfolder_files = []

    for subdir in os.listdir(current_dir):
        if os.path.isdir(os.path.join(current_dir, subdir)):
            obj = {"name": subdir, "files": []}

            for file in os.listdir(os.path.join(current_dir, subdir)):
                if os.path.isfile(os.path.join(current_dir, subdir, file)):
                    obj["files"].append(file)

            subfolder_files.append(obj)

    return subfolder_files

#|💡 ru: Удаление из строки 4 последних символа.
#|💡 en: Removing the last 4 characters from a string.

def remove_first_last_lines(text):
    lines = text.split('\n')
    lines = lines[1:-4]
    result = '\n'.join(lines)

    return result

#|💡 ru: Создание файла со всеми данными об сниппетах.
#|💡 en: Creating a file with all data about snippets.

def create_config_snippets():
    text = '{\n'

    for item in get_subfolder_files():
        name = item['name']
        list_files = item['files']
        text += f'\n\t//| {name}\n'
        
        for file in list_files:
            with open(f'{current_dir}/{name}/{file}', 'r', encoding="utf8") as input_file:
                    file_text = f'\n{remove_first_last_lines(input_file.read())}\n'
                    pattern = r"(.*)(\n[^\n]*)$"
                    replacement = r"\1,\2"

                    text += re.sub(pattern, replacement, file_text)

    text += '\n}\n\n//| 🔥 by kah3vich 🔥\n'

    with open('./cache/_config.json', 'w', encoding="utf-8") as output_file:
        output_file.write(text)
    with open('../../snippets/index.json', 'w', encoding="utf-8") as output_file:
        output_file.write(text)

#|💡 ru: Создание файла со всеми данными об сниппетами.
#|💡 en: Creating a file with all the snippet data.

def create_config_readme():
    config_text = '{\n\t"config": ['

    for item in get_subfolder_files():
        name = item['name']
        list_files = item['files']
        config_text += '\n\t\t{'
        config_text += f'\n\t\t\t"title": "{name}",\n\t\t\t"snippets": ['
        for file in list_files:
            config_text += '\n\t\t\t\t{'
            with open(f'{current_dir}/{name}/{file}', 'r', encoding="utf8") as input_file:
                    input_file_text = input_file.read()

                    name_text = re.search(r'"prefix": "(.*?)"', input_file_text).group(1)
                    description_text = re.search(r'"description": "(.*?)"', input_file_text).group(1)
                    config_text += f'\n\t\t\t\t\t"name": "{name_text}",\n\t\t\t\t\t"description": "{description_text}"'
            config_text += '\n\t\t\t\t},'
        config_text += '\n\t\t\t],\n\t\t},'

    config_text += '\n\t]\n}'


    with open('./cache/_readme.json', 'w', encoding="utf-8") as output_file:
        output_file.write(config_text)

#|💡 ru: Создание файла со всеми данными об сниппетами для создания readme.md файла.
#|💡 en: Creating a file with all the snippet data to create a readme file.

def compiler_readme(json_file, readme_file):
    result = ''

    with open('./main.md', 'r') as main_text:
        result += f'{main_text.read()}\n'

    with open(json_file,'r') as f:
        s = f.read()
        s = s.replace('\t','')
        s = s.replace('\n','')
        s = s.replace(',}','}')
        s = s.replace(',]',']')
        data = json.loads(s)['config']

        for i in range(len(data)): 
            result += f'\n<br/>\n\n## <b>{data[i]["title"]}</b>\n\n<br/>\n\n'
            snippets_list = data[i]["snippets"]

            for j in range(len(snippets_list)): 
                result += f'### `{snippets_list[j]["name"]}` - {snippets_list[j]["description"]}\n<details>\n\t<summary>Preview code</summary>\n\t<img src="https://raw.githubusercontent.com/kah3vich/Nano-Snippets/main/assets/code/{data[i]["title"].lower()}/{snippets_list[j]["name"]}.png" alt="code:{snippets_list[j]["name"]}">\n</details>\n\n'


    with open(readme_file, 'w') as f:
        f.write(str(result))

#| Result

if __name__ == "__main__":

    print('\n')

    #! 1. Create config snippets

    try: 
        create_config_snippets()
        print('create_config_snippets - Done ✅')
    except Exception: 
        print(f'❌ create_config_snippets: {Exception}')

    #! 2. Create config readme 

    try: 
        create_config_readme()
        print('create_config_readme - Done ✅')
    except Exception: 
        print(f'❌ create_config_readme: {Exception}')

    #! 3. Create finally readme file 

    try: 
        compiler_readme('./cache/_readme.json', "../../readme.md")
        print('compiler_readme - Done ✅')
    except Exception: 
        print(f'❌ compiler_readme: {Exception}')

print('\nNice ✅')