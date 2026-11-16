"""Greeting package for community."""


def greet(name: str) -> str:
    name = name.strip() or "world"
    return f"Hello, {name}!"

