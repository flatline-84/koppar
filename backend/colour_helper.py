import sys 

if __name__ == "__main__":
    colour = sys.argv[1]
    print(colour)
    colour = colour.strip('rgba').strip('(').strip(')').strip().split(',')
    new_colour = ""
    print(colour)
    for c in colour:
        new_colour += str(int(c)/256.0) + ','
    print(new_colour)