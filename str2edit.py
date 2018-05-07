
class MyEditDistance:
    def __init__(self):
        self.__free()

    @property
    def table(self):
        return self.__table

    def __init___table(self, s1, s2):
        self.__len1 = len(s1)
        self.__len2 = len(s2)
        self.__table = [None] * (self.__len2 + 1)

        # initialize __table
        for index in range(self.__len2 + 1):
            self.__table[index] = [0] * (self.__len1 + 1)

        # set first columns
        for i in range(1, self.__len2 + 1):
            self.__table[i][0] = i

        # set first rows
        for i in range(1, self.__len1 + 1):
            self.__table[0][i] = i

    def __free(self):
        self.__table = list()
        self.__len1 = int()
        self.__len2 = int()

    def set_edit_distance(self, s1, s2):
        self.__free()
        self.__init___table(s1, s2)

        for i in range(1, self.__len2 + 1):
            for j in range(1, self.__len1 + 1):
                if s1[j - 1] == s2[i - 1]:
                    d = 0
                else:
                    d = 1

                self.__table[i][j] = min(self.__table[i - 1][j - 1] + d,
                                         self.__table[i - 1][j] + 1,
                                         self.__table[i][j - 1] + 1)

    def print_table(self):
        print(self.table)
