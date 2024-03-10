def hashtag():
    s = input("Enter a phrase: ")
    cleaned_s = ''.join(char for char in s if char.isalnum())

    hashtag = '#' + ''.join(word.capitalize() for word in cleaned_s.split())

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

print(hashtag())
