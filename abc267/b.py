#N = int(input())
#N,M = map(int,input().split())
S = input()
#A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   #S.append(input())
if S[0] != '0':
    print('No')
    exit()


ren = {(6):0, (3):1, (1,7):2, (0,4):3, (2,8):4, (5):5, (9):6}


for i in ren.keys():
   for j in ren.keys():
      if i==j:continue

      tmp_i = 0
      tmp_j = 0
      if not str(i).isdigit():
         for ii in (i):
            tmp_i += int(S[ii])
      else:
         tmp_i += int(S[i])
      if not str(j).isdigit():
         for jj in j:
            tmp_j += int(S[jj])
      else:
         tmp_j += int(S[j])
      if (tmp_i == 0) or (tmp_j == 0):
         print('No')
         exit()
      if ren[i] > ren[j]:
         ren[i],ren[j] = ren[j],ren[i]
      mid = list(range(ren[i],ren[j]))
      for k in ren.keys():
         if ren[k] in mid:
            tmp = 0
            if not str(k).isdigit():
               for kk in k:
                  tmp += int(S[kk])
            else:
               tmp += int(S[k])
            if tmp == 0:
               print('Yes')
               exit()

print('No')


