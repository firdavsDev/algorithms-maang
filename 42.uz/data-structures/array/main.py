"""
# Array(massiv) - bir xil o'lchami malumotlarni saqlash uchun.

* Array yaratish uchun qoidalari amal qilish zarur:
- Davomiy bo'lish kerak(continuously)
- Chegarasi bor
- Har bir element bir xil o'lchamda bo'lish kerak

Nega array'lar 0dan boshlanadi?
- address + i(index) * element_bayti


BigO har doim eng yomon varyantini tanlashga undaydi
arr = [1,2,3,4]
Misol:
2 elementini uchirganimizda qolgan elementlar 3ni urniti tuldirish uchun siljiydi(shift) O(n) degani
agar 4 sungi element uchirsak constant ish bajariladi yani O(1)
bu varyantda 2 hil javob bor O(n) va O(1) biz O(n) tanlaymiz
"""
