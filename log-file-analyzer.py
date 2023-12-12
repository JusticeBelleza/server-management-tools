import re

def analyze_log_file(file_path):
    error_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
                print(line.strip())

    print(f"Total Errors Found: {error_count}")

if __name__ == "__main__":
    LOG_FILE_PATH = "/path/to/your/logfile.log"
    analyze_log_file(LOG_FILE_PATH)
