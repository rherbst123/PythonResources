# 8.  Sentence Capitalizer
# Write a program with a function that accepts a string as an argument and returns a copy 
# of the string with the first character of each sentence capitalized. For instance, if the argu-
# ment is “hello. my name is Joe. what is your name?” the function should return the string 
# “Hello. My name is Joe. What is your name?” The program should let the user enter 
# a string and then pass it to the function. The modified string should be displayed


def capitalize_sentences(user_string):
    #Split the string at the .
    sentences = user_string.split('.')
    #Print out each "Sentence"
    print(sentences)

    #New place for the new sentences to be combined
    result = []

    #for each sentence (each chunk with a .)
    for sentence in sentences:
        stripped = sentence.strip()
        print(f"Stripped sections: {stripped}")
        if stripped:
            # Capitalize first character and add the rest
            #Capitolize the 0 index, add the rest(Done for each stripped)
            result.append(stripped[0].upper() + stripped[1:])
    # return: join the stripped results with a . + if a user string ends with a . add it else add nothing
    return '. '.join(result) + ('.' if user_string.strip().endswith('.') else '')


# get the base string without capitols.
user_string = input("Enter a sentence or two. Do NOT use any caps: ")
print(capitalize_sentences(user_string))