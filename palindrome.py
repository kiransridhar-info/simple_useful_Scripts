def palindrom_checker():
    input_word = input("Enter a string which is to be checked for palindrome")

    if (len(input_word) % 2) == 0:
        print("%s is not a palindrome" % input_word)
    else:
        for index in range(int(len(input_word)/2)):
            if((input_word[index].lower()) == (input_word[-1-index].lower())):
                continue
            else:
                print("%s is not a palindrome" %input_word)
                break

        print("%s is a palindrome" %input_word)

if __name__ == '__main__':
    palindrom_checker()