def main():
    left = open('OCR_And_Editing/BrainfuckLeft.txt', 'r', encoding='utf-16')
    right = open('OCR_And_Editing/BrainfuckRight.txt', 'r', encoding='utf-16')

    leftlines = left.readlines()
    rightlines = right.readlines()

    for i, line in enumerate(leftlines):
        if i == len(leftlines) - 1:
            print(line + rightlines[i])
        else:
            print(line[:-1] + rightlines[i][:-1])

    left.close()
    right.close()
        
main()
