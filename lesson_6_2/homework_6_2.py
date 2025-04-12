while True:
    stroka = input("Enter word which contains letter 'h' or 'H' or type 'exit' to finish : ")

    if stroka.lower()== "exit":
        print ("Terminated")
        break


    if "h" in stroka.lower():
        print ("Congrats! You've entered correct word.")
        break
    else:
        print ("Oops! Try another word.")