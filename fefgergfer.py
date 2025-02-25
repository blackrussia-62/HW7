def calculate(expression):
    try:
        if '+' in expression:
            num1, num2 = map(float, expression.split('+'))
            return num1 + num2
        if '-' in expression:
            num1, num2 = map(float, expression.split('-'))
            return num1 - num2
        if '*' in expression:
            num1, num2 = map(float, expression.split('*'))
            return num1 * num2
        if '/' in expression:
            num1, num2 = map(float, expression.split('/'))
            if num2 == 0:
                raise ZeroDivisionError("gaga на ноль не делят")
            return num1 / num2
        else:
            raise ValueError("правильна пеши")
    except ValueError as e:
        return f"еррор: {str(e)}"
    except Exception as e:
        return f"ероор: {str(e)}"

if __name__ == "__main__":
    while True:
        at = input("нопеши выражение или выход шобы уйти")
        if at.lower() == 'выход':
            break
        result = calculate(at)
        print(f"Результат: {result}")
