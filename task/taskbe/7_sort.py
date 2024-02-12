def hyp(sequence):
    
    helwords = sequence.split('-')
    sorted_words = sorted(helwords)
    result = '-'.join(sorted_words)
    return result

sequence = input("Enter a hyphen-separated sequence of words:")

sorted_sequence = hyp(sequence)
print(f"Sorted Sequence:{sorted_sequence}")
