from flask import Blueprint, jsonify
import json
from .data_loader import fetch_cosmetics_by_season
from .utils import categorize_items, generate_shop_items

shop_bp = Blueprint('shop', __name__)

@shop_bp.route('/shop/random/<season>', methods=['GET'])
def get_random_shop(season):
    try:
        all_items = fetch_cosmetics_by_season(season)
    except FileNotFoundError:
        return jsonify({'error': 'Data file not found'}), 500
    except json.JSONDecodeError:
        return jsonify({'error': 'Data file is not valid JSON'}), 500
    except Exception as e:
        return jsonify({'error': f'Unable to read data: {str(e)}'}), 500

    if not all_items:
        return jsonify({'error': f'No items found for season {season}'}), 404

    skins, cosmetics = categorize_items(all_items)

    if len(skins) < 4:
        return jsonify({'error': f'Not enough skins for season {season}. Found {len(skins)}, need 4.'}), 422

    if len(cosmetics) < 4:
        return jsonify({'error': f'Not enough cosmetics for season {season}. Found {len(cosmetics)}, need 4.'}), 422

    shop_items = generate_shop_items(skins, cosmetics)
    return jsonify(shop_items), 200

@shop_bp.route('/', methods=['GET'])
def index():
        return jsonify({'error': 'Method Not Allowed'}), 405

@shop_bp.app_errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not Found'}), 404

@shop_bp.app_errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method Not Allowed'}), 405

@shop_bp.app_errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal Server Error'}), 500