def hashtag(s):
    hashtag = '#' + ''.join(word.capitalize() for word in s.split() if word.isalnum())
    return hashtag[:140]

print(hashtag('Python Community'))
print(hashtag('i like python community!'))
print(hashtag('Should, I. subscribe? Yes!'))
