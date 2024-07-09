def number_to_words(n):
  ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", 
          "fourteen", "fiveteen", "sixteen", "seventeen", "eighteen", "nineteen"  ]
  tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  if 1 <= n < 20:
    return ones[n]
  elif 20 <= n < 100:
    return tens[n//10] + ones[n%10]
  elif 100 <= n < 1000:
    return ones[n//100] + "hundred" + ("and" + number_to_words(n%100) if n%100 != 0 else "")
  elif n == 1000:
    return "onethousand"
  
def count_letters_in_range(start, end):
  words_list = [number_to_words(i) for i in range(start, end + 1)]
  letters_count = sum(len(word) for word in words_list)
  return letters_count

total_letters = count_letters_in_range(1, 1000)
print(total_letters)