import glob


def find_wma(folder):

    # this variable defines which file name and extension will be searched
    query = "**/*.wma"

    entries = glob.glob(query, root_dir=f"{folder}", recursive=True)
    entries_num = len(entries)
    # if entries_num == 0:
        # print(f"no results for query: {query}")
    # else:
        # print(f"Found {entries_num} result(s) for query: {query}")

    # print("-" * 10)

    # for entry in entries:
        # print(entry)

    return entries




# find_wma(folder="/home/spiced/Music/Music/Music/Treyarch Sound/Call of Duty_ Black Ops/")