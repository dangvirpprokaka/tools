def in_menu():
    # Gom key theo prefix (số trước dấu chấm)
    grouped = {}
    for key in tool_map:
        if '.' not in key:
            continue
        prefix = key.split('.')[0]
        if prefix not in grouped:
            grouped[prefix] = []
        grouped[prefix].append(key)

    # Tên tiêu đề tương ứng theo prefix
    menu_titles = {
        "1": "Golike",
        "2": "Trao Đổi Sub",
        "3": "Tương Tác Chéo",
        "4": "Facebook",
        "5": "Tiện Ích Khác"
    }

    # In từng nhóm
    for prefix in sorted(menu_titles.keys(), key=int):
        if prefix not in grouped:
            continue

        title = menu_titles[prefix]
        print(f"{trang}╔" + "─" * width + "╗")
        print(f"{trang}|{xnhac}{title.center(width)}{trang}|")
        print(f"{trang}╚" + "─" * width + "╝")

        for key in sorted(grouped[prefix]):
            desc = tool_map[key][0]
            print(f'{hdang}Nhập {do}[{vang}{key}{do}] {luc}{desc}')

    print(f"{trang}" + "─" * 57)
