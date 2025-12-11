# Intro to Sort
# Author: Ubial
# 4 December

import helper_spotify

# Sorting Algorithms
# The code below uses linear search to find songs from a particular artist
# We're going to sort the results using Selection Sort
#     * implement basic version
#     * implement sort with songs based on YouTube views in descending order


def selection_sort(l: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort

    Params:
        l - list of nums to be sorted
        ascending - True if order is ascending

    Returns:
        a sorted list"""

    num_items = len(l)

    # start at the beginning of list
    for i in range(num_items):
        candidate_num = l[i]
        candidate_index = i

        # check the rest of the list
        for j in range(i + 1, num_items):
            if ascending:
                if l[j] < candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
            else:
                if l[j] > candidate_num:
                    candidate_num = l[j]
                    candidate_index = j

        # swap the current index with the lowest
        l[i], l[candidate_index] = l[candidate_index], l[i]

    return l


def sort_songs(songs: list[list[str]], col: int, ascending=True) -> list[list[str]]:
    """Sort a list of spotify songs in place

    Params:
        songs - list of songs
        col - column to sort
        ascending - will sort ascending by default

    Returns: sorted list"""
    # Use Selection Sort to sort songs
    num_songs = len(songs)

    # Starting at the beginning of the list
    for i in range(num_songs):
        # Set this value to the candidate's value
        candidate_val = helper_spotify.string_to_num(songs[i][col])
        candidate_idx = i

        for j in range(i + 1, num_songs):
            this_songs_val = helper_spotify.string_to_num(songs[j][col])
            if ascending:
                if this_songs_val < candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j
            else:
                # If this val is higher than candidate
                if this_songs_val > candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j

        # Swap!
        songs[i], songs[candidate_idx] = songs[candidate_idx], songs[i]

    return songs


if __name__ == "__main__":
    # Task 1
    ed_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")
    for song in ed_songs:
        print(song[0], "\t", song[11])
    print()

    # Task 2
    ed_sorted_yt = sort_songs(ed_songs, 11, ascending=True)
    for song in ed_sorted_yt:
        print(song[0], "\t", song[11])
    print()

    # Task 3
    ed_sorted_tiktok = sort_songs(ed_songs, 12, ascending=False)
    for song in ed_sorted_tiktok:
        print(song[0], "\t", song[12])
    print()

    # Task 4
    songs_with_the = helper_spotify.songs_by_track_name("data/spotify2024.csv", "the")

    print("TASK 4 – Songs with 'the' in the track name")
    print("___________________________________________")
    for song in songs_with_the:
        print(song[0])

    # Task 5
    sorted_again = sort_songs(ed_sorted_tiktok, 12, ascending=False)
    for song in sorted_again:
        print(song[0], "\t", song[12])
    print()
