class Solution(object):
    SEEK_SIZE = 1

    def get_size(self, f_object):
        f_object.seek(0, 2)
        # size
        return f_object.tell()

    def reverse_file(self, filepath):
        with open(filepath, 'rb') as f:
            current = self.get_size(f)

            while current >= 0:
                f.seek(current)
                yield f.read(self.SEEK_SIZE)
                current -= self.SEEK_SIZE


if __name__ == "__main__":
    sol = Solution()

    with open("output.txt", "wb") as wr:
        for data in sol.reverse_file("input.txt"):
            wr.write(data)
