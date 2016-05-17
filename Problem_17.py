def word(num):
    last_two = num % 100
    remaining = num // 100
    third = remaining % 10
    remaining //= 10
    fourth = remaining % 10

    f_in_words = ""
    t_in_words = ""
    lt_in_words = ""

    if fourth != 0:
        f_in_words = translation_20[fourth] + "thousand"
    if third != 0:
        t_in_words = translation_20[third] + "hundred"
    if last_two != 0:
        if last_two < 20:
            lt_in_words = translation_20[last_two]
        else:
            lt_in_words = translation_tens[last_two // 10] + translation_20[last_two % 10]
    if (third == 0) & (fourth == 0):
        return lt_in_words
    elif last_two == 0:
        return f_in_words + t_in_words
    else:
        return f_in_words + t_in_words + "and" + lt_in_words


translation_20 = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                  10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                  17: "seventeen", 18: "eighteen", 19: "nineteen"}
translation_tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

Sum = 0
for i in range(1, 1001):
    Sum += len(word(i))

print(Sum)