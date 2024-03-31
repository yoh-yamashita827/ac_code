## 20以下の読み
under_20 = ["zero","one","two","three","four","five","six","seven","eight","nine","ten",
           "eleven","twelve","thirteen", "fourteen", "fifteen", "sixteen","seventeen", "eighteen", "nineteen"]
## 10の倍数の読み
nums_10 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

## 1000以上の接尾辞　
suffix = ["","thousand", "million", "billion"]

def number_to_english(x):
    ## 少数の場合は，整数部分と少数部分に切り分けて処理
    if "." in x:
        integer,decimal = x.split(".")
        int_part = number_to_english(integer)
        decimal_part = " ".join([number_to_english(digit) for digit in decimal])

        ## 最後にpointで繋げて返す
        return int_part + " point " + decimal_part



    def make_english(x):
        ## 20以下の場合は読みをそのまま返す
        if x < 20:
            return under_20[x]

        ## 100以下の場合は10の位と1の位
        elif x < 100:
            return nums_10[x//10] + (" " + under_20[x % 10] if x % 10 != 0 else "")
        
        ## 1000以下の場合は100の位の数＋hundred+それ以下の位
        elif x < 1000:
            return under_20[x//100] + " hundred " + (" " + make_english(x % 100) if x % 100 != 0 else "")
        
        ##　それ以上の場合は1000の何乗かによって場合分けを行い，対応する接尾辞を付け加える
        else:
            for i in range(len(suffix)):
                if x < 1000 ** (i + 1):
                    return make_english(x // 1000 ** i) + " " + suffix[i] + (" " + make_english(x % 1000 ** i) if x % 1000 ** i != 0 else "")
                
            
    
    if float(x) == 0:
        return under_20[0]
    else:
        return make_english(int(float(x)))
    
def error_handler(x):

    def valid_number(num):
        if not num.isdigit() or (len(num) != 1  and num[0] == '0'):
            print(-1)
            exit()

    if "." in x:
        integer,decimal = x.split(".")
        valid_number(integer)

    else:
        valid_number(x)


    

## 入力を受け取る
x = input()
error_handler(x)
## 出力フォーマットに合わせて整形する（頭文字を大文字に）
ans = number_to_english(x)
ans = ans[0].upper() + ans[1:]
print(ans)