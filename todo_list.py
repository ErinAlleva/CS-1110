# Alex Hicks (awh4kc)

todo_list = []

def read_todo_list():
   datafile = open("todo_list.txt", "r")
   for line in datafile:
       todo_list.append(line.strip())

def add_to_list(item):
   todo_list.append(item)

def write_todo_list_file():
   datafile = open("todo_list.txt", "w")
   for item in todo_list:
       datafile.write(item)
       datafile.write("\n")
   datafile.close()

def print_todo_list():
    print()
    print()
    print("Your TODO List")
    print("--------------")
    for i in range(len(todo_list)):
        print(str(i) + ") " + todo_list[i])
    print()

def main():
    done = False
    read_todo_list()

    while not done:
        print_todo_list()
        print("Select an item to remove it, A to add a new item, Q to quit")
        choice = input("Choice?: ")
        if choice.isdigit():
            del todo_list[int(choice)]
        elif choice == 'A':
            new_item = input("New item?: ")
            add_to_list(new_item)
        elif choice == 'Q':
            write_todo_list_file()
            done = True

main()
