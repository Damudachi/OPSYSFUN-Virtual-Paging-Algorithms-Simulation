# =====================================================
# MRU (MOST RECENTLY USED) PAGE REPLACEMENT SIMULATOR
# =====================================================

def print_results(hits, faults, total, capacity):

    hit_ratio = (hits / total) * 100
    failure_rate = (faults / total) * 100

    print("-----------------------------------------------------")
    print(f"Number of Pages (Total Requests): {total}")
    print(f"Number of Frames: {capacity}")
    print(f"Total Hits: {hits}")
    print(f"Page Interrupts (Total Faults): {faults}")
    print(f"Success Rate (Hit Ratio): {hit_ratio:.2f}%")
    print(f"Failure Rate (Miss Ratio): {failure_rate:.2f}%")
    print("=====================================================")


def mru_simulation(pages, capacity):

    frames = []
    last_used = {}   # tracks most recent usage
    hits = 0
    faults = 0

    print("\n==================== MRU RESULTS ====================")
    print("Step | Page | Frames        | Result")
    print("-----------------------------------------------------")

    for step, page in enumerate(pages, start=1):

        # PAGE HIT
        if page in frames:
            hits += 1
            result = "HIT"

        # PAGE FAULT
        else:
            faults += 1
            result = "FAULT"

            # If frames are not full
            if len(frames) < capacity:
                frames.append(page)

            # Replace MOST RECENTLY USED page
            else:
                mru_page = max(last_used, key=last_used.get)
                replace_index = frames.index(mru_page)
                frames[replace_index] = page
                del last_used[mru_page]

        # Update most recent usage
        last_used[page] = step

        # Display simulation step
        print(f"{step:<4} | {page:<4} | {str(frames):<13} | {result}")

    # Show final statistics
    print_results(hits, faults, len(pages), capacity)


# ================= MAIN PROGRAM =================
def main():

    print("====== PAGE REPLACEMENT ALGORITHM SIMULATOR ======")
    print("[1] MRU (Most Recently Used)")
    print("[0] Exit")

    choice = input("Select an algorithm: ")

    if choice == "1":

        ref_string = input(
            "Enter page reference string (space-separated, e.g., 7 0 1 2): "
        )

        try:
            pages = list(map(int, ref_string.split()))
            frames = int(input("Enter number of frames: "))

            mru_simulation(pages, frames)

        except ValueError:
            print("\n[!] Invalid input. Please enter numbers only.")

    else:
        print("Program ended.")


# RUN PROGRAM
if __name__ == "__main__":
    main()