def main():
    cube = open("cube.fbx", "rb")
    text = open("text.txt")

    for line in cube.readlines():
        smallines = line.split()
        print("_________________________________________________")
        print(smallines)
    # print(text.readlines())


if __name__ == "__main__":
    main()