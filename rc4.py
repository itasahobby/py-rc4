class Rc4:
    def __init__(self, key: bytearray) -> None:
        # Incrementing array generation
        inc_array = []
        for i in range(256):
            inc_array.append(i)
        # Attribute definition
        self.s_table = bytearray(inc_array)
        self.i = 0
        self.j = 0
        # Initialization
        temp = 0
        for i in range(256):
            j = (temp + self.s_table[i] + key[i % len(key)] ) % 256
            # Swap(S[i], S[j])
            self.s_table[i], self.s_table[j] = self.s_table[j], self.s_table[i]

    def __next(self) -> int:
        self.i = (self.i + 1) % 256
        self.j = (self.j + self.s_table[self.i]) % 256
        # Swap(S[i], S[j])
        self.s_table[self.i], self.s_table[self.j] = self.s_table[self.j], self.s_table[self.i]
        next_t = (self.s_table[self.i] + self.s_table[self.j]) % 256
        return next_t

    def encrypt(self, b_data) -> bytearray:
        output = []
        for b_char in b_data:
            k = self.__next()
            output.append(b_char ^ k)
        result = bytearray(output)
        return result

    def decrypt(self, data) -> bytearray:
        return self.encrypt(data)
