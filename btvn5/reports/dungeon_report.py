from utils.player_utils import get_status


def display_players(records):
    if not records:
        print('Hệ thống chưa có dữ liệu người chơi.')
        return

    print('--- DANH SÁCH NGƯỜI CHƠI ---')
    for i, p in enumerate(records, 1):
        status = get_status(p['hp'])
        print(f"{i}. Mã: {p['player_id']} | Tên: {p['name']} | "
              f"HP: {p['hp']} | Mana: {p['mana']} | Gold: {p['gold']} | "
              f"Level: {p['level']} | Trạng thái: {status}")
    print('------------------------------')


def show_leaderboard(records):
    if not records:
        print('Hệ thống chưa có dữ liệu người chơi.')
        return

    sorted_records = sorted(
        records,
        key=lambda p: (p['level'], p['gold'], p['hp']),
        reverse=True
    )

    print('--- BẢNG XẾP HẠNG NGƯỜI CHƠI ---')
    for i, p in enumerate(sorted_records, 1):
        print(f"{i}. {p['name']} | Level: {p['level']} | Gold: {p['gold']} | HP: {p['hp']}")
    print('--------------------------------')