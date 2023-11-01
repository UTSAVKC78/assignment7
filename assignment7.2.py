def process_file(file_name):
    unique_words = set()

    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                unique_words.add(word.lower())

    sorted_words = sorted(unique_words)
    return sorted_words

def main():
    sorted_words = process_file('romeo.txt')
    print(sorted_words)

if __name__ == "__main__":
    main()