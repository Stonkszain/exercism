def convert(number):
    rain_sound = ''
    if number % 3 == 0:
        rain_sound = rain_sound + 'Pling'
    if number % 5 == 0:
        rain_sound = rain_sound + 'Plang'
    if number % 7 == 0:
        rain_sound = rain_sound + 'Plong'
    if rain_sound == '':
        return str(number)
    return rain_sound
    # pass
