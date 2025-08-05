# 6. File Analysis
# Write a program that reads the contents of two text files and compares them in the following ways:
# • It should display a list of all the unique words contained in both files.
# • It should display a list of the words that appear in both files.
# • It should display a list of the words that appear in the first file but not the second.
# • It should display a list of the words that appear in the second file but not the first.
# • It should display a list of the words that appear in either the first or second file, but not both.
# Hint: Use set operations to perform these analyses.

def get_words_from_file(filename):
    
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            # Remove punctuation and split by whitespace
            words = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in content).split()
            return set(words)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return set()
    except Exception as e:
        print(f"An error occurred: {e}")
        return set()

def file_analysis(file1, file2):
   
    # Get sets of unique words from both files
    words1 = get_words_from_file(file1)
    words2 = get_words_from_file(file2)
    
    if not words1 or not words2:
        return
    
    # 1. All unique words in both files (union)
    all_unique_words = words1.union(words2)
    print("\n1. All unique words contained in both files:")
    print_word_set(all_unique_words)
    
    # 2. Words that appear in both files (intersection)
    words_in_both = words1.intersection(words2)
    print("\n2. Words that appear in both files:")
    print_word_set(words_in_both)
    
    # 3. Words in first file but not second (difference)
    words_only_in_first = words1.difference(words2)
    print("\n3. Words that appear in the first file but not the second:")
    print_word_set(words_only_in_first)
    
    # 4. Words in second file but not first (difference)
    words_only_in_second = words2.difference(words1)
    print("\n4. Words that appear in the second file but not the first:")
    print_word_set(words_only_in_second)
    
    # 5. Words in either file but not both (symmetric difference)
    words_in_either_not_both = words1.symmetric_difference(words2)
    print("\n5. Words that appear in either file but not both:")
    print_word_set(words_in_either_not_both)

def print_word_set(word_set):
    
    if not word_set:
        print("  (No words found)")
        return
        
    # Print in alphabetical order
    for word in sorted(word_set):
        print(f"  {word}")

def main():
    file1 = r'/home/riley/Documents/GitHub/RileyPython/Chapter9/Files/UniqueWords.txt'
    file2 = r'/home/riley/Documents/GitHub/RileyPython/Chapter9/Files/SecondFile.txt'
    
    file_analysis(file1, file2)

if __name__ == "__main__":
    main()
