def calculate_metrics(file_path, comment_indicator="#"):
    loc = 0  # Lines of Code
    ploc = 0  # Physical Lines of Code
    comments = 0  # Comment lines

    # Read the code from the file and calculate metrics
    with open(file_path, 'r') as file:
        lines = file.readlines()
        loc = len(lines)
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith(comment_indicator):
                comments += 1
            elif stripped_line != "":
                ploc += 1

    return loc, ploc, comments

# File paths
qa_exam_code_file_path = r"C:\Users\SAMSUNG\OneDrive\Documents\qafile\friend file\test_Fr1.py"
java_example_file_path = r"C:\Users\SAMSUNG\OneDrive\Documents\qafile\friend file\java_test.java" 

# Calculate metrics for QA exam code
qa_loc, qa_ploc, qa_comments = calculate_metrics(qa_exam_code_file_path)
print("QA Exam Code Snippet Metrics")
print(f"LOC (Lines of Code): {qa_loc}")
print(f"PLOC (Physical Lines of Code): {qa_ploc}")
print(f"Comments: {qa_comments}")

# Calculate metrics for Java Enterprise Hello World example
java_loc, java_ploc, java_comments = calculate_metrics(java_example_file_path, "//")
print("\nJava Enterprise Hello World Example Metrics")
print(f"LOC (Lines of Code): {java_loc}")
print(f"PLOC (Physical Lines of Code): {java_ploc}")
print(f"Comments: {java_comments}")
