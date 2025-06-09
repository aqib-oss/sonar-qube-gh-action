from sonar_qube_gh_action.calculator import Calculator

if __name__ == "__main__":
    result: int = Calculator().sum(5, 3)
    print(f"The sum of 5 and 3 is: {result}")
