# =========================================================
# 1) FIXED-SIZE ARRAY (statik massiv)
# =========================================================
# Boshida joy hajmi qat'iy belgilanadi, keyin o'zgartirib bo'lmaydi.
# Python'da bunga eng yaqin misol - "array" moduli yoki oddiy list'ni
# belgilangan hajmda ushlab turish.

FIXED_SIZE = 5
fixed_arr = [None] * FIXED_SIZE  # boshida 5 ta bo'sh joy ajratildi

fixed_arr[0] = 10
fixed_arr[1] = 20
fixed_arr[2] = 30
print(fixed_arr)  # [10, 20, 30, None, None]

# Muammo: FIXED_SIZE dan ortiq element qo'sha olmaymiz.
# fixed_arr[5] = 40  # IndexError: list assignment index out of range


# =========================================================
# 2) DYNAMIC ARRAY (dinamik massiv) - Python'ning list'i shunday ishlaydi
# =========================================================
# Joy tugasa, Python ichkarida KATTAROQ yangi massiv yaratadi
# (odatda ~1.125-2 barobar), eski elementlarni ko'chiradi va
# eskisini o'chiradi. Shuning uchun list'ga cheksiz append qilsa bo'ladi.

dynamic_arr = []
for i in range(5):
    dynamic_arr.append(i * 10)
    print(dynamic_arr, "hajmi (len):", len(dynamic_arr))

# Natija:
# [0] hajmi: 1
# [0, 10] hajmi: 2
# [0, 10, 20] hajmi: 3
# [0, 10, 20, 30] hajmi: 4
# [0, 10, 20, 30, 40] hajmi: 5
#
# append() odatda O(1) - amortized, chunki qayta joylashtirish
# kamdan-kam sodir bo'ladi, lekin sodir bo'lganda O(n) turadi.


# =========================================================
# 3) SHIFTING (elementlarni surish) - insert va delete paytida
# =========================================================

def insert_at(arr, index, value):
    # O(n) - index'dan keyingi barcha elementlarni 1 pog'ona
    # O'NGGA surish kerak, keyin bo'sh joyga value qo'yiladi
    arr.append(None)  # oxiriga joy ochamiz
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]  # har bir elementni o'ngga suramiz
    arr[index] = value
    return arr


def delete_at(arr, index):
    # O(n) - index'dan keyingi barcha elementlarni 1 pog'ona
    # CHAPGA surish kerak, bo'shagan oxirgi joyni olib tashlaymiz
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]  # har bir elementni chapga suramiz
    arr.pop()  # endi keraksiz bo'lgan oxirgi elementni o'chiramiz
    return arr


arr = [10, 20, 30, 40, 50]
print("Boshlang'ich:", arr)

insert_at(arr, 2, 99)
print("2-index'ga 99 qo'shilgach:", arr)
# [10, 20, 99, 30, 40, 50]  -> 30, 40, 50 o'ngga surildi

delete_at(arr, 1)
print("1-index o'chirilgach:   ", arr)
# [10, 99, 30, 40, 50]  -> 99, 30, 40, 50 chapga surildi


# =========================================================
# Big O (vaqt murakkabligi)
# =========================================================
# ------------------------------------------------------------
# Amal                    | Fixed-size array | Dynamic array (list)
# ------------------------------------------------------------
# index bo'yicha o'qish   | O(1)             | O(1)
# oxiriga qo'shish        | O(1) (agar joy bor bo'lsa) | O(1) amortized
# boshiga/o'rtaga qo'shish| O(n) - shift kerak | O(n) - shift kerak
# o'rtadan o'chirish      | O(n) - shift kerak | O(n) - shift kerak
# to'lib qolganda kengaytirish | mumkin emas (qayta yaratish kerak) | O(n), lekin kam-kam sodir bo'ladi
# ------------------------------------------------------------
#
# Xulosa:
# - Fixed-size array: hajmi oldindan ma'lum bo'lsa tez va xotira tejamkor,
#   lekin hajmini o'zgartirib bo'lmaydi.
# - Dynamic array (Python list): kerak bo'lganda avtomatik kengayadi,
#   shu uchun kundalik dasturlashda qulayroq.
# - Ikkalasida ham o'rtaga/oldga qo'shish yoki o'chirish O(n),
#   chunki elementlarni SURISH (shift) kerak - Linked List'dan farqli
#   o'laroq, bu yerda "bo'sh joy" yo'q, hammasi ketma-ket turishi shart.


# =========================================================
# Nega va qayerda kerak bo'ladi?
# =========================================================
# Array ishlatiladi, chunki:
# - index bo'yicha o'qish tezligi eng muhim bo'lganda (O(1))
# - element'lar soni ko'p o'zgarmasa yoki oxiriga qo'shish yetarli bo'lsa
# - CPU keshiga yaxshi mos keladi (elementlar xotirada ketma-ket
#   joylashgani uchun tez-tez ishlatiladigan ma'lumotlarni o'qish tezroq)
#
# Amaliy misollar:
# - Rasm piksellari, matritsa/jadval ma'lumotlari (index orqali tez kirish)
# - Fixed-size array: mikrokontroller/embedded tizimlar - xotira qat'iy
#   cheklangan bo'lganda (masalan, sensor buferi - har doim 10 ta oxirgi
#   o'lchov saqlanadi)
# - Dynamic array (Python list, Java ArrayList, C++ vector): kundalik
#   dasturlash - foydalanuvchilar ro'yxati, mahsulotlar ro'yxati, log'lar
# - Stack va queue'ning ichki implementatsiyasi ko'pincha array asosida
# - Sorting algoritmlari (quicksort, mergesort) array bilan ishlaydi,
#   chunki index orqali ikkita elementni solishtirish/almashtirish tez
#
# Qachon array YAXSHI TANLOV EMAS:
# - Ro'yxat o'rtasiga tez-tez qo'shish/o'chirish kerak bo'lsa
#   (bunday holda Linked List yoki boshqa struktura yaxshiroq)
# - Hajmi oldindan noma'lum va juda tez-tez o'zgarib turadigan holatda
#   fixed-size array mos emas
