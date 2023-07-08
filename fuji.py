def main(lines):
    for i,v in enumerate(lines):
        s = v

    if len(s) != 4:
        print('Reject')
        return 0
    
    flg = False
    nums = set()
    for i in s:
        if not i.isdigit(): # 1つでも数字じゃないものがあればflgをたてる
            flg = True
        else:
            nums.add(i)    # 数字だったらsetに追加
            
    if flg or len(nums) <= 1: # 文字が含まれているか数字の種類が1以下なら Reject
        print('Reject')
        return 0

    else:
        print('Accept')




if __name__ == '__main__':
    lines = ['1230']
    main(lines)