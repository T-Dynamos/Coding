import csv

with open("test.csv", "r") as file:
    DATA = list(csv.reader(file))
    file.close()


def define_result(student_data):
    mark = (
        (float(student_data[-4]) * 0.50)
        + (float(student_data[2]) * 0.40)
        + (float(student_data[3]) * 0.10)
    )
    if (
        student_data[-1].strip()
        == "College of Computer Science & Information Technology"
    ):  # CCSIT ratio
        result = all(
            [
                float(student_data[2]) > 40,
                float(student_data[3]) > 10,
                float(student_data[4]) > 50,
            ]
        )

    elif (
        student_data[-1].strip() == "College of Business Adminstartion"
    ):  # Business ratio
        result = all(
            [
                float(student_data[2]) > 40,
                float(student_data[3]) > 10,
                float(student_data[4]) > 50,
                mark >= 80,
            ]
        )

    elif (
        student_data[-1].strip() == "College of Agricultue and Food Sciences"
    ):  # Agricultue ratio
        result = all(
            [
                float(student_data[2]) > 50,
                float(student_data[3]) > 10,
                float(student_data[4]) > 40,
                mark >= 75,
            ]
        )
    elif student_data[-1].strip() == "College of Law":  # Law ratio
        result = all(
            [
                float(student_data[2]) > 40,
                float(student_data[3]) > 10,
                float(student_data[4]) > 50,
            ]
        )

    return (
        student_data[1].strip() + " : " + ("Accepted" if result == True else "Rejected")
    )


# Sort list using divide and conquer Algorithm
def sort_list(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # divide into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort
        sort_list(left_half)
        sort_list(right_half)

        # Merge the sorted halves back together
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Add any remaining elements from the left or right halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Search element in a list using binary search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def find(data, list_, n=-3):
    for l in list_:
        if float(l[n]) == float(data):
            return l


# Find using binary search
def find_student_algorithm(name, total, college, DATA=DATA):
    # find common college
    college_data = []
    for data in DATA:
        if data[-1].strip() == college:
            college_data.append(data)

    # find same names
    name_common = []
    for n_data in college_data:
        if n_data[1].strip() == name:
            name_common.append(n_data)

    # finally compare marks
    marks = [(float(d[-3]), d) for d in name_common]
    new_marks = [k[0] for k in list(marks)]
    sort_list(new_marks)  # sort using divide and conquer
    tmp = new_marks[binary_search(new_marks, float(total))]
    return find(tmp, name_common, n=-3)


# Bruetforce Algorithm (takes more time)
def find_student_bruteforce(name, total, college, DATA=DATA):
    for data in DATA:
        if (data[1].strip(), data[-3].strip(), data[-1].strip()) == (
            name,
            total,
            college,
        ):
            return data


# Using divide and conquer
print(
    define_result(
        find_student_algorithm(
            "Layla", "80.52", "College of Computer Science & Information Technology"
        )
    )
)
# Using Bruteforce
print(
    define_result(
        find_student_bruteforce(
            "Sarah", "97.925", "College of Computer Science & Information Technology"
        )
    )
)
