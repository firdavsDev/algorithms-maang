# Linked List - 0 dan To'liq O'rganish

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

```javascript
class ListNode {
    constructor(val) {
        this.val = val;        // Bu yerda ma'lumot saqlanadi
        this.next = null;      // Bu yerda keyingi node ga yo'nalish
    }
}
```

## 3. Linked List qanday yaratiladi?

```javascript
// Birinchi node yaratamiz
let node1 = new ListNode(1);
let node2 = new ListNode(2);
let node3 = new ListNode(3);

// Ularni bog'laymiz
node1.next = node2;
node2.next = node3;
node3.next = null;  // Oxirgi node

// Natija: 1 -> 2 -> 3 -> null
```

## 4. Linked List ni ko'rish (Traversal)

```javascript
function printList(head) {
    let current = head;
    while (current !== null) {
        console.log(current.val);
        current = current.next;
    }
}
```

## 5. Asosiy operatsiyalar

### 5.1 Boshiga element qo'shish:
```javascript
function addToStart(head, val) {
    let newNode = new ListNode(val);
    newNode.next = head;
    return newNode;  // Yangi head qaytaramiz
}
```

### 5.2 Oxiriga element qo'shish:
```javascript
function addToEnd(head, val) {
    let newNode = new ListNode(val);
    
    if (head === null) {
        return newNode;
    }
    
    let current = head;
    while (current.next !== null) {
        current = current.next;
    }
    current.next = newNode;
    return head;
}
```

### 5.3 Element o'chirish:
```javascript
function deleteValue(head, val) {
    if (head === null) return null;
    
    if (head.val === val) {
        return head.next;
    }
    
    let current = head;
    while (current.next !== null) {
        if (current.next.val === val) {
            current.next = current.next.next;
            break;
        }
        current = current.next;
    }
    return head;
}
```

## 6. Muhim usullar

### 6.1 Two Pointer Technique (Ikki ko'rsatkich)

Bu juda muhim usul! Ikki ta pointer ishlatamiz:
- **Slow pointer** - bir qadam
- **Fast pointer** - ikki qadam

```javascript
function twoPointerExample(head) {
    let slow = head;
    let fast = head;
    
    while (fast !== null && fast.next !== null) {
        slow = slow.next;        // 1 qadam
        fast = fast.next.next;   // 2 qadam
    }
    
    return slow;  // O'rtadagi element
}
```

## 7. Masala: Middle of the Linked List

Endi asosiy masalamizni yechamiz!

### Masala tahlili:
- Linked List berilgan
- O'rtadagi elementni topish kerak
- Agar 2 ta o'rtadagi element bo'lsa, ikkinchisini qaytarish

### Yechim 1: Uzunlikni hisoblash
```javascript
function findMiddle1(head) {
    // 1-qadam: Uzunlikni topamiz
    let length = 0;
    let current = head;
    while (current !== null) {
        length++;
        current = current.next;
    }
    
    // 2-qadam: O'rtaga boramiz
    let middle = Math.floor(length / 2);
    current = head;
    for (let i = 0; i < middle; i++) {
        current = current.next;
    }
    
    return current;
}
```

### Yechim 2: Two Pointer (Eng yaxshi!)
```javascript
function findMiddle2(head) {
    let slow = head;
    let fast = head;
    
    // Fast 2 qadam, slow 1 qadam
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    return slow;
}
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

```javascript
class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

function middleNode(head) {
    let slow = head;
    let fast = head;
    
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    return slow;
}

// Test qilish
function createList(arr) {
    if (arr.length === 0) return null;
    
    let head = new ListNode(arr[0]);
    let current = head;
    
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    
    return head;
}

// Misol 1: [1,2,3,4,5]
let list1 = createList([1,2,3,4,5]);
console.log(middleNode(list1).val); // 3

// Misol 2: [1,2,3,4,5,6]
let list2 = createList([1,2,3,4,5,6]);
console.log(middleNode(list2).val); // 4
```

## 10. Muhim maslahatlar

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
