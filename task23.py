#dictionary
dictionary={}
while True:
    print("\nDictionary Management Systems")
    print("1.Add a word")
    print("2.Search for meaning")
    print("3.Display All Words")
    print("4.Update All Words")
    print("5.Delete Word")
    print("6.Exit")

    choice=input("enter your choice:")
    
    if choice=='1':
        word=input("enter the word:")
        meaning=input("enter the meaning:")
        dictionary[word]=meaning
        print("word added successfully")

    elif choice=='2':
        word=input("enter the word to search:")
        if word in dictionary:
            print("meaning:",dictionary[word])
        else:
            print("word not found in dictionary")

    elif choice=='3':
        if word in dictionary:
           print(dictionary)
        else:
           print("dictionary is empty")

    elif choice=='4':
        word=input("enter the word to update meaning:")
        meaning=input("enter the word meaning:")
        dictionary[word]=meaning
        print(dictionary)
        print("meaning updated successfully")

    elif choice=='5':
        word=input("enter the word to delete:")
        dictionary.pop(word)
        print(dictionary)
        print("word deleted successfully")

    elif choice=='6':
        print("exiting program")

    else:
        print("invalid choice")
         


        
