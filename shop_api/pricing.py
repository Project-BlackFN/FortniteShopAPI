def get_price_for_item(item):
    rarity_obj = item.get('rarity', {})
    if isinstance(rarity_obj, dict):
        rarity = rarity_obj.get('displayValue', '').lower()
    else:
        rarity = str(rarity_obj).lower() if rarity_obj else ''
    
    item_type_obj = item.get('type', {})
    if isinstance(item_type_obj, dict):
        item_type = item_type_obj.get('value', '').lower()
    else:
        item_type = str(item_type_obj).lower() if item_type_obj else ''
    
    series_obj = item.get('series')
    if series_obj and isinstance(series_obj, dict):
        series = series_obj.get('value', '').lower()
    else:
        series = str(series_obj).lower() if series_obj else None

    if series:
        if series in ['gaming legends series', 'marvel series', 'star wars series', 'dc series', 'icon series']:
            if item_type == 'outfit':
                return 1500
            elif item_type == 'pickaxe':
                return 1200
            elif item_type == 'backpack':
                return 1200
            elif item_type == 'emote':
                return 500
            elif item_type == 'glider':
                return 1200
            elif item_type == 'wrap':
                return 700
            elif item_type == 'loadingscreen':
                return 500
            elif item_type == 'music':
                return 200
            elif item_type == 'emoji':
                return 200
        elif series == 'lava series':
            if item_type in ['outfit', 'glider', 'backpack']:
                return 2000
            elif item_type == 'pickaxe':
                return 1200
            elif item_type == 'loadingscreen':
                return 500
            elif item_type == 'music':
                return 200
            elif item_type == 'emoji':
                return 200
        elif series in ['shadow series', 'frozen series', 'slurp series', 'dark series']:
            if item_type == 'outfit':
                return 1500
            elif item_type == 'pickaxe':
                return 1200
            elif item_type == 'backpack':
                return 1200
            elif item_type == 'glider':
                return 1200
            elif item_type == 'wrap':
                return 700
            elif item_type == 'loadingscreen':
                return 500
            elif item_type == 'music':
                return 200
            elif item_type == 'emoji':
                return 200

    if item_type == 'outfit':
        if rarity == 'legendary':
            return 2000
        elif rarity == 'epic':
            return 1500
        elif rarity == 'rare':
            return 1200
        elif rarity == 'uncommon':
            return 800
    elif item_type == 'pickaxe':
        if rarity == 'epic':
            return 1200
        elif rarity == 'rare':
            return 800
        elif rarity == 'uncommon':
            return 500
    elif item_type == 'backpack':
        if rarity == 'legendary':
            return 2000
        elif rarity == 'epic':
            return 1500
        elif rarity == 'rare':
            return 1200
        elif rarity == 'uncommon':
            return 200
    elif item_type in ['emote', 'spray', 'emoji']:
        if rarity == 'legendary':
            return 2000
        elif rarity == 'epic':
            return 800
        elif rarity == 'rare':
            return 500
        elif rarity == 'uncommon':
            return 200
    elif item_type == 'glider':
        if rarity == 'legendary':
            return 2000
        elif rarity == 'epic':
            return 1200
        elif rarity == 'rare':
            return 800
        elif rarity == 'uncommon':
            return 500
    elif item_type == 'wrap':
        if rarity == 'legendary':
            return 1200
        elif rarity == 'epic':
            return 700
        elif rarity == 'rare':
            return 500
        elif rarity == 'uncommon':
            return 300
    elif item_type == 'loadingscreen':
        if rarity in ['legendary', 'epic', 'rare']:
            return 500
        elif rarity == 'uncommon':
            return 200
    elif item_type == 'music':
        if rarity in ['legendary', 'epic']:
            return 500
        elif rarity in ['rare', 'uncommon']:
            return 200

    return 1000