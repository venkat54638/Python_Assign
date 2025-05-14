#Easy function
#first function
def invert_dictionary(num):
    return {p: q for q, p in num.items()}
#test cases
print(invert_dictionary({"a": 1, "b": 2, "c": 3}))
#second function
def merge_dictionaries(dict1, dict2):
    res = dict1.copy()
    res.update(dict2)
    return res
#test cases
print(merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4}))

#medium function
#first function
def word_frequencies(words):
    words = text.split()  
    freq = {}             
    for i in words:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
#test cases
text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))
#second function
def add_contact(contacts, name, **detail):
    if name in contacts:
        contacts[name].update(detail)
    else:
        contacts[name] = detail
    return contacts
#test cases
contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St") 
print(contacts)

