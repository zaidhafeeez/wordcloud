from typing import Dict, List, Any
import colorsys

WORDCLOUD_CONFIG: Dict[str, Any] = {
    "dimensions": {
        "width": 1200,
        "height": 600,
        "margin": 20
    },
    "appearance": {
        "min_font_size": 12,
        "max_font_size": 90,
        "prefer_horizontal": 0.7,
        "relative_scaling": 0.7,
        "background_color": "white",
        "mode": "RGBA"
    },
    "processing": {
        "min_word_length": 3,
        "collocations": True,
        "normalize_plurals": True
    }
}

STOPWORDS: set[str] = {
    'merge', 'pull', 'request', 'branch', 'fix', 'fixed', 'bug',
    'update', 'updated', 'commit', 'version', 'v1', 'v2', 'changelog',
    'initial', 'add', 'added', 'remove', 'removed', 'change', 'changed',
    'bump', 'upgrade', 'upgraded', 'downgrade', 'implement', 'implemented',
    'feat', 'feature', 'chore', 'task', 'doc', 'docs', 'test', 'tests'
}

COLOR_SCHEMES: Dict[str, List[str]] = {
    'github': ['#0366d6', '#28a745', '#d73a49', '#6f42c1', '#24292e'],
    'neon': ['#FF1493', '#00FF00', '#FFD700', '#00FFFF', '#FF4500'],
    'pastel': ['#FFB3BA', '#BAFFC9', '#BAE1FF', '#FFFFBA', '#FFB3F7'],
    'sunset': ['#FF8C42', '#FF5733', '#C70039', '#900C3F', '#581845'],
    'ocean': ['#006D77', '#83C5BE', '#EDF6F9', '#FFDDD2', '#E29578']
}
