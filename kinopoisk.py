from kinopoisk_api import KP
import random
import config

kinopoisk = KP(token=config.kpoisk)


def get_cinema(genre):
    search_result = kinopoisk.search(genre)
    if genre == 'Аниме':
        x = random.randrange(0, 4)
        list1 = ['Название: ' + search_result[x].ru_name +
                 '\nГод: ' + search_result[x].year +
                 '\nРейтинг: ' + search_result[x].kp_rate +
                 '\nСсылка на Кинопоиск: ' + search_result[x].kp_url +
                 '\nДлительность: ' + search_result[x].duration +
                 '\nСсылка на постер' + search_result[x].poster_preview]
        return list1
    else:
        x = random.randrange(0, 6)
        list2 = ['Название: ' + search_result[x].ru_name +
                 '\nГод: ' + search_result[x].year +
                 '\nРейтинг: ' + search_result[x].kp_rate +
                 '\nСсылка на Кинопоиск: ' + search_result[x].kp_url +
                 '\nДлительность: ' + search_result[x].duration +
                 '\nСсылка на постер' + search_result[x].poster_preview]
        return list2
