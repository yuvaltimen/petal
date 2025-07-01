#!/bin/bash
set -e

echo "🔍 Validating version consistency..."

PYPROJECT_VERSION=$(grep -E '^version = ' pyproject.toml | cut -d'"' -f2)
INIT_VERSION=$(grep -E '^__version__ = ' petal/src/__init__.py | cut -d'"' -f2)

if [[ "$PYPROJECT_VERSION" != "$INIT_VERSION" ]]; then
  echo "❌ Version mismatch:"
  echo "   - pyproject.toml: $PYPROJECT_VERSION"
  echo "   - __init__.py:    $INIT_VERSION"
  exit 1
fi

echo "✅ Version is consistent: $PYPROJECT_VERSION"

