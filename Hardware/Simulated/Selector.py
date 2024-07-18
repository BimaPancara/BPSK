import subprocess
import os

def main():
    # Start `channelSimulated.py` automatically in a separate process.
    channel_process = subprocess.Popen(['python.exe', 'channelSimulated.py'])

    try:
        while True:
            print("\nMenu:")
            print("1. Transmit")

            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                # Run `pkt_rcv.py` concurrently
                rcv_process_2 = subprocess.Popen(['python.exe', 'pkt_rcv.py'])

                # Wait for user input before proceeding with the next commands
                input("Press Enter to continue...")

                # Run the transmission script
                subprocess.run(['python.exe', 'pkt_xmt.py', '--InFile="Kirim.txt"'])
                input("Press Enter to continue...")

                # Run the script to strip the preamble
                subprocess.run(['python.exe', 'strip_preamble.py', 'Rx.tmp', 'Rx.txt'])

                # Wait for `pkt_rcv.py` to complete if necessary
                rcv_process_2.wait()



            elif choice == '3':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please select again.")

    finally:
        # Terminate the `channelSimulated.py` process if it is still running.
        channel_process.terminate()
        channel_process.wait()
        print("channelSimulated.py process terminated.")

if __name__ == "__main__":
    main()
