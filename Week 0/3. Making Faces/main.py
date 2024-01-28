def convert():
    text = input("Enter the text to be converted: ").replace(":)","🙂").replace(":(", "🙁")
    return text

def main():
    print(convert())

main()