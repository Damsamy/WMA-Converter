import glob


def find_wma(folder):

    # this variable defines which file name and extension will be searched
    query = "**/*.wma"

    entries = glob.glob(query, root_dir=f"{folder}", recursive=True)
    entries_num = len(entries)

    return entries
