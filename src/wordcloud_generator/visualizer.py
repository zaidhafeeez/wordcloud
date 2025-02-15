import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Tuple
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from .config import WORDCLOUD_CONFIG, COLOR_SCHEMES, STOPWORDS

logger = logging.getLogger(__name__)

class CommitWordCloudGenerator:
    def __init__(self, output_dir: str = "."):
        self.output_dir = Path(output_dir)
        self.config = WORDCLOUD_CONFIG
        self.color_scheme = 'github'
        
    def generate_mask(self) -> np.ndarray:
        width = self.config['dimensions']['width']
        height = self.config['dimensions']['height']
        margin = self.config['dimensions']['margin']
        
        # Create rounded rectangle mask
        mask = np.zeros((height, width), dtype=np.uint8)
        radius = int(min(width, height) * 0.1)
        
        # Fill main rectangle
        mask[margin:-margin, margin:-margin] = 255
        
        return mask
    
    def color_func(self, word: str, font_size: int, *args, **kwargs) -> str:
        colors = COLOR_SCHEMES[self.color_scheme]
        return np.random.choice(colors)
    
    def generate(self, text: str, output_name: str = "commit_wordcloud") -> Tuple[str, dict]:
        try:
            mask = self.generate_mask()
            
            wordcloud = WordCloud(
                **self.config['appearance'],
                mask=mask,
                stopwords=STOPWORDS,
                color_func=self.color_func
            ).generate(text)
            
            # Create visualization
            plt.figure(figsize=(12, 6), dpi=100, facecolor='white')
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            
            # Add metadata
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            plt.text(0.99, 0.01, 
                    f"Generated: {timestamp}\nTheme: {self.color_scheme}",
                    fontsize=8, color='gray', alpha=0.7,
                    transform=plt.gca().transAxes, 
                    ha='right', va='bottom')
            
            # Save files
            svg_path = self.output_dir / f"{output_name}.svg"
            plt.savefig(svg_path, format='svg', dpi=300, bbox_inches='tight')
            plt.close()
            
            metadata = {
                "theme": self.color_scheme,
                "timestamp": timestamp,
                "word_count": len(wordcloud.words_),
                "top_words": sorted(wordcloud.words_.items(), 
                                  key=lambda x: x[1], 
                                  reverse=True)[:10]
            }
            
            return str(svg_path), metadata
            
        except Exception as e:
            logger.error(f"Error generating word cloud: {e}")
            raise
