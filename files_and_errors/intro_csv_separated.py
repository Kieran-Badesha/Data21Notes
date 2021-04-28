import csv

# Extract function
import pprint


def extract_csv_file(csv_name: str, delim: str=',') -> list:

    try:
        with open(csv_name) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=delim)
            csv_list = list(csvreader)
        return csv_list

    except FileNotFoundError:
        print('Sorry the file name you entered cannot be found')

    except FileExistsError:
        print('Sorry the file name you entered does not exist')

    finally:
        print("Extraction complete")


# Transform function
def transform_csv_file(csv_list):

    try:
        # Only save the Full name and Email address
        full_name_emails = []
        for item in csv_list:
            full_name_emails.append([item[i] for i in [1, 2, 4]])

        return full_name_emails
    finally:
        print('Transform complete')


# Load function
def load_csv_file(new_file_name: str, new_file_list: list):
    try:
        with open(new_file_name, 'w') as new_file:
            csv_writer = csv.writer(new_file, lineterminator='\n')
            csv_writer.writerows(new_file_list)
    finally:
        print('Load complete')


csv_reader = extract_csv_file('user_details.csv')
new_file_list = transform_csv_file(csv_reader)
load_csv_file('new_user_details.csv', new_file_list)
