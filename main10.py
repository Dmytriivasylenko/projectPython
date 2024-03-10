def project1():
    s = input("Enter some word: ")
    cleaned_s = ''.join(char for char in s if char.isalnum() or char.isspace())
    words = cleaned_s.split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

# Приклад
print(project1())
