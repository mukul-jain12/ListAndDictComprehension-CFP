"""
    @File :   dictionary_comprehension.py
    @Author : mukul
    @Date :   22-12-2021
"""


class DictComprehension:
    @staticmethod
    def problem_one(diction):
        """
            desc: Find all the numbers between 1–500 that are divisible by 6
        """
        even_diction = {name: value for (name, value) in diction.items() if value % 2 == 0}
        print("Dictionary having even values :", even_diction)

    @staticmethod
    def problem_two(diction):
        """
            desc: Assign even and odd value to name
        """
        new_dict = {name: ('even' if value % 2 == 0 else 'odd') for (name, value) in diction.items()}
        print(new_dict)


if __name__ == '__main__':
    dict_comp = DictComprehension()

    dictionary = {'mukul': 38, 'shivam': 54, 'dibyesh': 21, 'gunjan': 45}
    dict_comp.problem_one(dictionary)
    dict_comp.problem_two(dictionary)
