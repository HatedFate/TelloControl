import keyboard


def pressed_keys(key_name):
    ans = False
    if keyboard.is_pressed(key_name):
        ans = True
    return ans


def main():
    print(pressed_keys("a"))


if __name__ == '__main__':
    while True:
        main()
