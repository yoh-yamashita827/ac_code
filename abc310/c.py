N = int(input())
S = []
s_dict = {}
for _ in range(N):
    tmp = (input())
    # S.append(tmp)
    if tmp <=  tmp[::-1]:
        S.append(tmp)
    else:
        S.append(tmp[::-1])

print(len(set(S)))

# for i in S:
#     if i not in s_dict.keys():
#         s_dict[i] = 1
#     else:
#         s_dict[i] += 1

# ans = 0
# import copy
# ss_dict = copy.deepcopy(s_dict)

# for key in s_dict.keys():
#     if len(ss_dict.keys()) == 0:
#         continue
#     ans += ss_dict[key]
#     ss_dict.pop(key)
#     if key[::-1] in ss_dict.keys():
#         ans += ss_dict[key[::-1]]-1
#         ss_dict.pop(key[::-1])
#     else:
#         ans -= 1


# ans = 0
# visit = set()
# for i in S:
#     if (i in visit):
#         ans += 1
#     visit.add(i)
#     visit.add(i[::-1])

# print(ans)