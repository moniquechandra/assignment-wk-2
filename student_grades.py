import csv

def read_student_records():
    """ 
    Ask for and read a local CSV file to return it to a list of student records (with names and grades).
        Returns:
            records (list of dictionaries): an appended list of student records
    """
    file_path = input("Enter the path to the CSV file: ")

# append every row in CSV file to a list named record
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)

    return records

def average_grade(records):
    """
    Return an average of the grades in the list.
        Parameters:
            records (list of dictionaries): a list of students' names and grades
        Returns:
            average (int): a mean of all grades in the list
    """
    # calculate the total of all grades in the list 
    total = sum(float(record['Grade']) for record in records)

    # calculate the average
    average = total / len(records)
    return f"Average Grade: {average}"

    # return average

def filtering(records, n):
    """
    Return a list of the students' names that have grades more than n in the records.
        Parameters:
            records (list of dictionaries): a list of students' names and grades
            n (float): an integer that represents the minimum grade that wants to be filtered
        Returns:
            filtered_records (list of dictionaries): a list of students' names and grades that have grades more than n
    """
    # filter the records for which the grades are greater or equal to n
    filtered_records = [record for record in records if float(record['Grade']) >= n]
    
    for record in filtered_records:
        print(f"Name: {record['Name']}, Grade: {record['Grade']}")

if __name__ == "__main__":
    main()
