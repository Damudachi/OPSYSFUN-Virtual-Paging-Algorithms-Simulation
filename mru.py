def run_mru(pages, frames_count):
    frames = []
    page_faults = 0
    hits = 0
    steps = []
    
    # We track the most recently used page by storing the last page that was accessed
    most_recent_page = None

    for page in pages:
        if page in frames:
            hits += 1
            result = "HIT"
        else:
            page_faults += 1
            result = "FAULT"

            if len(frames) < frames_count:
                frames.append(page)
            else:
                # In MRU, we replace the page that was JUST used/accessed
                # We find where the most_recent_page is in our frames and swap it
                replace_index = frames.index(most_recent_page)
                frames[replace_index] = page

        # Update the most recent page for the next iteration
        most_recent_page = page

        steps.append({
            "page": page,
            "frames": list(frames),
            "result": result
        })

    return steps, page_faults, hits