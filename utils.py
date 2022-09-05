def print_lines(file, n=10):
    with open(file, 'rb') as datafile:
        lines = datafile.readlines()
    for line in lines[:n]:
        print(line)

def gen_result(result):
    return result[0]['generated_text']

def parse_results(result):
    pass
