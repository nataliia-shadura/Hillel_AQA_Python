while True:
    stroka = input("Enter string or type 'exit' to finish: ")

    if stroka.lower()== "exit":
        print ("Terminated")
        break


    unique_chars = set(stroka)

    if len(unique_chars) > 10 :
        print ("TRUE (number of unique characters > 10")
    else:
        print ("FALSE (number of unique characters <= 10")