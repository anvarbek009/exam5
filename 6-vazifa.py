class Alphabet:
    def __init__(self):
        self.current = ord('a') - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= ord('z'):
            raise StopIteration
        self.current += 1
        return chr(self.current)

alphabet = Alphabet()
for letter in alphabet:
    print(letter, end=' ')
