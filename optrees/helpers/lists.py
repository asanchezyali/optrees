def item_check_exists(list, index):
    try:
        list[index]
        return True
    except IndexError:
        return False
