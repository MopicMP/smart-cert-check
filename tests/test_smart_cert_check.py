"""Tests for smart-cert-check."""

import pytest
from smart_cert_check import check


class TestCheck:
    """Test suite for check."""

    def test_basic(self):
        """Test basic usage."""
        result = check("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            check("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = check(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
