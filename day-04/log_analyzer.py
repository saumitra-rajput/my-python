import json
# import pdb

def read_log():
    with open("app.log", "r") as file:
        return file.readlines()

def analyze(lines):
    # pdb.set_trace()
    log_count = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
            }
    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO": log_count["INFO"]+1})
        elif "WARNING" in line:
            log_count.update({"WARNING": log_count["WARNING"]+1})
        elif "ERROR" in line:
            log_count.update({"ERROR": log_count["ERROR"]+1})
        else:
            continue
    return log_count

def write_json(counts):
    with open("output.json", "w+") as json_file:
        json.dump(counts, json_file)

lines = read_log()
counts = analyze(lines)
print(counts)

print("\nGenerating output.json...\n")
write_json(counts)
print("\noutput.json Created Successfully\n")
