for a in range(1, 11):
    for b in range(a, 11):  # On commence à 'a' pour éviter les doublons
        print(f"{a} x {b} = {a * b}")


        def multiply(x, y):
            """Multiply x by y using only addition"""
            result = 0
            for _ in range(y):
                result += x
            return result


        def power(a, b):
            """Compute a**b using only addition"""
            result = 1
            for _ in range(b):
                result = multiply(result, a)
            return result


        # Lire les entrées
        a = int(input("Enter a positive integer a: "))
        b = int(input("Enter a positive integer b: "))

        print(f"{a}^{b} = {power(a, b)}")


        def is_palindrome(n):
            """Check if an integer is a palindrome"""
            return str(n) == str(n)[::-1]


        # Lire un nombre
        num = int(input("Enter an integer: "))

        if is_palindrome(num):
            print(f"{num} is a palindrome!")
        else:
            print(f"{num} is NOT a palindrome.")