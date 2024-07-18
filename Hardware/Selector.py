import os

def main():
    while True:
        print("\nMenu:")
        print("1. Run pkt_xmt.py")
        print("2. Run pkt_rcv.py and strip_preamble.py")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            input_file = input("Enter the input file name: ")
            os.system(f'python.exe pkt_xmt.py --InFile="{input_file}"')
        elif choice == '2':
            os.system('python.exe pkt_rcv.py')
            received_file = input("Enter the name of the received file to be processed with strip_preamble.py: ")
            os.system(f'python.exe strip_preamble.py Received.tmp "{received_file}"')
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
