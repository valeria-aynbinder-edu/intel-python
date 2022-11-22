# def my_mul(nums_list: list) -> list:
#     ret_list = []
#     for i in nums_list:
#         ret_list.append(i ** 2)
#     return ret_list
#
#
# print(my_mul([1,2,3,4,5]))


def is_pangram(sentence: str) -> bool:
    alphbet="abcdefghijklmnopqrstuvwxyz"
    sent = sentence.lower()
    for char in alphbet:
        if char not in sent:
            return False
    return True

