from typing import Dict, List

ACTIVITIES: Dict[str, List[str]] = {
    'feat': [
        'add {feature} functionality',
        'implement {feature} module',
        'introduce {feature} support',
        'create new {feature} component'
    ],
    'fix': [
        'fix bug in {component}',
        'resolve {component} issue',
        'patch {component} vulnerability',
        'correct {component} behavior'
    ],
    'refactor': [
        'refactor {component} code',
        'optimize {component} performance',
        'improve {component} structure',
        'clean up {component} implementation'
    ],
    'docs': [
        'update {component} documentation',
        'add {component} examples',
        'improve {component} readme',
        'document {component} API'
    ],
    'test': [
        'add tests for {component}',
        'improve {component} test coverage',
        'create {component} integration tests',
        'fix flaky {component} tests'
    ]
}

FEATURES: List[str] = [
    'user authentication', 'data visualization', 'export', 'import',
    'search', 'filtering', 'sorting', 'pagination', 'caching',
    'logging', 'monitoring', 'reporting', 'backup', 'restore',
    'notification', 'validation'
]

COMPONENTS: List[str] = [
    'frontend', 'backend', 'database', 'API', 'UI',
    'authentication', 'authorization', 'cache', 'logger',
    'utils', 'core', 'config', 'tests', 'docs'
]
