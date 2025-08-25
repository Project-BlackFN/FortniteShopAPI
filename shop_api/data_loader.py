import os
import json
from .config import DATA_PATH

def fetch_cosmetics_by_season(season):
    if not os.path.isfile(DATA_PATH):
        raise FileNotFoundError('data.json not found')
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    cosmetics = data.get('data', [])
    filtered = []
    for item in cosmetics:
        introduction = item.get('introduction', {})
        item_season = introduction.get('season')
        rarity = item.get('rarity', {}).get('displayValue', '').lower()
        if rarity == 'common':
            continue
        if item_season is None:
            continue
        if str(item_season).lower() == str(season).lower() or str(item_season) == str(season):
            filtered.append(item)
    return filtered
