def highest_frequency_word_length(input_str):
#     """
#     Calculate the length of the word with the highest frequency in the input string.

#     Parameters:
#     input_str (str): The input string from which to calculate the word length.

#     Returns:
#     int: The length of the word with the highest frequency. Returns 0 if the input string is empty.
#     """
#     words = input_str.split()
#     word_freq = {}

#     for word in words:
#         word_freq[word] = word_freq.get(word, 0) + 1

#     max_freq = max(word_freq.values(), default=0)
    
#     if max_freq == 0:
#         return 0  # No words in the string

#     max_freq_word = [word for word, freq in word_freq.items() if freq == max_freq][0]
    
#     return len(max_freq_word)

# # Example usage:
# input_str = "write write write all the number from from from 1 to 100"
# output = highest_frequency_word_length(input_str)
# print(output)  # Output: 5


# #Testcase_1 
# input_str_1 = "apple orange banana apple orange banana mango"
# output_1 = highest_frequency_word_length(input_str_1)
# print(output_1)  # Output: 6 (for "orange")
# # Explanation: "orange" has the highest frequency, and its length is 6.

# #Testcase_2 
# input_str_2 = "hello world hello world hello world"
# output_2 = highest_frequency_word_length(input_str_2)
# print(output_2)  # Output: 5 (for "hello" or "world")
# # Explanation: Both "hello" and "world" have the same highest frequency, and their length is 5.