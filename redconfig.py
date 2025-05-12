line_port=0
line_source=1

def read_port():
    with open('data.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if line_port < len(lines):
            print(lines[line_port].strip())
        else:
            print("Строка с таким номером не существует.")
        return lines[line_port].strip()

def read_source():
    with open('data.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if line_source < len(lines):
            print(lines[line_source].strip())
        else:
            print("Строка с таким номером не существует.")
        return lines[line_source].strip()