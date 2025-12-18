# Helper for searching through Spotify results

import csv


def songs_by_track_name(path: str, word: str) -> list[list[str]]:
    """Return all songs whose track name contains the given word."""

    # manually read the CSV
    file = open(path)
    lines = file.readlines()
    file.close()

    results = []

    # skip header, process rows
    for line in lines[1:]:
        parts = line.strip().split(",")  # split row into columns
        track_name = parts[0].lower()

        if word.lower() in track_name:
            results.append(parts)

    return results


def songs_by_artist(file_path: str, artist: str) -> list[list[str]]:
    """Searches through given file and returns a list of songs from given artist."""
    artist_col = 2

    songs = []

    # open the file
    with open(file_path) as f:
        # get rid of the header row
        _ = f.readline()

        # create a reader object
        r = csv.reader(f)

        # go through reader line by line
        for info in r:
            # if the current artist is "Kendrick"
            if info[artist_col] == artist:
                songs.append(info)

    return songs


def string_to_num(s: str) -> int:
    """Converts a string number with commas in it to an inteeger. (e.g. "1,223,222" -> 1223222)"""
    return int(s.replace(",", "")) if s else 0


songs_by_artist("data/spotify2024.csv", "Taylor Swift")
