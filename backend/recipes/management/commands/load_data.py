import json
from django.core.management.base import BaseCommand
from recipes.models import Recipe
def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
def safe_int(value):
    return value if isinstance(value, int) else None
class Command(BaseCommand):
    help = 'Load recipes from fixed JSON file'
    def handle(self, *args, **kwargs):
        with open('recipes_fixed.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        skipped = 0
        success = 0
        for entry in data:
            try:
                title = entry.get('title')
                if not title:  # Skip if title is missing
                    continue

                Recipe.objects.create(
                cuisine=entry.get('cuisine') or "",
                title=title,
                rating=safe_float(entry.get('rating')),
                prep_time=entry.get('prep_time') if isinstance(entry.get('prep_time'), int) else None,
                cook_time=entry.get('cook_time') if isinstance(entry.get('cook_time'), int) else None,
                total_time=entry.get('total_time') if isinstance(entry.get('total_time'), int) else None,
                description=entry.get('description') or "",
                nutrients=entry.get('nutrients'),
                serves=entry.get('serves') or ""
                )
                success += 1
            except Exception as e:
                print("Error:", e)
                skipped += 1
        print(f"✅ Done. {success} recipes added. {skipped} skipped.")
