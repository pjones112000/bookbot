def occurrencs(file_text,char):
   return file_text.lower().count(char.lower())

def wc(file_text):
    wordlist = file_text.split()
    return len(wordlist)

def main():
    with open("books/frankenstein.txt") as f:
       file_contents = f.read()
    
#    print(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(wc(file_contents),"words found in the document")

    print("The 'a' character was found",occurrencs(file_contents,"A"),"times")
    print("--- End report ---")
main()

