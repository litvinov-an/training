n = int(input())
for i in range(n):
    nalichie_slova_cot = False
    phrase = input()
    if "кот" or ("Кот" in phrase):
        nalichie_slova_cot = True
if nalichie_slova_cot:
    print("МЯУ")
else:
    print("НЕТ")
