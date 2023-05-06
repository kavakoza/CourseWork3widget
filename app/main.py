from app.utils import display_transactions

if __name__ == "__main__":
    print_data = display_transactions()
    for item in print_data:
        print(item)