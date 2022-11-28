import csv
import os

# if __name__ == "__main__":
#     relative_path = "./data/alice_in_wonderland.txt"
#     absolute_path = "/Users/valeria/src/biosense/meeting3/files/data/alice_in_wonderland.txt"
#     test_path = "../my_test.py"

    # file_handler = open(relative_path, 'r')
    # print(type(file_handler))
    # content = file_handler.read()
    # print(content)
    # file_handler.close()

    # context manager
    # with open(relative_path) as file_handler:
    #     content = file_handler.read()

    # read text file and count lines
    # with open(relative_path) as file_handler:
    #     counter = 0
    #     for line in file_handler:
    #         counter += line.count("Alice")
    #         # print(line)
    #     print(counter)

    # with open(relative_path) as file_handler:
    #     print(file_handler.read(15))
    #     print(file_handler.read(20))
        # file_handler.seek()


    # reading csv - basic
    # with open("./data/AAPL.csv", "r") as fh:
    #     # skip first line
    #     fh.readline()
    #     for i, line in enumerate(fh):
    #         if i != 0:
    #             row_list = line.split(",")
    #             print(f"The Open price in date {row_list[0]} is: {row_list[2]}")


    # reading from csv using DictReader
    # with open("./data/AAPL.csv") as fh:
    #     reader = csv.DictReader(fh)
    #
    #     print(type(reader))
    #     for row in reader:
    #         print(row)
    #         # print(f"The Open price in date {row['Date']} is: {row['Open']}")


    # write to file
    # with open("./data/my_file1.txt", "w") as fh:
    #     fh.write("Sun")

    # with open("./data/my_file1.txt", "a") as fh:
    #     fh.write(" is shining")


    # reading csv - basic
    # with open("./data/AAPL.csv", "r") as fh:
    #     for line in fh:
    #         row_list = line.split(",")
    #         print(f"The Open price in date {row_list[0]} is: {row_list[2]}")


    # reading from csv using DictReader
    # with open("./data/AAPL.csv") as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         print(f"The Open price in date {row['Date']} is: {row['Open']}")

    # root: Prints out directories only from what you specified.
    # dirs: Prints out sub-directories from the root.
    # files: Prints out all files from root and directories.

    # iterate over files in
    # that directory
    # "/data"
    # /users/data/alice.txt
    # C:\\Users\fcg\sdfs\alice.txt
    # for root, dirs, files in os.walk("data"):
    #     # print(f"root: {root} | dirs: {dirs} | files: {files}")
    #     for filename in files:
    #         # print(f"{root}/{filename}")  # not recommended
    #         print(os.path.join(root, filename))  # the correct way


    # print(os.sep)
    # print(os.path.exists(relative_path))
    # print(os.path.exists("./filess.py"))
    # print(os.path.abspath("./data/alice_in_wonderland.txt"))
    # print(os.path.relpath("/Users/valeria/src/zeiss/meeting3/files/data/alice_in_wonderland.txt", "."))
    # print(os.path.split("/Users/valeria/src/biosense/meeting3/files/data/alice_in_wonderland.txt"))
    # print(os.path.splitext(relative_path))


    # os.makedirs("./data/new_data/bla/bla")
    # os.rmdir()
    # os.remove()

    # header = "first_name, last_name\n"
    # line1 = "valeria, aynbinder\n"
    # line2 = "brad, pitt\n"
    # rows = [header, line1, line2]
    # with open("./data/new_data/bla/bla/test.csv", "w") as fh:
    #     fh.writelines(rows)


    # with open(relative_path, 'rb') as file_handler:
    #     content = file_handler.read()

