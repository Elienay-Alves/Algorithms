def is_anagram(first_string, second_string):
    str1 = "".join(sort(first_string.lower()))
    str2 = "".join(sort(second_string.lower()))

    if len(str1) == 0 or len(str2) == 0:
        return str1, str2, False

    return str1, str2, str1 == str2


def merge(left, right):
    result = []
    index1 = index2 = 0
    while index1 < len(left) and index2 < len(right):
        if left[index1] < right[index2]:
            result.append(left[index1])
            index1 += 1
        else:
            result.append(right[index2])
            index2 += 1
    result += left[index1:]
    result += right[index2:]
    return result


def sort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left = sort(string[:mid])
    right = sort(string[mid:])
    return merge(left, right)
