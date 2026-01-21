
def find_longest_word(filename):
    try:
        with open(filename, "r") as f:
            words = f.read().split()
            return max(words, key=len)
    except FileNotFoundError:
        print("Error: File not found.")
        return None


# Main Program
filename = input("Enter file name: ")
longest = find_longest_word(filename)

if longest:
    print("Longest word in the file is:", longest)