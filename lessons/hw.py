def main() -> None:
    x: str = "x"
    y: str = "y"
    z: str = x
    y = x
    x = "y"

    if not (x != y and x != "y"):
        print(f"x: {x}")
    else:
        print("'if' condition not met.")


main()
