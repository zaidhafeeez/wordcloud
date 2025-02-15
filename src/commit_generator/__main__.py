import random
import sys
import logging

from commit_generator.generator import CommitGenerator

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    try:
        generator = CommitGenerator()
        num_commits = int(sys.argv[1]) if len(sys.argv) > 1 else 5
        
        logger.info(f"Starting to generate {num_commits} commits")
        
        successful_commits = 0
        for i in range(num_commits):
            logger.debug(f"Generating commit {i+1}/{num_commits}")
            if generator.create_commit(random.randint(1, 3)):
                successful_commits += 1
            else:
                logger.error(f"Failed to create commit {i+1}")
        
        logger.info(f"Successfully created {successful_commits}/{num_commits} commits")
        
        if successful_commits == 0:
            sys.exit(1)
        
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
