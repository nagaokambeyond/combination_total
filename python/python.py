""" 合計がXになる整数の組み合わせを出力する """
source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_integral_value_combination(list, target):
    """
    https://qiita.com/Cesaroshun/items/6302542e4e32602d775d

    Args:
        list:リスト
        target:この値になる
    Returns:
        targetになる組み合わせのリスト
    """
    def a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(list)):
            a((u + 1), l + [list[u]], r, t)
        return r
    return a(0, [], [], target)

def get_integral_value_combination_refacter(list_source: list, target_value: int) -> list:
    """
    https://qiita.com/Cesaroshun/items/6302542e4e32602d775d

    Args:
        list_source:リスト
        target_value:この値になる
    Returns:
        target_valueになる組み合わせのリスト
    """
    list_length = len(list_source)
    result = []
    def recursion(start_index: int, combination_list: list) -> None:
        summary = sum(combination_list)
        if target_value == summary:
            result.append(combination_list)
        elif target_value < summary:
            return  # 超えているためなにも返さない
        else:
            for index in range(start_index, list_length):
                next_start_index = index + 1
                next_combination_list = combination_list + [list_source[index]]    # 指定要素の内容を追加したリスト
                recursion(next_start_index, next_combination_list)
        return
    recursion(0, [])
    return result


print(get_integral_value_combination_refacter(source, 10))
#print(get_integral_value_combination(source, 10))
