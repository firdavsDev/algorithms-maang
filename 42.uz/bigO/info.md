# Big O notation

Miqdorlarni o'lchash uchun hayotda turli xil o'lchov birliklaridan foydalanamiz.
Uzunlik uchun santimetr, suv uchun litr, og'irlik uchun tonna/kilogram/gram/miligram va h.k.z.larni misol qilishimiz mumkin.
Xuddi shunday, dasturlashdagi ko'p narsalarni ham o'lchash uchun o'lchov birliklari bor.

Algoritm va ma'lumotlar strukturasini o'lchash uchun odatda 3 xil o'lchov birligidan foydalanamiz:

1. **Big O notation** — vaqt va xotira murakkabligining eng yuqori qiymatini, ya'ni algoritm yoki ma'lumotlar strukturasining eng yomon holatda (*worst case*) qanday ishlashini tasvirlaydi.
2. **Theta notation** — vaqt va xotira murakkabligining o'rtacha holatini tasvirlaydi.
3. **Omega notation** — vaqt va xotira murakkabligining eng past qiymatini, ya'ni algoritm yoki ma'lumotlar strukturasining eng yaxshi holatda (*best case*) qanday ishlashini tasvirlaydi.

Odatda dasturlarning *worst case* holati o'lchanadi. Chunki bu orqali dasturingiz eng yomon holatda qanday ko'rsatkichda ishlashini bilib olasiz. Bu xuddi marafon yuguruvchisining kasal va yugurishga yaroqsiz holatidagi natijasini o'lchashga o'xshaydi.

## Big O nima?

Big O algoritmingizning tezligi (vaqt murakkabligi) va qancha xotira kerakligini aniqlab beradi.

- Ma'lumotlar ko'paygani sari algoritm qanchalik sekinlashishini ko'rsatadi.
- Funksiya input hajmi oshganda o'zini qanday tutishini, tezligi va xotira sarfi qanday o'sishini tasvirlaydi.
- Masalan, `O(n)` ifodasida `n` input hajmini, `O()` esa algoritmni o'lchash belgisini bildiradi.

## 1. Constant — `O(1)`

*Constant* — konstanta, ya'ni o'zgarmas va doimiy degan ma'noni bildiradi.

Agar algoritm yoki ma'lumotlar strukturasi har qanday input uchun bir xil vaqt va xotira sarflasa, u constant hisoblanadi.

## 2. Linear — `O(n)`

*Linear* — chiziqli degan ma'noni bildiradi. Agar input hajmi oshgani sari algoritmning vaqt yoki xotira sarfi ham mutanosib ravishda oshsa, u linear hisoblanadi.

### Linear time

Oldingizda 5 ta idish mavjud va har bir idishni yuvish uchun 1 soniya sarflaysiz. Idishlar soni oshgani sari ketkaziladigan vaqt ham oshadi. Eng yomon holatda `n` ta idish uchun `n` soniya vaqt sarflaysiz.

### Linear space

Mehmonxonada har bir inson uchun 1 ta xona ajratiladi. Demak, `n` ta kishi uchun mehmonxona `n` ta xona tayyorlashi kerak.

## 3. Logarithmic — `O(log n)`

Logarifm Big O da `O(log n)` ko'rinishida tasvirlanadi. Asos ko'rsatilmagan bo'lsa, odatda 2 soni nazarda tutiladi: `log₂ n`.

```text
log₂(1024) = 10
log₂(10) + log₂(5) = log₂(10 × 5)
```

`O(n)` — chiziqli o'sish. Xotiradan ko'proq foydalanish har doim amallarni tezlashtirmaydi.

## Foydali havolalar

- https://www.dsalgo.uz/bigo
- 42.uz
- https://www.youtube.com/watch?v=WqrbIUggEXQ&t=2697s
