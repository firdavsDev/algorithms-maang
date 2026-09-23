# Har bir "Node" — bitta element va "keyingisiga" ishora (pointer)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # ro'yxat boshini ko'rsatib turadi

    def append(self, value):
        # O(n) - oxirigacha yurish kerak (head'da tail saqlansa O(1) bo'lardi)
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        # O(1) - faqat head'ni almashtiramiz, yurish shart emas
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, target_value, value):
        # O(n) - target_value'ni topguncha yurish kerak
        current = self.head
        while current is not None:
            if current.value == target_value:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError(f"{target_value} topilmadi")

    def delete(self, value):
        # O(n) - o'chiriladigan node'ni topguncha yurish kerak
        # (head bo'lsa O(1))
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def search(self, value):
        # O(n) - eng yomon holatda oxirigacha yurish kerak
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# Foydalanish
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()
# Natija: 10 -> 20 -> 30 -> None

ll.prepend(5)
ll.print_list()
# Natija: 5 -> 10 -> 20 -> 30 -> None

ll.insert_after(20, 25)
ll.print_list()
# Natija: 5 -> 10 -> 20 -> 25 -> 30 -> None

ll.delete(10)
ll.print_list()
# Natija: 5 -> 20 -> 25 -> 30 -> None

print(ll.search(25))  # True
print(ll.search(100))  # False


# Big O (vaqt murakkabligi)
# ------------------------------------------------------
# Amal          | Linked List | Array (Python list)
# ------------------------------------------------------
# append (oxir)  | O(n)       | O(1) - amortized
# prepend (bosh) | O(1)       | O(n) - hammasini surish kerak
# insert_after   | O(n)       | O(n)
# delete         | O(n)       | O(n)
# search         | O(n)       | O(n)
# index bo'yicha | O(n)       | O(1) - to'g'ridan-to'g'ri manzil
#   olish        |            |   (index 0 dan boshlanishi shu yerda ishlaydi)
# ------------------------------------------------------
# Xulosa: Linked List boshiga qo'shish/o'chirishda kuchli,
# lekin index bo'yicha tezkor kirish kerak bo'lsa - array yaxshiroq,
# chunki index orqali manzilni bevosita hisoblab bo'ladi (arr[i]),
# Linked List'da esa har doim boshidan yurish kerak.


# =========================================================
# Nega va qayerda kerak bo'ladi?
# =========================================================
# Linked List ishlatiladi, chunki:
# - hajmi oldindan noma'lum va tez-tez o'zgarib turadi (array kabi
#   qayta joylashtirish/surish shart emas)
# - boshiga/oxiriga tez-tez qo'shish/o'chirish kerak bo'lganda
# - xotira parchalangan (fragmented) bo'lsa ham ishlaydi - array kabi
#   BITTA katta ketma-ket joy talab qilmaydi
#
# Amaliy misollar:
# - Stack va Queue'ning ichki implementatsiyasi (masalan, Python'da
#   collections.deque aslida doubly linked list asosida ishlaydi)
# - "Undo/Redo" tarixi - har bir amal keyingisiga ulanadi
# - Musiqa pleyeridagi "next/previous" navbat (playlist)
# - Katta hujjatlarni tahrirlash (text editor) - matn bo'laklarini
#   o'rtaga qo'shish/o'chirish tez-tez sodir bo'ladi
# - Hash Table'dagi "chaining" - bir xil hash'ga tushgan elementlarni
#   bog'lab saqlash uchun
# - Operatsion tizimda xotira boshqaruvi (bo'sh xotira bloklarini
#   bog'langan ro'yxat sifatida kuzatish)
#
# Qachon Linked List YAXSHI TANLOV EMAS:
# - Index bo'yicha tez-tez element olish kerak bo'lsa (arr[5] kabi)
# - Element'lar soni ko'p o'zgarmaydigan va tez qidirish kerak
#   bo'lgan holatlarda (array yoki hash table yaxshiroq)
