def solution(phone_book):
    phone_number_set = set(phone_book)
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if phone_number[:i] in phone_number_set:
                return False
    return True