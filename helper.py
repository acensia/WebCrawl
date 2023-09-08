

def sort_path(path):
    folders = path.split("\\")
    style = folders[2]
    num = int(folders[3])
    return (style, num)