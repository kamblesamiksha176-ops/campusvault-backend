# CampusVault - Contributing Guide

## Code of Conduct

- Be respectful and inclusive
- Support each other's learning
- Follow project conventions
- Report issues constructively

## How to Contribute

### 1. Fork the Repository
```bash
git clone https://github.com/yourusername/campusvault.git
cd campusvault
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/add-new-feature
```

### 3. Make Changes
- Follow code style guidelines
- Write tests for new features
- Update documentation

### 4. Commit Changes
```bash
git add .
git commit -m "feat: add new feature"
```

### 5. Push and Create Pull Request
```bash
git push origin feature/add-new-feature
```

## Code Style

### Backend (Python)
```python
# Follow PEP 8
# Use type hints
# Write docstrings

def get_resources(user_id: str, limit: int = 10) -> List[Resource]:
    """
    Get resources for a specific user.
    
    Args:
        user_id: The user's unique identifier
        limit: Maximum number of resources to return
        
    Returns:
        List of Resource objects
    """
    pass
```

### Frontend (Dart)
```dart
// Use const constructors
// Follow Dart conventions
// Document complex logic

class ResourceCard extends StatelessWidget {
  /// The resource title to display
  final String title;
  
  const ResourceCard({
    Key? key,
    required this.title,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Text(title),
    );
  }
}
```

## Testing

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
flutter test
```

## Documentation

- Update README for major features
- Add comments for complex code
- Include examples where relevant
- Keep API documentation updated

## Pull Request Checklist

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Commit messages follow conventions

## Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation
- **style**: Code style changes
- **refactor**: Code refactoring
- **perf**: Performance improvement
- **test**: Adding/updating tests
- **chore**: Maintenance tasks

### Example
```
feat(ai): implement quiz generation from topics

Add functionality to generate quiz questions using OpenAI API.
Includes validation and error handling.

Closes #123
```

## Issue Reporting

When reporting issues, include:
1. Clear description of the problem
2. Steps to reproduce
3. Expected vs actual behavior
4. Environment details (OS, versions)
5. Error logs/screenshots if applicable

### Issue Template
```
## Description
Brief description of the issue

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: 
- Browser/Device:
- Flutter/Python version:
```

## Review Process

1. Automated tests run
2. Code review by maintainers
3. Feedback provided
4. Changes requested (if needed)
5. Approval and merge

## Getting Help

- Check existing documentation
- Review similar code
- Ask in discussions
- Contact maintainers

## Recognition

Contributors will be recognized in:
- README contributors section
- Release notes
- GitHub contributor page

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to CampusVault! 🎓
