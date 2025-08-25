import re
import random
from .pricing import get_price_for_item


def format_item_name(name):
    formatted = re.sub(r'[^\w\s]', '', name)
    formatted = formatted.replace(' ', '_')
    return formatted


def categorize_items(items):
    skins = []
    cosmetics = []
    for item in items:
        item_type = item.get('type', {}).get('value', '').lower()
        if item_type == 'outfit':
            skins.append(item)
        elif item_type in ['backpack', 'glider', 'pickaxe', 'emote', 'wrap', 'loadingscreen', 'music', 'emoji', 'spray']:
            cosmetics.append(item)
    return skins, cosmetics


def generate_shop_items(skins, cosmetics):
    shop_items = []
    selected_skins = random.sample(skins, min(4, len(skins)))
    for skin in selected_skins:
        shop_items.append({
            'shopName': format_item_name(skin.get('name', 'Unknown_Skin')) + '_Skin',
            'price': get_price_for_item(skin)
        })
    selected_cosmetics = random.sample(cosmetics, min(4, len(cosmetics)))
    for cosmetic in selected_cosmetics:
        item_type = cosmetic.get('type', {}).get('value', 'Item').title()
        shop_items.append({
            'shopName': format_item_name(cosmetic.get('name', 'Unknown_Item')) + f'_{item_type}',
            'price': get_price_for_item(cosmetic)
        })
    return shop_items
