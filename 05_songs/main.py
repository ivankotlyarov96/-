violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


duration_song = 0

count_song = int(input('Сколько песен выбрать? '))
for i in range(count_song):
    titl_song = input(f'Название {i + 1} -й песни: ')
    for i in violator_songs:
        if i[0] == titl_song:
            duration_song += i[1]


print('Общее время звучания песен: ', round(duration_song, 2))
# TODO здесь писать код
