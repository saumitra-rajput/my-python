import json
# import pdb
import argparse

class LogAnalyzer: # creating class
    """
    class has 2 things
    data members(variables) & member functions (functions)
    """

    # init function
    # when you create class's object  __init__ functions will be called automatically
    # NOTE: not all functions will be called eg read_log, analyze, write_jso

    def __init__(self, file_name, output_file):
        self.file_name = file_name
        self.output_file = output_file

    def read_log(self):
        with open(self.file_name, "r") as file:
            return file.readlines()

    def write_json(self, counts):
        with open(self.output_file, "w+") as json_file:
            json.dump(counts, json_file)

    def analyze(self):
        # pdb.set_trace()
        log_count = {
                "INFO": 0,
                "WARNING": 0,
                "ERROR": 0
                }
        lines = self.read_log()
        for line in lines:
            if "INFO" in line:
                log_count.update({"INFO": log_count["INFO"]+1})
            elif "WARNING" in line:
                log_count.update({"WARNING": log_count["WARNING"]+1})
            elif "ERROR" in line:
                log_count.update({"ERROR": log_count["ERROR"]+1})
            else:
                continue

        self.write_json(log_count)

# Adding CLI part using python module argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file")
parser.add_argument("--out")

args = parser.parse_args()


# calling class functions
log1 = LogAnalyzer(args.file, args.out) # creating object of class here
log1.analyze()

print("\nGenerating output file...")
print("\nJSON file is Created Successfully")
