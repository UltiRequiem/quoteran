"""Tests for the configurable API URL."""
import contextlib
import io
import json
import os
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from unittest import mock

from quoteran import core


class QuoteHandler(BaseHTTPRequestHandler):
    """A tiny Quotable server that remembers which paths it was asked for."""

    paths = []

    def do_GET(self):  # pylint: disable=invalid-name
        """Answer /api/random with a quote and everything else with 404."""
        QuoteHandler.paths.append(self.path)

        if self.path == "/api/random":
            body = json.dumps({"content": "Be yourself.", "author": "Someone"}).encode()
            self.send_response(200)
        elif self.path == "/broken/random":
            body = json.dumps({"message": "not a quote"}).encode()
            self.send_response(200)
        else:
            body = b"{}"
            self.send_response(404)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):  # silence the test output
        pass


class BaseUrlTests(unittest.TestCase):
    """Precedence: explicit value, environment, default."""

    def test_default(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(core.get_base_url(), core.DEFAULT_API_URL)

    def test_environment_variable(self):
        with mock.patch.dict(os.environ, {core.API_URL_ENV: "https://env.example.com/"}):
            self.assertEqual(core.get_base_url(), "https://env.example.com")

    def test_explicit_value_wins(self):
        with mock.patch.dict(os.environ, {core.API_URL_ENV: "https://env.example.com"}):
            self.assertEqual(core.get_base_url("https://x.example.com///"), "https://x.example.com")

    def test_random_quote_url(self):
        self.assertEqual(
            core.random_quote_url("https://example.com/quotes-api/"),
            "https://example.com/quotes-api/random",
        )


class ParseQuoteTests(unittest.TestCase):
    """Only well formed answers are accepted."""

    def test_valid(self):
        self.assertEqual(core.parse_quote({"content": "a", "author": "b"}), ("a", "b"))

    def test_invalid(self):
        for data in ({"content": "a"}, {"content": 1, "author": "b"}, [], None):
            with self.subTest(data=data), self.assertRaises(ValueError):
                core.parse_quote(data)


class MainTests(unittest.TestCase):
    """The command line against a real local HTTP server."""

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), QuoteHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}/api"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def setUp(self):
        QuoteHandler.paths = []

    def run_main(self, argv, env=None):
        """Run main(), returning (stdout, stderr, exit code)."""
        out, err = io.StringIO(), io.StringIO()
        code = 0

        with mock.patch.dict(os.environ, env or {}, clear=True), contextlib.redirect_stdout(
            out
        ), contextlib.redirect_stderr(err):
            try:
                core.main(argv)
            except SystemExit as exit_info:
                code = exit_info.code

        return out.getvalue(), err.getvalue(), code

    def test_flag(self):
        out, _, code = self.run_main(["--api-url", self.url])

        self.assertEqual(code, 0)
        self.assertIn("Be yourself.", out)
        self.assertIn("Someone", out)
        self.assertEqual(QuoteHandler.paths, ["/api/random"])

    def test_environment_variable(self):
        out, _, code = self.run_main([], {core.API_URL_ENV: self.url + "/"})

        self.assertEqual(code, 0)
        self.assertIn("Be yourself.", out)

    def test_flag_beats_environment(self):
        unreachable = {core.API_URL_ENV: "http://127.0.0.1:1"}
        _, _, code = self.run_main(["--api-url", self.url], unreachable)

        self.assertEqual(code, 0)

    def test_unreachable_server_exits_with_a_hint(self):
        _, err, code = self.run_main(["--api-url", "http://127.0.0.1:1"])

        self.assertEqual(code, 1)
        self.assertIn("Could not get a quote from http://127.0.0.1:1", err)
        self.assertIn(core.API_URL_ENV, err)

    def test_http_error_exits(self):
        _, _, code = self.run_main(["--api-url", self.url + "/missing"])

        self.assertEqual(code, 1)

    def test_malformed_answer_exits(self):
        base = self.url.replace("/api", "/broken")
        _, err, code = self.run_main(["--api-url", base])

        self.assertEqual(code, 1)
        self.assertIn("Unexpected answer", err)

    def test_version(self):
        out, _, code = self.run_main(["--version"])

        self.assertEqual(code, 0)
        self.assertIn(core.__version__, out)


if __name__ == "__main__":
    unittest.main()
