numbers = {
    1 : "", 2 : "ABC", 3 : "DEF",
    4 : "GHI", 5 : "JKL", 6 : "MNO",
    7 : "PQRS", 8 : "TUV", 9 : "WXYZ",
    0 : ""
}
string = input().upper()
time = 0
for i in string:
    for key, value in numbers.items():
        if i in value:
            time += key + 1
print(time)