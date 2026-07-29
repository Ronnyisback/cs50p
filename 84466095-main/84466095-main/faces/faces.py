def main():
    a=input()
    b=convert(a)
    print(b)
def convert(text):
    text=text.replace("Hello :)", "Hello 🙂")
    text=text.replace("Goodbye :(", "Goodbye 🙁")
    return(text)
main()





