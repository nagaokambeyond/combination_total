source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
https://qiita.com/Cesaroshun/items/6302542e4e32602d775d

Args:
    list:リスト
    target:この値になる
Returns:
    targetになる組み合わせのリスト
"""
def get_integral_value_combination(list, target):
    def a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(list)):
            a((u + 1), l + [list[u]], r, t)
        return r
    return a(0, [], [], target)

def get_integral_value_combination_refacter(list, target_value):
    list_length = len(list)
    def recursion(start_index, combination_list, result):
        summary = sum(combination_list)
        if target_value == summary: 
            result.append(combination_list)
        elif target_value < summary: 
            return  # 超えているためなにも返さない
        else:
            for index in range(start_index, list_length):
                recursion((index + 1), combination_list + [list[index]], result)
        return result
    return recursion(0, [], [])


#print(get_integral_value_combination_refacter(source, 10))
print(get_integral_value_combination(source, 10))