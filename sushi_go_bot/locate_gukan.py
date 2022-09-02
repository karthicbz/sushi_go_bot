import pyautogui

receipe_images = ['rice.png', 'nori.png', 'fish_egg.png']
order_list = []
def locate_orders():
    for image in receipe_images:
        gukan_list = list(pyautogui.locateAllOnScreen(image))
        for _ in range(len(gukan_list)):
            order_list.append(image.replace('.png', ''))

    return order_list
    # coordinates = pyautogui.locateOnScreen('gukan.png', confidence=0.9)
    # return coordinates

print(locate_orders())
