from collections import defaultdict

def in_menu():
    # Gom các key theo nhóm prefix (1, 2, 3, ...)
    grouped = defaultdict(list)
    for key in tool_map:
        if "." in key:
            group = key.split(".")[0]
            grouped[group].append(key)

    # Tên tiêu đề cho mỗi nhóm
    menu_titles = {
        "1": "Golike",
        "2": "Trao Đổi Sub",
        "3": "Tương Tác Chéo",
        "4": "Facebook",
        "5": "Tiktok"
    }

    # In từng nhóm menu
    for group_id, title in menu_titles.items():
        keys = grouped.get(group_id)
        if not keys:
            continue
        print(f"{trang}╔" + "─" * width + "╗")
        print(f"{trang}|{xnhac}{title.center(width)}{trang}|")
        print(f"{trang}╚" + "─" * width + "╝")
        for key in sorted(keys):
            print(f'{hdang}Nhập {do}[{vang}{key}{do}] {luc}{tool_map[key][0]}')

    print(f"{trang}" + "─" * 57)
