class Solution(object):
    """
    If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate.
    Give a count as well as print the strings.

     For example:
    Input: "1123". You need to general all valid alphabet codes from this string.

    Output List
    aabc //a = 1, a = 1, b = 2, c = 3
    kbc // since k is 11, b = 2, c= 3
    alc // a = 1, l = 12, c = 3
    aaw // a= 1, a =1, w= 23
    kw // k = 11, w = 23

    """
    def is_valid(self, param):
        param = int(param)

        index_limit = 26
        if param > index_limit or param <= 0:
            return False

        return True

    def generate_permutations(self, data):
        str_start_index = ord("a") - 1
        acc = ""

        for chr_index in data:
            if self.is_valid(int(chr_index)):
                acc += chr(int(chr_index)+str_start_index)
        yield acc

    def merge_results(self, prefix, results):
        out_list = []

        for res in results:
            out_list.append("{}{}".format(prefix, res))

        return out_list

    def generate_permutation(self, input_str):

        str_start_index = ord("a") - 1
        test_str = ""
        res = []

        while len(input_str) > 0:
            test_str += input_str[0]
            input_str = input_str[1:]

            if self.is_valid(test_str):
                res_prefix = chr(int(test_str) + str_start_index)
                sub_result = self.generate_permutation(input_str)

                if len(sub_result) == 0:
                    res += res_prefix
                else:
                    res += self.merge_results(res_prefix, sub_result)
        return res


if __name__ == "__main__":
    sol = Solution()

    for item in sol.generate_permutation("112312"):
        print(item)
