"""
Paskal uchburchagi
Paskal uchburchagining dastlabki n ta qatorini toping.

💡 Paskal uchburchagi har bir element o'zidan yuqoridagi 2 ta element yig'indisiga teng.
https://telegra.ph/file/aa4bc22f821489292609c.gif

Misol 1:
Kiritish: 2
Natija: [[1], [1,1]]

Misol 2:
Kiritish: 5
Natija: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""


def generate_row(prev: list) -> list:
    next_ = [1]
    for i in range(len(prev) - 1):
        next_.append(prev[i] + prev[i + 1])
    next_.append(1)
    return next_


def generate(n: int) -> list:
    if n == 0:
        return []

    row = [1]
    lst = [row]

    for _ in range(n - 1):
        row = generate_row(row)
        lst.append(row)

    return lst


if __name__ == "__main__":
    n = 5
    res = generate(n)
    print(res)
