import re

def parse_srt(srt_content):
    """Parses SRT content into a list of dictionaries."""
    # Regex to capture index, timecode, and text (handling multiline text)
    # Removed the inline (?s) flag, rely solely on re.DOTALL argument
    pattern = re.compile(
        r"(\d+)\r?\n"                                      # 1: Index
        r"(\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3})\r?\n" # 2: Timecode
        r"(.+?)"                                        # 3: Subtitle text (non-greedy)
        r"(?=\r?\n\r?\n|\Z)",                                 # Positive lookahead for blank line or end of string
        re.DOTALL  # Make '.' match newline characters
    )
    matches = pattern.findall(srt_content)

    subtitles = []
    for match in matches:
        # Indices are based on capture groups
        try:
            index = int(match[0])
            timecode = match[1].strip()
            text = match[2].strip()
            subtitles.append({"index": index, "timecode": timecode, "text": text})
        except IndexError:
            print(f"Warning: Skipping malformed match: {match}")

    return subtitles
