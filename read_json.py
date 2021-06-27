import json

file_name = "test_json.json"

def process_file():
    file_ptr = open(file_name, "r")
    outer_dic = json.load(file_ptr)
    lang_list = outer_dic.get("lang_list")
    thelist = []
    for lang in lang_list:
        name = lang.get("name")
        year = lang.get("year")
        print("Language: ", name)
        print("Year: ", year)
        author = lang.get("author")
        
        fn = author.get("fn")
        ln = author.get("ln")
        print("Author: ", fn, ln)
        print()
        thelist.append(name)
    thelist.sort()
    print("The list of languages in sorted order is: ", thelist)
def main():
    process_file()
main()