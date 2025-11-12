from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

#RANDOM ASS NOTATION, SHORTCUT FOR MAKING A LINE MOVE UP OR NOT IS ALT ARROW up or down


def test():

    # content_lorem = get_file_content("calculator", "lorem.txt")
    # if len(content_lorem) > 10000:
    #     exit("it was longer than 10000 characters so we got prob")

    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


if __name__ == "__main__":
    test()
