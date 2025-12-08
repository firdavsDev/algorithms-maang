- Miqdorlarni o'lchash uchun hayotda turli hil o'lchov birliklaridan foydalanamiz.
Uzunlik uchun santimetr, suv uchun litr, og'irlik uchun tonna/kilogram/gram/miligram va h.k.z.larni misol qilishimiz mumkin.
Huddi shunday dasturlashdagi ko'p narsalarni ham o'lchash uchun o'lchov birliklari bor.

Algoritm va Ma'lumotlar Strukturasini o'lchash uchun esa biz odatda 3 xil o'lchov birligidan foydalanamiz:
    1) Big O notation - Vaqt va Xotira murakkabligini eng maksimum qiymatini o'lchash uchun ishlatiladi. Uning vazifasi bizning Algoritm yoki Ma'lumotlar struktuamiz eng yomon holat(worst-case)da qanday ishlashini tasvirlaydi.
    2) Theta notation - Vaqt va Xotira murakkabligini o'rtacha holatini o'lchash uchun ishlatiladi.
    3) Omega notation - Vaqt va Xotira murakkabligini eng minimum qiymatini o'lchash uchun ishlatiladi. Uning vazifasi bizning Algoritm yoki Ma'lumotlar struktuamiz eng yaxshi holat(best-case)da qanday ishlashini tasvirlash.

Dasturlarni odatda worst-case holati o'lchanadi. Chunki bu orqali siz o'z dasturingiz eng yomon holatda qanday ko'rsatgichda ishlashini bilib olasiz. Bu huddi marafon yuguruvchisi kasal va yugurishga loyiq emas holatida qanday natija ko'rsatishini o'lchashdek gap.
Demak biz Big O notation nima uchun xizmat qilishini qisman tushunib oldik endi keling to'liqroq misollar bilan ko'rib chiqsak.


Q) BigO nima?
A) BigO bu algoritimingiz tezligi (vaqt) va qancha xotira kerak ekanligini aniqlab beradi.
- Yani ma'lumotlarimiz ko'paygani sari bu qanchalik sekinlashish darajasini aytib beradi.
- Big O input xajmi qanchalik oshgani sari funksiya o'zini qanday tutishi, tezligi va xajmi qanday o'sishini tasvirlash uchun ishlatilar ekan.
- Misol uchun O(n), n harfi bu yerda input hajmini bildiradi va O() esa algoritmni o'lchashdagi belgi vazifasini o'taydi.
- Keling endi o'lchovlarni qanday qilishni o'rganib chiqsak.

1) Constant:
- Constant so'zi bu konstanta ya'ni o'zgarmas, doimiy degan ma'noni bildiradi.
- Agar algoritm yoki ma'lumot strukturasi harqanday inputga nisbatan bir xil vaqt va xotira sarflasa, demak u constant bo'ladi.
- Uni biz Big O bilan O(1) deb tasvirlaymiz.

2) Linear
- Linear so'zi bu chiziqli degan ma'noni bildiradi.
- Chiziq uzunligi o'sgani sari qiymati (sm) ham o'sib boradi.
- Agar algoritm yoki ma'lumot strukturasi har-xil inputga nisbatan har-xil vaqt va xotira sarflasa, demak u linear bo'ladi.
- Uni biz Big O bilan O(n) deb tasvirlaymiz.

Linear Time: Oldingizda 5ta idish mavjud va siz har bir idishni yuvish uchun 1-sekund vaqt sarflaysiz. Idishlar soni oshib borar ekan ketkaziladigan vaqt ham oshib boraveradi. Shuning uchun ham eng yomon ko'rsatgichda siz n-ta idish uchun n-sekund vaqt sarflaysiz.

Linear Space: Mexmonxonada 1-kishilik xonalarni olaylik. Har bir inson uchun mexmonxona 1ta xona bersa, n-ta kishi uchun mexmonxona n-ta xona tayyorlashi kerak degani.

Logarithmic:
- Logarifmni biz Big O da O(log n) deb tasvirlaymiz.
- Bu yerda log deyilganda asos berilmagan bilaman ammo biz asosida 2 soni turibdi deb tasavvur qilishimiz kerak. Ya'ni log2 n degani bilan teng.


log2(1024) = 10 (2ning nechani darajasi  1024ga teng degan mano bu yerda)
log2(10) + log2(5) = log2(10*5) (bir xil asosli log'lar qushilganda unig darajalari ko'paytiriladi, asoslar ayrilganda esa darajalari bo'linadi )
O(n) - bu linear(chiziqli) o'sish.
Qancha xotira ko'p ishlatilsa, amalar shuncha tez bajariladi.



Useful links:
- https://www.dsalgo.uz/bigo
- 42.uz
- https://www.youtube.com/watch?v=WqrbIUggEXQ&t=2697s
