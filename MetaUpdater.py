import sys, os

if __name__ == '__main__':
    vLen = len(sys.argv)
    if vLen != 1 and vLen != 2 and vLen != 3:
        print("Wrong number of parameters\nFor usage, run MetaUpdater.py --help")
    else:
        if vLen == 2:
            if sys.argv[1] == "--help":
                print("Help age")
            else:
                if not os.path.exists(sys.argv[1]):
                    print("Error, no such path as:\n" + str(sys.argv[1]))
                else:
                    print("Parsing,,,")