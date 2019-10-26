import sys


class Cout:
    def __lshift__(self, other):
        """
        Prints `str(other)`.
        Flushes the buffer if other is `endl`.
        >>> cout << 1000 << "hellos to the world !" << endl;
        :param other: object
        :return: Cout
        """
        sys.stdout.write(str(other))
        if other == endl:
            sys.stdout.flush()
        return self

    def __repr__(self):
        return ""

    def __str__(self):
        return ""


cout = Cout()
endl = "\n"
