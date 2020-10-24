favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
coders = ['jen', 'edward', 'peter']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"{coder.title()}, thank you for taking poll!")
    else:
        print(f"{coder.title()}, need to take a poll.")
