import math

# 调试函数，显示详细计算过程
def debug_effective_number(num):
    print(f"\nDebug for number: {num}")
    
    if num < 1:
        print("Error: num < 1")
        return False
    
    # 步骤1：计算每个数字的平方和，然后求平方根
    digits = [int(d) for d in str(num)]
    print(f"Digits: {digits}")
    square_sum = sum(d**2 for d in digits)
    print(f"Square sum: {square_sum}")
    sqrt_square_sum = math.sqrt(square_sum)
    print(f"Square root of sum: {sqrt_square_sum}")
    
    # 步骤2：求平方根结果的质因数乘积的平方
    sqrt_int = round(sqrt_square_sum)
    print(f"Round to int: {sqrt_int}")
    
    if not math.isclose(sqrt_square_sum, sqrt_int):
        print("Error: sqrt_square_sum is not integer")
        return False
    
    # 质因数分解函数
    def get_prime_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n = n // 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n = n // i
            i += 2
        if n > 2:
            factors.add(n)
        return list(factors)
    
    prime_factors = get_prime_factors(sqrt_int)
    print(f"Prime factors: {prime_factors}")
    
    if not prime_factors:
        product_prime = 1
    else:
        product_prime = 1
        for factor in prime_factors:
            product_prime *= factor
    
    result_step2 = product_prime ** 2
    print(f"Product of primes: {product_prime}")
    print(f"Result after step 2: {result_step2}")
    
    # 步骤3：判断结果是否等于原数立方根整数部分的平方
    cube_root_int = int(math.pow(num, 1/3))
    print(f"Cube root (float): {math.pow(num, 1/3)}")
    print(f"Cube root int (initial): {cube_root_int}")
    
    if (cube_root_int + 1) ** 3 <= num:
        cube_root_int += 1
    
    target_value = cube_root_int ** 2
    print(f"Cube root int (final): {cube_root_int}")
    print(f"Target value: {target_value}")
    
    is_effective = math.isclose(result_step2, target_value)
    print(f"Is effective: {is_effective}")
    
    return is_effective

# 测试样例
test_cases = [1, 8, 27, 64]
for num in test_cases:
    debug_effective_number(num)