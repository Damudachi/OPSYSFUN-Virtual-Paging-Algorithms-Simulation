def run_fifo(pages, frames_count):
    frames = []
    page_faults = 0
    hits = 0
    steps = []
    
    # We use this pointer to track which index to replace next (FIFO)
    replacement_index = 0

    for page in pages:
        if page in frames:
            hits += 1
            result = "HIT"
        else:
            page_faults += 1
            result = "FAULT"

            if len(frames) < frames_count:
                # Still filling up empty slots
                frames.append(page)
            else:
                # Frames are full; replace the oldest (at replacement_index)
                frames[replacement_index] = page
                # Move pointer to the next slot (circular)
                replacement_index = (replacement_index + 1) % frames_count

        steps.append({
            "page": page,
            "frames": frames.copy(),
            "result": result
        })

    return steps, page_faults, hits