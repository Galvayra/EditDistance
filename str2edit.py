from EditDistance.dataset.dataHandler import MyDataHandler

DEFAULT_DISTANCE = 100


class MyEditDistance(MyDataHandler):
    def __init__(self):
        super().__init__()
        if not self.can_load():
            exit(-1)
        self.__table = list()
        self.__len1 = int()
        self.__len2 = int()

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, table):
        self.__table = table

    @property
    def len1(self):
        return self.__len1

    @len1.setter
    def len1(self, _len):
        self.__len1 = _len

    @property
    def len2(self):
        return self.__len2

    @len2.setter
    def len2(self, _len):
        self.__len2 = _len

    def __init_table(self, s1, s2):
        self.len1 = len(s1)
        self.len2 = len(s2)
        self.table = [None] * (self.len2 + 1)

        # initialize __table
        for index in range(self.len2 + 1):
            self.table[index] = [0] * (self.len1 + 1)

        # set first columns
        for i in range(1, self.len2 + 1):
            self.table[i][0] = i

        # set first rows
        for i in range(1, self.len1 + 1):
            self.table[0][i] = i

    def __free(self):
        self.__table = list()
        self.__len1 = int()
        self.__len2 = int()

    def get_distance(self):
        s1 = input("Please input word(EXIT) - ")

        while s1 != "EXIT":
            s1 = s1.lower()

            if s1 in self.data_dict:
                print("\ndictionary has key!")
                print(s1.ljust(15), self.data_dict[s1])
            else:
                distance_list = self.__get_distance_list_in_dict(s1)
                print("\nEdit Distance is", distance_list[0])
                for k in distance_list[1]:
                    print(k.ljust(15), ', '.join(self.data_dict[k]))

            s1 = input("\nPlease Input Word(EXIT) - ")

    def __get_distance_list_in_dict(self, s1):
        distance_list = [DEFAULT_DISTANCE, list()]

        for s2 in self.data_dict:
            self.__init_table(s1, s2)

            for i in range(1, self.len2 + 1):
                for j in range(1, self.len1 + 1):
                    if s1[j - 1] == s2[i - 1]:
                        d = 0
                    else:
                        d = 1

                    self.table[i][j] = min(self.table[i - 1][j - 1] + d,
                                           self.table[i - 1][j] + 1,
                                           self.table[i][j - 1] + 1)

            distance_min = self.table[self.len2][self.len1]

            if distance_list[0] > distance_min:
                distance_list[0] = distance_min
                distance_list[1] = [s2]

            elif distance_list[0] == distance_min:
                distance_list[1].append(s2)

        return distance_list

    def print_table(self):
        print(self.table)
