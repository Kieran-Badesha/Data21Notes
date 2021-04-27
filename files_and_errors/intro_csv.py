import csv

def transform_user_details(csv_name):
    # only save the full name and email address
    try:
        with open(csv_name) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            iterable_csv = iter(csv_name)
            next(iterable_csv)
            filtered_csv = []
            for row in csvreader:
                filtered_csv.append([row[1], row[2], row[-1]])
            return filtered_csv

    except FileNotFoundError:
        print('This File cannot be found')

    except FileExistsError:
        print('This File does not exist')

    finally:
        print('Execution complete')

# transform_user_details("user_details.csv")


def create_csv_file(old_user_details="user_details.csv", new_file_name="new_details.csv"):
    new_user_details = transform_user_details(old_user_details)

    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_details)


create_csv_file()
