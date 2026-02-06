A README for your upgraded script works best when it does two things at once:  
• explains the tool clearly to new users  
• highlights the major improvements you added over the original version  

This draft does both and is structured so it can live directly in your repository.

---

# City Map Poster Generator

A command‑line tool for generating high‑quality, theme‑driven map posters for any city in the world.  
It uses OpenStreetMap data, OSMnx, and Matplotlib to produce clean, minimalist artwork suitable for printing.

This version extends the original script with major improvements in typography, caching, feature handling, internationalization, and output control.

---

## ✨ Key Features

### Map Rendering
- Fetches street networks, water features, and parks from OpenStreetMap  
- Applies hierarchical road styling (motorways → residential)  
- Supports custom color themes stored as JSON  
- Adds top and bottom gradient fades for a polished poster look  
- Crops the map intelligently to preserve aspect ratio while honoring the requested radius

### Typography
- Roboto font support with automatic fallback  
- Dynamic font scaling based on poster size  
- Automatic city‑name resizing to prevent overflow  
- Script‑aware formatting:
  - Latin scripts get spaced uppercase lettering  
  - Non‑Latin scripts (CJK, Arabic, Thai, etc.) keep natural casing and spacing  
- Optional display overrides for city and country names  
- Coordinates and attribution included by default

### Output Options
- PNG, SVG, and PDF export  
- Custom poster dimensions (width/height in inches)  
- Automatic filename generation with timestamps  
- Tight bounding boxes and minimal padding for print‑ready output

---

## 🚀 Enhancements Beyond the Original Script

### Caching System
- Street networks, water features, parks, and coordinates are cached on disk  
- Dramatically faster repeated runs  
- Reduces load on OSM and Nominatim  
- Robust error handling for cache read/write failures

### Smarter Data Fetching
- Separate caching for each feature type  
- Automatic retry logic for geocoding coroutines  
- Compensation for viewport cropping to ensure full coverage of the requested radius

### Improved Typography Engine
- Dynamic font scaling based on poster dimensions  
- Automatic reduction of city‑name font size for long names  
- Script detection to avoid spacing non‑Latin text  
- Cleaner fallback fonts when Roboto is unavailable

### Internationalization (i18n)
- `--display-city` and `--display-country` allow:
  - native‑script names  
  - alternate spellings  
  - multilingual posters  
- Script detection ensures correct formatting for languages like Japanese, Arabic, Thai, Korean, etc.

### More Robust Geometry Handling
- Filters out point features so water/park layers don’t produce stray dots  
- Projects all geometries into the graph CRS for consistent rendering  
- Ensures polygons and multipolygons render correctly

### Flexible CLI
- Custom width/height  
- Optional manual latitude/longitude override  
- Theme listing  
- Generate posters for all themes in one run  
- Country‑label override  
- Cleaner help text and examples

### Output Improvements
- Tight bounding box export  
- DPI control for PNG  
- Consistent margins  
- Automatic theme‑based filenames

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

You must also provide:

- `themes/` directory containing JSON theme files  
- `fonts/` directory containing Roboto font files (Bold, Regular, Light)

---

## 🧭 Usage

### Basic
```bash
python create_map_poster.py --city "Paris" --country "France"
```

### Choose a theme
```bash
python create_map_poster.py -c Tokyo -C Japan -t midnight_blue
```

### Custom size
```bash
python create_map_poster.py -c "Böblingen" -C Germany --width 11 --height 17
```

### Override display names (i18n)
```bash
python create_map_poster.py -c Kyoto -C Japan --display-city 京都市
```

### Generate posters for all themes
```bash
python create_map_poster.py -c Rome -C Italy --all-themes
```

### List themes
```bash
python create_map_poster.py --list-themes
```

---

## 📁 Output

Generated posters are saved in:

```
posters/
```

Filenames include city, theme, and timestamp.

---

## 📝 Notes

- Cached data is stored in `cache/`  
- Respectful rate‑limiting is built in for Nominatim  
- Long city names automatically shrink to avoid overflow  
- Non‑Latin scripts render without forced uppercase or spacing  

---

Example commands that showcase range and flexibility, starting from your real one and branching outward into different use‑cases:

```bash
python create_map_poster.py \
  --city "Fuquay-Varina" --country "USA" \
  --distance 4000 --all-themes \
  --size custom --width 27.94 --height 43.18 --unit cm
```

### Custom sizes in inches
```bash
python create_map_poster.py \
  --city "Böblingen" --country "Germany" \
  --distance 4500 --size custom --width 11 --height 17
```

### Standard poster with a specific theme
```bash
python create_map_poster.py \
  --city "Barcelona" --country "Spain" \
  --theme pastel_dream --distance 8000
```

### High‑density downtown view
```bash
python create_map_poster.py \
  --city "Tokyo" --country "Japan" \
  --theme neon_cyberpunk --distance 3500
```

### Wide metropolitan radius
```bash
python create_map_poster.py \
  --city "Mumbai" --country "India" \
  --theme contrast_zones --distance 20000
```

### Native‑script display names
```bash
python create_map_poster.py \
  --city "Kyoto" --country "Japan" \
  --display-city "京都市" --display-country "日本" \
  --theme japanese_ink
```

### Manual coordinates instead of geocoding
```bash
python create_map_poster.py \
  --city "Central Park" --country "USA" \
  --latitude 40.7829 --longitude -73.9654 \
  --theme noir --distance 6000
```

### Generate posters for all themes at a custom size
```bash
python create_map_poster.py \
  --city "Rome" --country "Italy" \
  --all-themes --width 12 --height 18
```

### SVG output for vector editing
```bash
python create_map_poster.py \
  --city "Paris" --country "France" \
  --theme noir --distance 10000 --format svg
```

