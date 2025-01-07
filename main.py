file_content = ""
def word_count(str):
    return len(str.split(" "))
def char_count(str):
    result = {}
    lstr = (str.lower())
    for i in set(list(lstr)):
        result[i] = 0
    for i in list(lstr):
        result[i] += 1
    return result
def main():
    with open("./books/frankenstein.txt") as f:
        file_content = f.read()
    print(file_content)
    print ("Word count: " + str(word_count(file_content)) + " words")
    c = char_count(file_content)
    for i in c:
        print(f"Character '{i}' was found {c[i]} times")
main()