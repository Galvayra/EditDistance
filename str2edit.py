

class MyEditDistance:
    def __init__(self):
        self.__free()

    def __init_table(self, s1, s2):
        self.len1 = len(s1)
        self.len2 = len(s2)
        self.table = [None] * (self.len2 + 1)

        # initialize table
        for index in range(self.len2 + 1):
            self.table[index] = [0] * (self.len1 + 1)

        # set first columns
        for i in range(1, self.len2 + 1):
            self.table[i][0] = i

        # set first rows
        for i in range(1, self.len1 + 1):
            self.table[0][i] = i

    def __free(self):
        self.table = list()
        self.len1 = int()
        self.len2 = int()

    def set_edit_distance(self, s1, s2):
        self.__free()
        self.__init_table(s1, s2)

        for i in range(1, self.len2 + 1):
            for j in range(1, self.len1 + 1):
                if s1[j - 1] == s2[i - 1]:
                    d = 0
                else:
                    d = 1

                self.table[i][j] = min(self.table[i - 1][j - 1] + d, self.table[i - 1][j] + 1, self.table[i][j - 1] + 1)

    def print_table(self):
        print(self.table)
