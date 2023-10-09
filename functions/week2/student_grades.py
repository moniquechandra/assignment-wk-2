import csv

def main():
    records = [
    {'Name': 'Alice', 'Grade': '95.5'},
    {'Name': 'Bob', 'Grade': '75.0'},
    {'Name': 'Charlie', 'Grade': '88.5'},
    {'Name': 'David', 'Grade': '92.0'},
    {'Name': 'Eve', 'Grade': '78.5'},
]
    
    print(average_grade(records))
    print("Student Report\n----------------")
    (filtering(records, 80.0))    

def read_student_records():
    """ 
    Ask for and read a local CSV file to return it to a list of student records (with names and grades).
    """
    file_path = input("Enter the path to the CSV file: ")

# Append every row in CSV file to a list named record
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)

    return records

def average_grade(records):
    """
    Return an average of the grades in the list.
    """
    # Calculate the total of all grades in the list 
    total = sum(float(record['Grade']) for record in records)

    # Calculate the average
    average = total / len(records)
    return f"Average Grade: {average}"

    # return average

def filtering(records, n):
    """
    Return a list of the students' names that have grades more than n in the records.
    """
    # Filter the records for which the grades are greater or equal to n
    filtered_records = [record for record in records if float(record['Grade']) >= n]
    
    for record in filtered_records:
        print(f"Name: {record['Name']}, Grade: {record['Grade']}")

if __name__ == "__main__":
    main()