Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
Max = None
Min = None
while True:
    inp = input("Enter a number:")
    if inp == "done"：
        break
    try:
        inp = float(inp)
    except:
        print("%s is not a number" % inp)
        continue
    if Max is None or Max < inp:
        Max = inp
    if Min is None or Min > inp:
        Min = inp
print("Maximun:",Max,"Minimum",Min)
input()
