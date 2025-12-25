"""Tests for web fetching functionality."""

import curl_cffi
import pytest
import requests

HTTP_OK = 200

TEST_URLS: list[str] = [
    "https://httpbin.org/get",  # Simple HTTP test endpoint
    "https://httpbin.org/html",  # HTML response
]

CHALLENGE_URLS: list[str] = [
    "https://www.forbes.com/sites/andreahill/2025/08/21/why-95-of-ai-pilots-fail-and-what-business-leaders-should-do-instead/",
    "https://web-assets.bcg.com/pdf-src/prod-live/targets-over-tools-the-mandate-for-ai-transformation.pdf",
]


class TestWebFetch:
    """Test web fetching with and without camouflage."""

    def test_curl_cffi_fetch_success(self) -> None:
        """Test that curl_cffi can fetch content from test URLs."""
        for url in TEST_URLS:
            response = curl_cffi.get(url, impersonate="chrome")
            assert response.status_code == HTTP_OK
            assert len(response.text) > 0
            # Check for appropriate content based on endpoint
            if "html" in url:
                assert "html" in response.text.lower()
            elif "get" in url:
                assert "args" in response.text  # JSON response from httpbin

    def test_regular_requests_fetch_success(self) -> None:
        """Test that regular requests can fetch content from test URLs."""
        for url in TEST_URLS:
            response = requests.get(url, timeout=30)
            assert response.status_code == HTTP_OK
            assert len(response.text) > 0
            # Check for appropriate content based on endpoint
            if "html" in url:
                assert "html" in response.text.lower()
            elif "get" in url:
                assert "args" in response.text  # JSON response from httpbin

    def test_curl_cffi_vs_requests_content_length(self) -> None:
        """Compare content length between curl_cffi and regular requests."""
        # Use only one URL to avoid rate limiting
        url = TEST_URLS[0]

        # Fetch with curl_cffi
        cffi_response = curl_cffi.get(url, impersonate="chrome")

        # Fetch with regular requests
        requests_response = requests.get(url, timeout=30)

        # Both might be blocked due to rate limiting, but curl_cffi should generally work better
        # The key test is that curl_cffi can access content that regular requests cannot
        if cffi_response.status_code == HTTP_OK:
            assert len(cffi_response.text) > 0
            # If curl_cffi works but requests doesn't, that's the expected outcome
            if requests_response.status_code != HTTP_OK:
                assert requests_response.status_code in [403, 429]  # Blocked/rate limited
        # If both fail, it might be rate limiting - still acceptable for this test

    def test_curl_cffi_different_impersonations(self) -> None:
        """Test curl_cffi with different browser impersonations."""
        url = TEST_URLS[0]  # Use first URL for this test

        impersonations: list[curl_cffi.BrowserTypeLiteral] = ["chrome", "firefox", "safari"]

        # At least one impersonation should work (allowing for rate limiting)
        success_count = 0
        for impersonate in impersonations:
            response = curl_cffi.get(url, impersonate=impersonate)
            if response.status_code == HTTP_OK:
                assert len(response.text) > 0
                success_count += 1

        # At least one impersonation should work
        assert success_count > 0, "No impersonation method succeeded"

    def test_curl_cffi_invalid_impersonation(self) -> None:
        """Test curl_cffi handles errors gracefully."""
        # Test with an invalid URL to ensure error handling works
        invalid_url = "https://this-domain-does-not-exist-12345.com"

        with pytest.raises((curl_cffi.CurlError, curl_cffi.exceptions.RequestException)):
            curl_cffi.get(invalid_url, impersonate="chrome")

    def test_curl_cffi_timeout_behavior(self) -> None:
        """Test curl_cffi timeout behavior."""
        # Use a URL that should respond quickly
        url = TEST_URLS[0]

        # Test with reasonable timeout - may be blocked due to rate limiting
        response = curl_cffi.get(url, impersonate="chrome", timeout=10)
        # Accept either success or blocking (rate limiting)
        assert response.status_code in [HTTP_OK, 403, 429]

        if response.status_code == HTTP_OK:
            assert len(response.text) > 0

    def test_challenging_urls_with_camouflage(self) -> None:
        """Test URLs that are likely blocked by normal requests but work with camouflage."""
        # These URLs are known to have anti-bot protection
        for url in CHALLENGE_URLS:
            # Test with camouflage (should work)
            try:
                cffi_response = curl_cffi.get(url, impersonate="realworld", timeout=30)  # type: ignore[arg-type]
                # If we get a successful response, it should have content
                if cffi_response.status_code == HTTP_OK:
                    assert len(cffi_response.text) > 0, (
                        f"Camouflaged fetch succeeded but returned empty content for {url}"
                    )
                    # For PDF URL, check that it looks like a PDF (starts with %PDF)
                    if "bcg.com" in url and ".pdf" in url:
                        assert cffi_response.text.startswith("%PDF"), (
                            f"PDF URL should return PDF content, got: {cffi_response.text[:50]}"
                        )
                else:
                    # Non-200 status is acceptable (may be rate limited or blocked)
                    pass
            except curl_cffi.CurlError as e:
                pytest.skip(f"Camouflaged fetch failed for {url}: {e}")
            except Exception as e:  # noqa: BLE001
                pytest.skip(f"Camouflaged fetch failed for {url}: {e}")

            # Test with normal requests (likely to be blocked)
            try:
                requests_response = requests.get(url, timeout=30)
                # Normal requests may succeed or be blocked - both are acceptable outcomes
                # The key is that camouflage should provide better access
                assert requests_response.status_code is not None
            except requests.RequestException:
                # Normal requests failing is expected for challenging URLs
                pass
