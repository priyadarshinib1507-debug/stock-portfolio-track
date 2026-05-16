# Fixed stock prices
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "NFLX": 400,
    "AMZN": 150
}

# Store user portfolio
holdings = {}

# Final total amount
grand_total = 0
count = int(input("Enter number of stocks: "))
for i in range(count):
    symbol = input("Enter stock name: ").upper()
    shares = int(input("Enter number of shares: "))
    holdings[symbol] = shares
    
print("\n----- Portfolio Report -----")

for company, shares_owned in holdings.items():
    if company in prices:
        stock_rate = prices[company]
        stock_value = shares_owned * stock_rate
        grand_total += stock_value
        print( f"{company} : {shares_owned} shares × ${stock_rate} = ${stock_value}" )
    else:
        print(f"{company} stock price not found")

print("--------------------------------")
print(f"Total Portfolio Value = ${grand_total}")

# Save result into file
choice = input("\nSave report to file? (yes/no): ").lower()

if choice == "yes":

    with open("stock_report.txt", "w") as report:

        report.write("Portfolio Report\n")
        report.write("--------------------------\n")

        for company, shares_owned in holdings.items():

            if company in prices:

                stock_rate = prices[company]

                stock_value = shares_owned * stock_rate

                report.write(
                    f"{company} : {shares_owned} shares × ${stock_rate} = ${stock_value}\n"
                )

        report.write("--------------------------\n")
        report.write(f"Total Portfolio Value = ${grand_total}")

    print("Report saved successfully!")