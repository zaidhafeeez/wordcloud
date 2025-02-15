import random
import sys
from commit_generator.generator import CommitGenerator

def main():
    generator = CommitGenerator()
    num_commits = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    
    for _ in range(num_commits):
        generator.create_commit(random.randint(1, 3))

if __name__ == "__main__":
    main()
