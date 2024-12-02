def is_safe(report):
    """
    Checks if a given report is safe based on the conditions:
    1. The levels are either all increasing or all decreasing.
    2. Any two adjacent levels differ by at least one and at most three.
    """
    # Calculate differences between adjacent levels
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are either positive or negative
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    return is_increasing or is_decreasing


def count_safe_reports(filename):
    """
    Reads the reports from the input file and counts how many are safe.
    """
    safe_count = 0

    with open(filename, 'r') as file:
        for line in file:
            # Convert the report to a list of integers
            report = list(map(int, line.split()))
            # Check if the report is safe
            if is_safe(report):
                safe_count += 1

    return safe_count


# Replace 'input.txt' with the path to your input file
input_file = "../input.txt"
safe_reports = count_safe_reports(input_file)

print(f"Number of safe reports: {safe_reports}")
