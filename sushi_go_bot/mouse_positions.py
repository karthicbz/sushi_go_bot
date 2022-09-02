class MousePositions:
    def start_game_positions(self):
        positions = [
        {'mouse_x':332, 'mouse_y':595, 'clicks':1, 'button':'left'},
        {'mouse_x':327, 'mouse_y':786, 'clicks':1, 'button':'left'},
        {'mouse_x':331, 'mouse_y':797, 'clicks':1, 'button':'left'},
        {'mouse_x':607, 'mouse_y':850, 'clicks':1, 'button':'left'},
        {'mouse_x':338, 'mouse_y':775, 'clicks':1, 'button':'left'},
        ]
        return positions

    def tutorial_positions(self):
        positions = [
        {'mouse_x':514, 'mouse_y':784, 'clicks':1, 'button':'left'},
        {'mouse_x':345, 'mouse_y':835, 'clicks':1, 'button':'left'},
        {'mouse_x':112, 'mouse_y':732, 'clicks':1, 'button':'left'},
        {'mouse_x':109, 'mouse_y':783, 'clicks':1, 'button':'left'},
        {'mouse_x':55, 'mouse_y':777, 'clicks':1, 'button':'left'},
        {'mouse_x':207, 'mouse_y':779, 'clicks':1, 'button':'left'},
        {'mouse_x':201, 'mouse_y':599, 'clicks':1, 'button':'left'},
        {'mouse_x':334, 'mouse_y':804, 'clicks':1, 'button':'left'},
        ]
        return positions

    def plate_positions(self):
        positions = [
            {'mouse_x':98, 'mouse_y':601, 'clicks':1, 'button':'left'},
            {'mouse_x':189, 'mouse_y':601, 'clicks':1, 'button':'left'},
            {'mouse_x':300, 'mouse_y':601, 'clicks':1, 'button':'left'},
            {'mouse_x':400, 'mouse_y':601, 'clicks':1, 'button':'left'},
            {'mouse_x':501, 'mouse_y':601, 'clicks':1, 'button':'left'},
            {'mouse_x':598, 'mouse_y':601, 'clicks':1, 'button':'left'},
        ]
        return positions

    def receipe_images(self):
        return ['gukan_maki1.png', 'california_roll1.png', 'onigiri1.png']

    def restock_item_images(self):
        restock_items = []
        for i in range(0, 5):
            restock_items.append(f'nori{i}.png')
            restock_items.append(f'fish_egg{i}.png')
            restock_items.append(f'rice{i}.png')
        return restock_items

    def receipe_positions(self, receipe):
        onigiri = [
            {'mouse_x':112, 'mouse_y':732, 'clicks':1, 'button':'left'},
            {'mouse_x':112, 'mouse_y':732, 'clicks':1, 'button':'left'},
            {'mouse_x':55, 'mouse_y':777, 'clicks':1, 'button':'left'},
        ]

        california_roll = [
            {'mouse_x':112, 'mouse_y':732, 'clicks':1, 'button':'left'},
            {'mouse_x':109, 'mouse_y':783, 'clicks':1, 'button':'left'},
            {'mouse_x':55, 'mouse_y':777, 'clicks':1, 'button':'left'},
        ]

        gukan_maki = [
            {'mouse_x':112, 'mouse_y':732, 'clicks':1, 'button':'left'},
            {'mouse_x':55, 'mouse_y':777, 'clicks':1, 'button':'left'},
            {'mouse_x':109, 'mouse_y':783, 'clicks':1, 'button':'left'},
            {'mouse_x':109, 'mouse_y':783, 'clicks':1, 'button':'left'},
        ]

        if receipe == 'onigiri':
            return onigiri
        elif receipe == 'california_roll':
            return california_roll
        elif receipe == 'gukan_maki':
            return gukan_maki

    def receipe_order_positions(self, items_to_restock):
        nori = [
            {'mouse_x':602, 'mouse_y':751, 'clicks':1, 'button':'left'},
            {'mouse_x':553, 'mouse_y':668, 'clicks':1, 'button':'left'},
            {'mouse_x':512, 'mouse_y':675, 'clicks':1, 'button':'left'},
            {'mouse_x':500, 'mouse_y':687, 'clicks':1, 'button':'left'},
        ]

        fish_egg = [
            {'mouse_x':602, 'mouse_y':751, 'clicks':1, 'button':'left'},
            {'mouse_x':553, 'mouse_y':668, 'clicks':1, 'button':'left'},
            {'mouse_x':592, 'mouse_y':668, 'clicks':1, 'button':'left'},
            {'mouse_x':500, 'mouse_y':687, 'clicks':1, 'button':'left'},
        ]

        rice = [
            {'mouse_x':602, 'mouse_y':751, 'clicks':1, 'button':'left'},
            {'mouse_x':550, 'mouse_y':688, 'clicks':1, 'button':'left'},
            {'mouse_x':557, 'mouse_y':679, 'clicks':1, 'button':'left'},
            {'mouse_x':500, 'mouse_y':687, 'clicks':1, 'button':'left'},
        ]

        if items_to_restock == 'nori':
            return nori
        elif items_to_restock == 'fish_egg':
            return fish_egg
        elif items_to_restock == 'rice':
            return rice
