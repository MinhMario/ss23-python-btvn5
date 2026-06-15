from data.players import player_records
from utils.item_utils import open_treasure_chest, buy_item
from utils.battle_utils import fight_monster
from reports.dungeon_report import display_players, show_leaderboard


while True:
        print('\n===== RIKKEI DUNGEON - PYTHON MODULE ADVENTURE =====')
        print('1. Hiển thị danh sách người chơi')
        print('2. Mở rương báu ngẫu nhiên')
        print('3. Mua vật phẩm trong cửa hàng')
        print('4. Chiến đấu với quái vật')
        print('5. Xem bảng xếp hạng người chơi')
        print('6. Thoát chương trình')
        print('====================================================')

        choice = input('Chọn chức năng (1-6): ').strip()

        match choice:
            case '1': display_players(player_records)
            case '2': open_treasure_chest(player_records)
            case '3': buy_item(player_records)
            case '4': fight_monster(player_records)
            case '5': show_leaderboard(player_records)
            case '6':
                print('Cảm ơn bạn đã tham gia Rikkei Dungeon!')
                break
            case _:
                print('Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 6.')

