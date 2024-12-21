def prompt(prompt):
    try:
        val = int(input(prompt))
        return val
    except ValueError:
        print("value error is raised")
    finally:
        print("finally has printed")

n = prompt("integer val")
