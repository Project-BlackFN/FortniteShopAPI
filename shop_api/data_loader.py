import os
import json
from .config import DATA_PATH

def fetch_cosmetics_by_season(season):
    if not os.path.isfile(DATA_PATH):
        raise FileNotFoundError('data.json not found')

    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cosmetics = data.get('data', [])
    filtered_items = []

    for item in cosmetics:
        introduction = item.get('introduction', {})
        item_season = introduction.get('season')
        
        rarity_obj = item.get('rarity', {})
        if isinstance(rarity_obj, dict):
            rarity = rarity_obj.get('displayValue', '').lower()
        else:
            rarity = str(rarity_obj).lower() if rarity_obj else ''
        
        if rarity == 'common' or item_season is None:
            continue

        if str(item_season).lower() == str(season).lower() or str(item_season) == str(season):
            filtered_items.append(item)

    return filtered_items