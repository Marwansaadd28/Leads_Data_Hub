from extract import extract


def main():
    rows = extract()

    print(f"\nTotal rows extracted: {len(rows)}")


if __name__ == "__main__":
    main()