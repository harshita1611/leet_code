class Solution(object):
    def plusOne(self, digits):
        str_list = []
        for i in digits:
            str_list.append(str(i))
        numbers = int("".join(str_list))
        numbers = str(numbers + 1)
        new_list = []
        for i in numbers:
            new_list.append(int(i))
        return new_list
