def run_second_chance(pages, frames_count):
    frames = []
    reference_bits = []
    pointer = 0
    page_faults = 0
    hits = 0
    steps = []

    for page in pages:
        if page in frames:
            hits += 1
            result = "HIT"
            page_index = frames.index(page)
            reference_bits[page_index] = 1
        else:
            page_faults += 1
            result = "FAULT"

            if len(frames) < frames_count:
                frames.append(page)
                reference_bits.append(1)
            else:
                # Rotate until we find a page with reference bit 0.
                while reference_bits[pointer] == 1:
                    reference_bits[pointer] = 0
                    pointer = (pointer + 1) % frames_count

                frames[pointer] = page
                reference_bits[pointer] = 1
                pointer = (pointer + 1) % frames_count

        steps.append({
            "page": page,
            "frames": frames.copy(),
            "result": result
        })

    return steps, page_faults, hits
