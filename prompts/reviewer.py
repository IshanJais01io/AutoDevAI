def build_review_prompt(file_contents):

    return f"""
You are an expert Staff Software Engineer.

Review the following Python source files.

Identify:

1. Bugs
2. Security Issues
3. Performance Problems
4. Maintainability Issues
5. Code Smells
6. Refactoring Suggestions

Provide your report using this format.

## Summary

## Bugs

## Security

## Performance

## Maintainability

## Recommendations

Source Code:

{file_contents}
"""