coke = 50
paid = 0
coins = [25, 10, 5]

while coke > 0:
    print(f"Amount Due: {coke}")
    inserted = int(input("Inter Coin: "))
    if inserted in coins:
        coke = coke - inserted
        paid = paid + inserted

if paid >= coke:
    print(f"Change Owed: {paid - 50}")

