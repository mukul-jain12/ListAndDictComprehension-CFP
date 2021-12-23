"""
    @File :   list_comprehension.py
    @Author : mukul
    @Date :   22-12-2021
"""


class ListComprehension:
    @staticmethod
    def problem_one(max_num):
        """
            desc: Find all the numbers between 1–500 that are divisible by 6
        """
        number = [num for num in range(1, max_num) if num % 6 == 0]
        print("List of Numbers is :", number)

    @staticmethod
    def problem_two(paragraph):
        """
            desc: Count the number of spaces in a string
        """
        count_space = [word for word in paragraph if word == " "]
        print("Number of spaces in the paragraph is :", len(count_space))


if __name__ == '__main__':
    list_comp = ListComprehension()

    max_range = 500
    para = "A paragraph is a series of related sentences developing a central idea, called the topic. Try to " \
           "think about paragraphs in terms of thematic unity: a paragraph is a sentence or a group of " \
           "sentences that supports one central, unified idea. Paragraphs add one idea at a time to your " \
           "broader argument. "

    list_comp.problem_one(max_range)
    list_comp.problem_two(para)
