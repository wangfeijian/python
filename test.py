def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    num_first = text.find(begin)
    num_second = text.find(end)
    print(num_first)
    print(num_second)
    if num_first > num_second and num_second != -1:
        return ''
    elif num_first == -1 and num_second == -1:
        return text
    elif num_first != -1 and num_second == -1:
        print(text[(num_first + len(begin)):])
    elif num_first == -1 and num_second != -1:
        return text[:num_second]
    elif num_first < num_second and num_first != -1:
        return text[(num_first + len(begin)):num_second]
between_markers('No [b]hi', '[b]', '[/b]')