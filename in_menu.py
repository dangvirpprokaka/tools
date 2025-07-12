def in_menu():
    # Gom nhóm theo tiền tố (prefix) trước dấu chấm
    grouped = {}
    for key in tool_map:
        if '.' in key:
            prefix = key.split('.')[0]
            if prefix not in grouped:
                grouped[prefix] = []
            grouped[prefix].append(key)

    # Tiêu đề tương ứng cho từng nhóm
    menu_titles = {
        "1": "Golike",
        "2": "Trao Đổi Sub",
        "3": "Tương Tác Chéo",
        "4": "Facebook",
        "5": "Tiktok"
    }

    # In ra menu
    for prefix in sorted(menu_titles.keys(), key=int):
        if prefix not in grouped:
            continue

        title = menu_titles[prefix]
        print(f"{trang}╔" + "─" * width + "╗")
        print(f"{trang}|{xnhac}{title.center(width)}{trang}|")
        print(f"{trang}╚" + "─" * width + "╝")

        for key in sorted(grouped[prefix]):
            print(f'{hdang}Nhập {do}[{vang}{key}{do}] {luc}{tool_map[key][0]}')

    print(f"{trang}" + "─" * 57)
