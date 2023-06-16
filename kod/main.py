from app import App


def main():
    frame = App()
    try:
        frame.run()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
