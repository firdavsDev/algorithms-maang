# Linked List - 0 dan To'liq O'rganish

## 1. Hayotiy misollar

### 🚗 Navbat (Queue) - Avtomobil yuvish
Tasavvur qiling, avtomobil yuvish joyida navbat bor:
```
[BMW] -> [Toyota] -> [Nexia] -> [Spark] -> None
```

**Nima sodir bo'ladi?**
- Yangi mashina keldi → oxiriga qo'shamiz
- Birinchi mashina yuvildi → boshidan o'chiramiz
- O'rtadan mashina ketdi → o'chirib, bog'lovchi o'zgartiramiz

**Array bilan muammo:**
```python
# Array bilan
cars = ["BMW", "Toyota", "Nexia", "Spark"]
# Boshidan o'chirish uchun HAMMA elementlarni siljitish kerak!
cars.pop(0)  # Juda sekin! O(n)
```

**Linked List bilan oson:**
```python
# Linked List bilan
def remove_first(head):
    return head.next  # Faqat bitta o'zgartirish! O(1)
```

### 📱 Brauzer tarixi (History)
Chrome, Safari brauzerlarida "Orqaga" tugmasi:
```
[google.com] -> [facebook.com] -> [instagram.com] -> [youtube.com] -> None
```

**Nima uchun Array emas?**
- Har safar yangi sahifa ochsangiz, eskisini o'chirish kerak
- Orqaga borishda elementlar o'zgaradi
- Hajmi oldindan noma'lum

### 🎵 Musiqa pleyeri (Playlist)
Spotify, Apple Music'da qo'shiqlar ro'yxati:
```
[Song1] -> [Song2] -> [Song3] -> [Song4] -> None
```

**Afzalliklar:**
- Qo'shiq qo'shish/o'chirish tez
- Shuffle qilish oson
- Xotira tejamkor

## 2. Linked List vs Array - Taqqoslash

| Operatsiya | Array | Linked List |
|------------|--------|-------------|
| **Boshiga qo'shish** | O(n) - hamma elementni siljitish | O(1) - faqat pointer o'zgartirish |
| **Oxiriga qo'shish** | O(1) - agar joy bo'lsa | O(n) - oxirigacha borish |
| **O'rtadan o'chirish** | O(n) - elementlarni siljitish | O(1) - pointer o'zgartirish |
| **Qidirish** | O(n) | O(n) |
| **Index orqali kirish** | O(1) | O(n) |
| **Xotira** | Kam | Ko'p (pointer uchun) |

## 3. Qachon Linked List ishlatish kerak?

### ✅ Linked List yaxshi:

**1. Ko'p qo'shish/o'chirish operatsiyalari**
```python
# Masalan: Chat dasturi
class Message:
    def __init__(self, text, next=None):
        self.text = text
        self.next = next

# Yangi xabar qo'shish - tez!
def add_message(head, text):
    new_message = Message(text)
    new_message.next = head
    return new_message
```

**2. Hajmi oldindan noma'lum**
```python
# Masalan: Foydalanuvchi kiritayotgan ma'lumotlar
def collect_user_input():
    head = None
    while True:
        data = input("Ma'lumot kiriting (stop = to'xtatish): ")
        if data == "stop":
            break
        head = add_to_start(head, data)
    return head
```

**3. Xotira tejash kerak**
```python
# Katta ma'lumotlar uchun
class LargeData:
    def __init__(self, data):
        self.data = data  # Katta ma'lumot
        self.next = None

# Array esa barcha joyni oldindan band qiladi
```

### ❌ Array yaxshi:

**1. Index orqali tez kirish kerak**
```python
# Masalan: O'quvchilar ro'yxati
students = ["Ali", "Vali", "Guli"]
print(students[1])  # Tez! O(1)
```

**2. Matematik operatsiyalar**
```python
# Masalan: Matematik hisoblashlar
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # Array bilan oson
```

**3. Tartiblash kerak**
```python
# Masalan: Baholarni tartiblash
grades = [85, 92, 78, 95]
grades.sort()  # Array bilan oson
```

## 4. Real dasturlashda misollar

### 🌐 Web Development
```python
# Django/Flask - Middleware chain
class Middleware:
    def __init__(self, name, next_middleware=None):
        self.name = name
        self.next = next_middleware
    
    def process_request(self, request):
        print(f"{self.name} processing...")
        if self.next:
            return self.next.process_request(request)
        return request

# Authentication -> CORS -> Logging -> App
auth = Middleware("Auth")
cors = Middleware("CORS", auth)
logging = Middleware("Logging", cors)
```

### 💾 Ma'lumotlar bazasi
```python
# Database transaction log
class Transaction:
    def __init__(self, operation, data, next=None):
        self.operation = operation
        self.data = data
        self.next = next
        self.timestamp = time.time()

# Har bir operatsiya linked list ga qo'shiladi
def log_transaction(head, operation, data):
    new_transaction = Transaction(operation, data)
    new_transaction.next = head
    return new_transaction
```

### 🎮 Game Development
```python
# O'yin ob'ektlari ro'yxati
class GameObject:
    def __init__(self, name, x, y, next=None):
        self.name = name
        self.x = x
        self.y = y
        self.next = next
    
    def update(self):
        # Ob'ekt holatini yangilash
        pass

# Barcha ob'ektlarni yangilash
def update_all_objects(head):
    current = head
    while current:
        current.update()
        current = current.next
```

## 5. Katta kompaniyalarda ishlatilishi

### 🔍 Google
- **Search results** - qidiruv natijalari
- **Chrome tabs** - brauzer yorliqlar

### 📘 Facebook
- **News feed** - yangiliklar lentasi
- **Friends list** - do'stlar ro'yxati

### 🎬 Netflix
- **Watch history** - ko'rish tarixi
- **Recommendations** - tavsiyalar

### 💰 Banking
- **Transaction history** - to'lov tarixi
- **Account operations** - hisob operatsiyalari

## 6. Qachon ishlatmaslik kerak?

### ❌ Yomon holatlar:
1. **Index orqali tez kirish kerak** - Array ishlatang
2. **Matematik hisoblashlar** - Array/List ishlatang
3. **Kichik ma'lumotlar** - Array soddaroq
4. **Xotira cheklangan** - Array kam joy egallaydi

### ✅ Yaxshi holatlar:
1. **Ko'p qo'shish/o'chirish** - Linked List
2. **Hajmi noma'lum** - Linked List
3. **Navbat/Stek** - Linked List
4. **Katta ma'lumotlar** - Linked List

## 7. Xulosa

**Linked List ishlatishning sabablari:**
- Tez qo'shish/o'chirish (O(1))
- Moslashuvchan hajm
- Xotira tejamkor (katta ma'lumotlar uchun)
- Navbat/Stek uchun ideal

**Eslab qoling:**
> "Agar siz ko'p qo'shish/o'chirish operatsiyalari qilasiz va index orqali kirish kerak emas bo'lsa - Linked List ishlatang!"


## 1. Linked List nima?

Tasavvur qiling, sizda **zanjir** bor. Har bir halqa keyingi halqaga bog'langan. Xuddi shunday, Linked List ham zanjir kabi - har bir element (node) keyingi elementga bog'langan.

### Oddiy Array vs Linked List:

**Array (massiv):**
```
[1][2][3][4][5]  - barcha elementlar yonma-yon joylashgan
```

**Linked List:**
```
[1] -> [2] -> [3] -> [4] -> [5] -> null
```

## 2. Node nima?

Node - bu Linked List ning asosiy qismi. Har bir node 2 ta narsani saqlaydi:
- **Data** - bizning ma'lumotimiz (masalan, raqam)
- **Next** - keyingi node ga yo'nalish (pointer)

```python
class ListNode:
    def __init__(self, val):
        self.val = val        # Bu yerda ma'lumot saqlanadi
        self.next = None      # Bu yerda keyingi node ga yo'nalish
```

## 3. Linked List qanday yaratiladi?

```python
# Birinchi node yaratamiz
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Ularni bog'laymiz
node1.next = node2
node2.next = node3
node3.next = None  # Oxirgi node

# Natija: 1 -> 2 -> 3 -> null
```

## 4. Linked List ni ko'rish (Traversal)

```python
def print_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next
```


## 5. Asosiy operatsiyalar

### 5.1 Boshiga element qo'shish:
```python
def add_to_start(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node  # Yangi head qaytaramiz
```

### 5.2 Oxiriga element qo'shish:
```python
def add_to_end(head, val):
    new_node = ListNode(val)
    
    if head is None:
        return new_node
    
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head
```

### 5.3 Element o'chirish:
```python
def delete_value(head, val):
    if head is None:
        return None
    
    if head.val == val:
        return head.next
    
    current = head
    while current.next is not None:
        if current.next.val == val:
            current.next = current.next.next
            break
        current = current.next
    return head
```

## 6. Muhim usullar

### 6.1 Two Pointer Technique (Ikki ko'rsatkich)

Bu juda muhim usul! Ikki ta pointer ishlatamiz:
- **Slow pointer** - bir qadam
- **Fast pointer** - ikki qadam

```python
def two_pointer_example(head):
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next        # 1 qadam
        fast = fast.next.next   # 2 qadam
    
    return slow  # O'rtadagi element
```

## 7. Masala: Middle of the Linked List

Endi asosiy masalamizni yechamiz!

### Masala tahlili:
- Linked List berilgan
- O'rtadagi elementni topish kerak
- Agar 2 ta o'rtadagi element bo'lsa, ikkinchisini qaytarish

### Yechim 1: Uzunlikni hisoblash
```python
def find_middle1(head):
    # 1-qadam: Uzunlikni topamiz
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    
    # 2-qadam: O'rtaga boramiz
    middle = length // 2
    current = head
    for _ in range(middle):
        current = current.next
    
    return current
```

### Yechim 2: Two Pointer (Eng yaxshi!)
```python
def find_middle2(head):
    slow = head
    fast = head
    
    # Fast 2 qadam, slow 1 qadam
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

## 8. Nima uchun Two Pointer yaxshi?

**Misollar:**

**5 ta element:** [1,2,3,4,5]
- Slow: 1 -> 2 -> 3 (to'xtaydi)
- Fast: 1 -> 3 -> 5 (to'xtaydi)
- Javob: 3 ✓

**6 ta element:** [1,2,3,4,5,6]
- Slow: 1 -> 2 -> 3 -> 4 (to'xtaydi)
- Fast: 1 -> 3 -> 5 -> null (to'xtaydi)
- Javob: 4 ✓

## 9. To'liq kod

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head):
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Test qilish
def create_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

# Misol 1: [1,2,3,4,5]
list1 = create_list([1, 2, 3, 4, 5])
print(middle_node(list1).val)  # 3

# Misol 2: [1,2,3,4,5,6]
list2 = create_list([1, 2, 3, 4, 5, 6])
print(middle_node(list2).val)  # 4
```

1. **Har doim null tekshiring!** - Linked List bosh bo'lishi mumkin
2. **Two Pointer usuli** - ko'p masalalarda ishlatiladi
3. **Edge cases** - 1 ta yoki 2 ta element bo'lsa nima bo'ladi?
4. **Qadamlab debugging** - har bir qadamni kuzatib boring

## 11. Keyingi bosqich

Endi siz Linked List ning asoslarini bildingiz! Keyingi masalalar:
- Reverse Linked List
- Detect Cycle
- Merge Two Sorted Lists
- Remove Duplicates

**Eslab qoling:** Linked List - bu zanjir, har bir halqa keyingi halqaga bog'langan!
