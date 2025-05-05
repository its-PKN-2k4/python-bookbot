# Function for getting the number of words in a string
def get_word_count(text):
    strip_text = text.split()
    return len(strip_text)

# Function for getting a dictionary of all characters in the string with number of apperance
def get_char_frequency(text):
    lower = text.lower() # Convert string to lowercase to avoid counting lowercase and uppercase of same letters

    char_dict = {}

    for c in lower:
        if c in char_dict:
            char_dict[c] += 1 # If c already in dict, add 1 to frequency counter
        else:
            char_dict[c] = 1 # Otherwise, initiate frequency counter to 1

    return char_dict

# Function for getting the value of 'num' key for comparison
def get_count(d):
    return d["num"]

def get_sorted_dicts(dictionary):
    dict_list = []

    for key, value in dictionary.items():
        dict = {}
        dict["char"] = key
        dict["num"] = value
        dict_list.append(dict) # Add new sub-dictionary to end of list

    dict_list.sort(key=get_count, reverse=True) # Sort from most frequent to least frequent
    return dict_list
