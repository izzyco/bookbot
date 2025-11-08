def get_num_words(text):
    return len(text.split())

def get_map_num_words(text):
    split_words = text.split()
    char_map = {}
    for word in split_words:
        for char in word:
            lower_char = char.lower()
            if lower_char in char_map:
                char_map[lower_char] += 1
            else:
                char_map[lower_char] = 1
    
    return char_map

def sort_on(char_map):
    return char_map["nums"]

def sort_char_map(char_map):
    # Convert to char/num value 
    double_kv_char_map = []
    for k, v in char_map.items():
        double_map = { "char": k, "nums": v}
        double_kv_char_map.append(double_map)
    
    double_kv_char_map.sort(reverse=True, key=sort_on)
    return double_kv_char_map
