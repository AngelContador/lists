def main():
    word = "python"
    print(word[2])
    print(word[-1])
    print(len(word))
    print(word[-6])
    print(word[0:2])
    print(word[2:])
    print(word[2:6])
    print(word[2:-1])
    print(word[-2:])
    print(word[:99])  #nofuncionarà
    print(word[99:0]) #nofuncionarà
    print(word[::-1])


if __name__ == '__main__':
    main()

    #hola