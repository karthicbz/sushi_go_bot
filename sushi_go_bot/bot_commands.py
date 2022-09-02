import time
import pyautogui
from mouse_positions import MousePositions
import re


class BotCommands(MousePositions):
    def __init__(self):
        super().__init__()

    #Click_engine method is used to click a item in exact position
    #Basically we are going to generate lots of clicks so i created this method specifically for that
    def click_engine(self, positions, waiting_time=0):
        click_position = positions
        for position in click_position:
            pyautogui.click(x=position.get('mouse_x'), y=position.get('mouse_y'), clicks=position.get('clicks'), button=position.get('button'))
            time.sleep(waiting_time)


    #This method is used to pass into tutorial section
    #This method is used to click initial start game buttons and its next buttons
    def pass_through_game(self, start_game_positions, waiting_time):
        self.click_engine(start_game_positions, waiting_time)
        print('Entered into game')


    #This method is used to complete the tutorial
    def pass_tutorial(self, tutorial_positions):
        time.sleep(5)
        for value in range(0,len(tutorial_positions)-2):
            position = tutorial_positions[value]
            pyautogui.click(x=position.get('mouse_x'), y=position.get('mouse_y'), clicks=position.get('clicks'), button=position.get('button'))
        for value in range(6, 8):
            time.sleep(12)
            position = tutorial_positions[value]
            pyautogui.click(x=position.get('mouse_x'), y=position.get('mouse_y'), clicks=position.get('clicks'), button=position.get('button'))
        print('Completed tutorial successfully')

    #This method is used to click plates after game characters 
    # finished eating
    def clear_plates(self, plate_positions):
        print('Clearing Plates')
        self.click_engine(plate_positions)

    #This method is used to make a receipes for game characters
    def prepare_recipes(self, receipes):
        print(f'orders:{receipes}')
        for receipe in receipes:
            self.click_engine(super().receipe_positions(receipe))
            pyautogui.click(x=207, y=779, clicks=1, button='left')
            time.sleep(3)

    def locate_items(self, item_images):
        item_list = []
        for image in item_images:
            receipe = list(pyautogui.locateAllOnScreen(image))
            for _ in range(len(receipe)):
                # item_list.append(image.replace('.png', ''))
                item_list.append(re.sub('[0-9].png', '', image))
        # print(f'orders: {order_list}')
        return item_list

    def locate_orders(self, receipe_images):
        # order_list = []
        # for image in receipe_images:
        #     receipe = list(pyautogui.locateAllOnScreen(image))
        #     for _ in range(len(receipe)):
        #         order_list.append(image.replace('.png', ''))
        # print(f'orders: {order_list}')
        # return order_list
        return self.locate_items(receipe_images)

    def locate_low_items(self, low_item_images):
        return self.locate_items(low_item_images)

    def restocking_items(self, restockable_items):
        for item in restockable_items:
            print(f'restocking {item}')
            self.click_engine(super().receipe_order_positions(item))


bot = BotCommands()
mouse_positions = MousePositions()
bot.pass_through_game(bot.start_game_positions(), 1)
# i = 5
while True:
# bot.pass_tutorial(bot.tutorial_positions())
    # bot.clear_plates(mouse_positions.plate_positions())
    time.sleep(5)
    # bot.locate_orders(mouse_positions.receipe_images)
    bot.prepare_recipes(bot.locate_orders(mouse_positions.receipe_images()))
    time.sleep(5)
    bot.clear_plates(mouse_positions.plate_positions())
    bot.restocking_items(bot.locate_low_items(mouse_positions.restock_item_images()))
    # i -= 1

