def run_mru(pages, frames_count):
    frames = []
    page_faults = 0
    hits = 0
    steps = []

    # Tracks the page that was accessed most recently.
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
                replace_index = frames.index(most_recent_page)
                frames[replace_index] = page

        most_recent_page = page

        steps.append({
            "page": page,
            "frames": frames.copy(),
            "result": result
        })

    return steps, page_faults, hits