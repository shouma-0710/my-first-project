num1 = float(input("1つ目の数字を入力してください："))
op = input("演算子を入力してください。(+,-,*,/)：")
num2 = float(input("2つ目の数字を入力してください："))

if(op == "+"):
    result = num1 + num2
elif(op == "-"):
    result = num1 - num2
elif(op == "*"):
    result = num1 * num2
elif(op == "/"):
    if num2 == 0:
        print("エラー：0で割ることはできません。")
    else:
        result = num1 / num2
else:
    print("不明な演算子です。")

print("答え：",result)