import random
import os
import logging
from typing import List, Optional
from dataclasses import dataclass
from .constants import ACTIVITIES, FEATURES, COMPONENTS

logger = logging.getLogger(__name__)

@dataclass
class FileChange:
    path: str
    content: str

class CommitGenerator:
    def create_random_file_change(self) -> Optional[FileChange]:
        try:
            file_type = random.choice(['python', 'react', 'html', 'css'])
            templates = {
                'python': self._create_python_file,
                'react': self._create_react_file,
                'html': self._create_html_file,
                'css': self._create_css_file
            }
            
            return templates[file_type]()
        except Exception as e:
            print(f"Error creating file: {e}")
            return None

    def _create_python_file(self) -> FileChange:
        filename = f"src/python/module_{random.randint(1, 100)}.py"
        content = self._get_python_template()
        return FileChange(filename, content)

    def _get_python_template(self) -> str:
        return f"""
class {random.choice(['User', 'Data', 'Service'])}Controller:
    def __init__(self) -> None:
        self.initialized = True
    
    def process_data(self, data: dict) -> dict:
        return data
"""

    # ... Similar methods for other file types ...

    def generate_commit_message(self) -> str:
        activity_type = random.choice(list(ACTIVITIES.keys()))
        template = random.choice(ACTIVITIES[activity_type])
        placeholder = random.choice(FEATURES if activity_type == 'feat' else COMPONENTS)
        
        message = template.format(feature=placeholder, component=placeholder)
        
        if random.random() < 0.3:
            scope = random.choice(COMPONENTS)
            return f"{activity_type}({scope}): {message}"
        return f"{activity_type}: {message}"

    def create_commit(self, num_files: int = 1) -> bool:
        try:
            changed_files = []
            for _ in range(num_files):
                file_change = self.create_random_file_change()
                if file_change:
                    logger.debug(f"Creating file: {file_change.path}")
                    os.makedirs(os.path.dirname(file_change.path), exist_ok=True)
                    with open(file_change.path, 'w') as f:
                        f.write(file_change.content.strip())
                    changed_files.append(file_change.path)

            if not changed_files:
                logger.error("No files were changed")
                return False

            for file in changed_files:
                logger.debug(f"Staging file: {file}")
                if os.system(f'git add "{file}"') != 0:
                    logger.error(f"Failed to stage file: {file}")
                    return False

            message = self.generate_commit_message()
            logger.info(f"Creating commit with message: {message}")
            result = os.system(f'git commit -m "{message}"')
            if result != 0:
                logger.error(f"Failed to create commit, git returned: {result}")
            return result == 0

        except Exception as e:
            logger.error(f"Error during commit creation: {e}")
            return False
