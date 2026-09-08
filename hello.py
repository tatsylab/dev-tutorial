"""Small program used in the Tatsy Lab development environment tutorial."""


def repeat_message(message: str, count: int) -> str:
    """Return a message repeated on separate lines."""
    if count < 1:
        raise ValueError("count must be at least 1")
    return "\n".join(message for _ in range(count))


def main() -> None:
    message = "Hello from the Tatsy Lab development environment!"
    print(repeat_message(message, 2))


if __name__ == "__main__":
    main()
