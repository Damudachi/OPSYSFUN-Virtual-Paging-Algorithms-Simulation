import optimal
import lru
import mru
import second_chance

def display_results(algo_name, steps, faults, hits):
    """
    Formats and prints the simulation results.
    Satisfies conditions: Number of pages, Frames, Reference string, 
    Page interrupts, Success Rate, and Failure Rate.
    """
    total_requests = len(steps)
    
    print(f"\n{'='*25} {algo_name.upper()} RESULTS {'='*25}")
    print(f"{'Step':<5} | {'Page':<5} | {'Frames':<25} | {'Result':<10}")
    print("-" * 70)
    
    for idx, step in enumerate(steps):
        # Displays the "Page reference string/requested pages"
        frames_display = str(step['frames'])
        print(f"{idx+1:<5} | {step['page']:<5} | {frames_display:<25} | {step['result']:<10}")
    
    print("-" * 70)
    
    # Satisfying the specific conditions for your output
    print(f"Number of Pages (Total Requests): {total_requests}")
    print(f"Page Interrupts (Total Faults):   {faults}")
    print(f"Total Hits:                       {hits}")
    
    if total_requests > 0:
        success_rate = (hits / total_requests) * 100
        failure_rate = (faults / total_requests) * 100
        
        print(f"Success Rate (Hit Ratio):         {success_rate:.2f}%")
        print(f"Failure Rate (Miss Ratio):        {failure_rate:.2f}%")
    
    print("=" * 60)

def get_input():
    """Handles user input for pages and frames with error checking."""
    try:
        raw_pages = input("Enter page reference string (space-separated, e.g., 7 0 1 2): ")
        if not raw_pages.strip():
            return None, None
        pages = [int(x) for x in raw_pages.split()]
        frames_count = int(input("Enter number of frames: "))
        return pages, frames_count
    except ValueError:
        print("\n[!] Invalid input. Please ensure pages are integers separated by spaces.")
        return None, None

def main_menu():
    while True:
        print("\n===== PAGE REPLACEMENT ALGORITHM SIMULATOR =====")
        print("[1] LRU (Least Recently Used)")
        print("[2] Optimal (Belady's Algorithm)")
        print("[3] MRU (Most Recently Used)")
        print("[4] Second Chance (Clock)")
        print("[0] Exit")
        
        choice = input("Select an algorithm: ")

        if choice == "0":
            print("Exiting Simulator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("\n[!] Invalid choice or Algorithm not yet implemented.")
            continue

        pages, frames_count = get_input()
        if pages is None:
            continue

        if choice == "1":
            # Calling run_lru from lru.py
            steps, faults, hits = lru.run_lru(pages, frames_count)
            display_results("LRU", steps, faults, hits)
        elif choice == "2":
            # Calling run_optimal from optimal.py
            steps, faults, hits = optimal.run_optimal(pages, frames_count)
            display_results("Optimal", steps, faults, hits)
        elif choice == "3":
            # Calling run_mru from mru.py
            steps, faults, hits = mru.run_mru(pages, frames_count)
            display_results("MRU", steps, faults, hits)
        elif choice == "4":
            # Calling run_second_chance from second_chance.py
            steps, faults, hits = second_chance.run_second_chance(pages, frames_count)
            display_results("Second Chance", steps, faults, hits)

if __name__ == "__main__":
    main_menu()