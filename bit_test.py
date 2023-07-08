import numpy as np
num = 10

for _ in range (10):
    max_values = [np.random.randint(0,200) for _ in range(num)]
    score = 0
    rival_score = 0
    for i in max_values:
        # print('最大値は{}です'.format(i))
        # bid = int(input('入札額を入力してください\n'))
        bid = int(i/2)
        rival = np.random.randint(0,200)


        if bid > rival:
            score += i-bid

        
    print('利益：{}\n'.format(score))



