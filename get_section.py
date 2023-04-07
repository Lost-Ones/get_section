from dataclasses import dataclass
from collections import defaultdict
import re

@dataclass
class FileToList():
    file_to_read : str

    def make_list(self):
        file = open(self.file_to_read, "r")
        data = file.read()
        data_into_list = data.split("\n")
        file.close()
        return(data_into_list)

@dataclass
class GetSection():
    text : list
    start : str
    stop : str

    def get_section(self):
        results = defaultdict(list)
        for line in self.text:
            if re.match(f'{self.start}.+', line):
                key = re.match(f'{self.start}.+', line)
                if key:
                    results[key[0]].append(line)
                    go = 1
                    continue
            if results:
                if go == 1:
                    if self.stop not in line:
                        results[key[0]].append(line)
                        continue
                    else:
                        results[key[0]].append(line)
                        go = 0
                        continue
        return results


def main():
    file_to_read = input("Enter the name of the file to read: ")
    start = input("Enter the Start word to search: ")
    stop = input("Enter the End Word of search: ")
    data_list = FileToList(file_to_read=file_to_read)
    text = data_list.make_list()

    data = GetSection(text=text, start=start, stop=stop)
    results = data.get_section()

    for k,v in results.items():
        for line in v:
            print('-->', k, v)

if __name__ == "__main__":
    main()
