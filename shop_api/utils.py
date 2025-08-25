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
        item_type_obj = item.get('type', {})
        if isinstance(item_type_obj, dict):
            item_type = item_type_obj.get('value', '').lower()
        else:
            item_type = str(item_type_obj).lower() if item_type_obj else ''
        
        if item_type == 'outfit':
            skins.append(item)
        elif item_type in ['backpack', 'glider', 'pickaxe', 'emote', 'wrap', 'loadingscreen', 'music', 'emoji', 'spray']:
            cosmetics.append(item)
    return skins, cosmetics


def generate_shop_items(skins, cosmetics):
    daily_items = []
    selected_skins = random.sample(skins, min(4, len(skins)))
    for skin in selected_skins:
        daily_items.append({
            "price": get_price_for_item(skin),
            "shopName": format_item_name(skin.get('name', 'Unknown_Skin')) + "_Skin"
        })
    
    featured_items = []
    selected_cosmetics = random.sample(cosmetics, min(4, len(cosmetics)))
    for cosmetic in selected_cosmetics:
        item_type_obj = cosmetic.get('type', {})
        if isinstance(item_type_obj, dict):
            item_type = item_type_obj.get('value', 'Item').title()
        else:
            item_type = str(item_type_obj).title() if item_type_obj else 'Item'
        
        featured_items.append({
            "price": get_price_for_item(cosmetic),
            "shopName": format_item_name(cosmetic.get('name', 'Unknown_Item')) + f"_{item_type}"
        })
    
    return {
        "daily": daily_items,
        "featured": featured_items
    }