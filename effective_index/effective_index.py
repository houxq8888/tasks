import math

def get_prime_factors(n):
    """
    获取一个数的所有质因数（不包括1）
    :param n: 需要分解的数
    :return: 质因数列表
    """
    factors = set()
    # 处理2的情况
    while n % 2 == 0:
        factors.add(2)
        n = n // 2
    # 处理奇数情况
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n = n // i
        i += 2
    # 剩下的数如果大于2则是质数
    if n > 2:
        factors.add(n)
    return list(factors)

def is_effective_number(num):
    """
    判断一个自然数是否为有效指数
    步骤：
    1. 对该数的每个数字进行平方和，然后求该和的平方根
    2. 对其结果求一切可能的质因数（不包括1），并求这些质因数的乘积的平方
    3. 如果这个结果是原数的立方根的整数部分的平方，返回True，否则返回False
    :param num: 输入的自然数
    :return: 是否为有效指数
    """
    if num < 1:
        return False
    
    # 步骤1：计算每个数字的平方和，然后求平方根
    digits = [int(d) for d in str(num)]
    square_sum = sum(d**2 for d in digits)
    sqrt_square_sum = math.sqrt(square_sum)
    
    # 步骤2：求平方根结果的质因数乘积的平方
    # 质因数分解通常针对整数，所以将平方根四舍五入为最接近的整数
    sqrt_int = round(sqrt_square_sum)
    
    # 对取整后的结果进行质因数分解
    prime_factors = get_prime_factors(sqrt_int)
    if not prime_factors:
        # 如果没有质因数（sqrt_int为1）
        product_prime = 1
    else:
        product_prime = 1
        for factor in prime_factors:
            product_prime *= factor
    
    result_step2 = product_prime ** 2
    
    # 步骤3：判断结果是否等于原数立方根整数部分的平方
    # 计算原数的立方根整数部分
    cube_root_int = int(math.pow(num, 1/3))
    # 验证是否正确的整数部分（防止精度问题）
    if (cube_root_int + 1) ** 3 <= num:
        cube_root_int += 1
    
    target_value = cube_root_int ** 2
    
    return math.isclose(result_step2, target_value)

def main():
    """
    主函数，用于测试
    """
    # 测试样例
    test_cases = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    for num in test_cases:
        result = is_effective_number(num)
        print(f"Number {num}: {'Effective' if result else 'Not Effective'}")

if __name__ == "__main__":
    main()