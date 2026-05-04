def read_log(): # this function will read the app.log files
    with open("app.log", "r") as file:
        return file.readlines()


def analyze(lines):
    log_count = {
            "INFO": 0,
            "ERROR": 0
            }
    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO": log_count["INFO"]+1})
        elif "ERROR" in line:
            log_count.update({"ERROR": log_count["ERROR"]+1})
        else:
            continue
    return log_count

lines = read_log() # calling the read_log function

logdata = analyze(lines)

print(logdata)
