def open_and_print_file(file):

    try:
        with open(file, "r") as opened_file:
            for line in opened_file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError as errmsg:
        print("There has been an error opening your file!")
        print(errmsg)

    finally:
        print("Execution complete!")


def write_to_file(file, order_item):
    try:
        with open(file, "a") as opened_file:
            for item in order_item_list:
                opened_file.write(item + "\n")

    except FileNotFoundError:
        print("File cannot be found")

    except FileExistsError:
        print("File already exists")

    finally:
        print("Execution complete")


order_item_list = ['Tango', 'Pepsi', '7up']

write_to_file("order.txt", "order_item")
open_and_print_file("order.txt")
