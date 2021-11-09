# книга Свейгарт розділ 5 практична робота інвентар пригодницької гри.
import json


def displayInventory():
    try:
        info_about_player_inventory = {'rope': int(input('add rope')),
                                       'torch': int(input('add torch')),
                                       'dagger': int(input('add dagger')),
                                       'arrow': int(input('add arrow'))
                                       }
        return info_about_player_inventory
    except ValueError:
        print('Catostrofa')


def write_json_file_with_user_inventory():
    with open('user_inventory.json', 'w', encoding='utf-8') as file_json:
        json.dump(displayInventory(), file_json, ensure_ascii=False, indent=4)
    return 'user_inventory.json'


def read_json_file():
    with open(write_json_file_with_user_inventory(), 'r') as file_json:
        user_inventory = json.load(file_json)
        print(type(user_inventory))
    return user_inventory

def more_info():
    inventory_user = read_json_file()
    item_total = 0
    for key, values in inventory_user.items():
        print(str(values) + ' ' + key)
        item_total += values
        print(f'Гравець має стільки предметів:-{item_total}.\nУ своєму інвентарі.')


more_info()