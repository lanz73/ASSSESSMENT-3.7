# Assessment 3.7: Sorting Algorithms
# Name: Lanz Renier A. Casinao
# Sorting Method: Bubble Sort (Ascending Alphabetical Order)

def bubble_sort(array):
    """Sort letters alphabetically using Bubble Sort."""
    sorted_array = array.copy()
    n = len(sorted_array)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_array[j] > sorted_array[j + 1]:
                sorted_array[j], sorted_array[j + 1] = (
                    sorted_array[j + 1],
                    sorted_array[j]
                )

    return sorted_array


# Full name: Lanz Renier A. Casinao
# Spaces and punctuation are excluded.
# Duplicate letters are discarded, keeping each letter's first occurrence.
full_name = "Lanz Renier A. Casinao"

unsorted_array = []
for character in full_name.upper():
    if character.isalpha() and character not in unsorted_array:
        unsorted_array.append(character)

sorted_array = bubble_sort(unsorted_array)

print("Name:", full_name)
print("Sorting Method: Bubble Sort")
print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
