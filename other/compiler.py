import json

def compiler(json_file, readme_file):

    result = ''

    with open(json_file, 'r') as f:
        data = json.load(f)['config']

        for i in range(len(data)): 
            result += f'\n<br/>\n\n## <b>{data[i]["title"]}</b>\n\n<br/>\n\n'
            snippets_list = data[i]["snippets"]

            for j in range(len(snippets_list)): 
                result += f'### `{snippets_list[j]["name"]}` - {snippets_list[j]["description"]}\n<details>\n\t<summary>Preview code</summary>\n\t<img src="https://raw.githubusercontent.com/kah3vich/Nano-Snippets/main/assets/code/{data[i]["title"].lower()}/{snippets_list[j]["name"]}.png" alt="code:{snippets_list[j]["name"]}">\n</details>\n\n<br/>\n\n'


    with open(readme_file, 'w') as f:
        f.write(str(result))

    print('Done ✅')

compiler('snippets.json', 'readme.md')