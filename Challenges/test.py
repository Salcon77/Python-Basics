def process():
    while True:
        # Stores input into variable x
        x = input()

        # This is the checksum. Last two
        checksum = x[-2:]
        # This converts the checksum hex into a int
        checksumInt = int(checksum, 16)

        # This is the account number without the checksum
        accountNumberHex = x[:-2]

        # This converts the hex account number to int
        accountNumberInt = int(accountNumberHex, 16)

        # puts each integer in the account number into a list
        accountNumberList = map(int, str(accountNumberInt))

        # sums the list
        accountSum = sum(accountNumberList)

        if accountSum == checksumInt:

            print("VALID")
        else:

            print("INVALID")
process()