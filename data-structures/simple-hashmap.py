# Hash Map (Hash Table) - "kalit -> qiymat" (key -> value) saqlaydigan
# struktura. Ichkarida ARRAY ishlatiladi, lekin key to'g'ridan-to'g'ri
# index emas - avval HASH FUNKSIYA orqali index'ga aylantiriladi.
#
# Bu bizga sonli index o'rniga ("array[0]") ixtiyoriy kalitlar bilan
# ishlash imkonini beradi ("hashmap['ali']").


class HashMap:
    def __init__(self, size=8):
        self.size = size
        # har bir "bucket" - bir nechta (key, value) juftlikni saqlaydigan ro'yxat
        # (chaining orqali kolliziyani hal qilamiz)
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Kalitni array index'ga aylantiramiz.
        # Python'ning built-in hash() funksiyasidan foydalanamiz,
        # keyin bucket'lar sonidan qoldiq (%) olamiz.
        return hash(key) % self.size

    def put(self, key, value):
        # O(1) o'rtacha holatda (amortized)
        index = self._hash(key)
        bucket = self.buckets[index]

        # agar key allaqachon mavjud bo'lsa - yangilaymiz
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # aks holda yangi juftlik qo'shamiz
        bucket.append((key, value))

    def get(self, key):
        # O(1) o'rtacha holatda
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"{key} topilmadi")

    def delete(self, key):
        # O(1) o'rtacha holatda
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

        raise KeyError(f"{key} topilmadi")

    def contains(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        return any(k == key for k, v in bucket)

    def print_map(self):
        for i, bucket in enumerate(self.buckets):
            print(f"[{i}]: {bucket}")


# Foydalanish
hm = HashMap(size=5)
hm.put("ism", "Ali")
hm.put("yosh", 25)
hm.put("shahar", "Toshkent")

hm.print_map()
# Har bir key o'zining hash qiymati asosida bucket'ga tushadi

print(hm.get("ism"))     # Ali
print(hm.contains("yosh"))  # True

hm.put("ism", "Vali")    # mavjud key yangilanadi
print(hm.get("ism"))     # Vali

hm.delete("shahar")
print(hm.contains("shahar"))  # False


# =========================================================
# KOLLIZIYA (collision) nima?
# =========================================================
# Ikkita har xil key bir xil bucket index'ga tushib qolishi mumkin
# (masalan hash("a") % 5 == hash("f") % 5). Bu KOLLIZIYA deyiladi.
#
# Yechim - CHAINING: har bir bucket index o'zi bitta qiymat emas,
# balki RO'YXAT (list) saqlaydi. Kolliziya bo'lganda ikkala juftlik
# ham o'sha bucket ichidagi ro'yxatga qo'shiladi (yuqoridagi kodda
# aynan shu usul ishlatilgan).
#
# Muqobil yechim - OPEN ADDRESSING: kolliziya bo'lsa, keyingi bo'sh
# joyni qidirib topiladi (bu yerda ko'rsatilmagan, murakkabroq usul).


# =========================================================
# Big O (vaqt murakkabligi)
# =========================================================
# ------------------------------------------------------------
# Amal      | O'rtacha holat | Eng yomon holat
# ------------------------------------------------------------
# put       | O(1)           | O(n) - hammasi bitta bucket'ga tushsa
# get       | O(1)           | O(n)
# delete    | O(1)           | O(n)
# contains  | O(1)           | O(n)
# ------------------------------------------------------------
# Eng yomon holat kamdan-kam sodir bo'ladi (yaxshi hash funksiya va
# yetarlicha bucket soni bo'lsa), shuning uchun amaliyotda hashmap
# deyarli har doim O(1) sifatida hisoblanadi.


# =========================================================
# Nega va qayerda kerak bo'ladi?
# =========================================================
# Hash Map ishlatiladi, chunki:
# - kalit orqali qiymatni DARHOL topish kerak bo'lganda (array kabi
#   index emas, balki ixtiyoriy kalit - masalan, ism, so'z, ID)
# - qidirish, qo'shish, o'chirish tezligi O(1) bo'lishi kerak bo'lganda
#   (array/linked list'da bu O(n) bo'lardi)
#
# Amaliy misollar:
# - Python dict, JavaScript object/Map, Java HashMap - dasturlash
#   tillarining o'zida keng ishlatiladi
# - Foydalanuvchi ma'lumotlarini ID orqali tez topish (user_id -> user)
# - So'zlar chastotasini sanash (so'z -> nechta marta uchragani)
# - Caching / memoization - hisoblangan natijalarni saqlab, qayta
#   hisoblamaslik uchun (masalan, Fibonacci memoization)
# - Ma'lumotlar bazasidagi indexlash tushunchasining asosi
# - Ikki massivda umumiy elementlarni tez topish (set/hashmap orqali)
# - Login tizimlarida username -> parol hash'ini tez tekshirish
#
# Qachon Hash Map YAXSHI TANLOV EMAS:
# - Elementlarni TARTIBLANGAN holda saqlash/aylanib chiqish kerak
#   bo'lsa (hashmap tartibni kafolatlamaydi - buning uchun
#   TreeMap/sorted structure kerak)
# - Juda kichik ma'lumotlar to'plami bo'lsa, oddiy array/list
#   yetarli va tezroq bo'lishi mumkin (hash hisoblash xarajati bor)


# =========================================================
# Python'ning o'zidagi dict - bu tayyor Hash Map!
# =========================================================
# Yuqorida biz HashMap'ni QO'LDA yasadik, tushunish uchun.
# Lekin amaliyotda hech qachon o'zingiz yozmaysiz - Python'da
# buning uchun built-in "dict" bor, u xuddi shu prinsipda ishlaydi
# (hash funksiya + bucket + kolliziya), faqat C tilida yozilgan
# va juda optimallashtirilgan.

py_dict = {}
py_dict["ism"] = "Ali"
py_dict["yosh"] = 25
py_dict["shahar"] = "Toshkent"

print(py_dict)                # {'ism': 'Ali', 'yosh': 25, 'shahar': 'Toshkent'}
print(py_dict["ism"])         # O(1) - Ali
print("yosh" in py_dict)      # O(1) - True
py_dict["ism"] = "Vali"       # mavjud key yangilanadi
del py_dict["shahar"]         # O(1) - o'chirish
print(py_dict.get("yoq", "topilmadi"))  # xato bermaydi, default qaytaradi

# Muhim farq bizning qo'lda yozganimizdan:
# - Python 3.7+ da dict TARTIBNI SAQLAYDI (qo'shilgan tartibda) -
#   garchi ichkarida hash orqali ishlasa ham, alohida mexanizm bilan
#   qo'shilish tartibi ham eslab qolinadi (bizning oddiy HashMap'imiz
#   buni qilmaydi)
# - dict.get(key, default) - key topilmasa xato bermay, default
#   qiymat qaytaradi (bizning get() esa KeyError beradi)
# - juda tez, chunki C tilida implementatsiya qilingan va
#   resizing/hash funksiyasi ancha optimallashtirilgan
#
# Xulosa: real loyihalarda har doim built-in dict ishlating -
# o'z HashMap'ingizni yozish faqat "ichkarida qanday ishlaydi"ni
# tushunish uchun foydali mashq.
