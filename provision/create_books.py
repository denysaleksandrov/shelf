#!/usr/bin/env python3
import json
import string
import base64
import requests

URL = "http://127.0.0.1:8000/api/bookshelf?format=json"

HEADERS = {
    'content-type': "application/json",
}

def get_image(name):
    with open('book_images/{}'.format(name), "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode()

BOOKS = [
         {'book': {'title': 'The Eye of the World', 
                   'author': 'Robert Jordan', 
                   'publishdate': '1990-01-15',
                   'description': '''The Eye of the World is a fantasy novel by
                   American writer Robert Jordan, the first book of The Wheel of
                   Time series. ''',
                   'cover': get_image('WoT01_TheEyeOfTheWorld.jpg')
                   }
          },
         {'book': {'title': 'The Great Hunt', 
                   'author': 'Robert Jordan', 
                   'publishdate': '1990-11-15',
                   'description': '''The Great Hunt is a fantasy novel by
                   American author Robert Jordan, the second book of The Wheel
                   of Time series.''',
                   'cover': get_image('WoT02_TheGreatHunt.jpg')
                   }
          },
         {'book': {'title': 'The Dragon Reborn', 
                   'author': 'Robert Jordan', 
                   'publishdate': '1991-09-15',
                   'description': '''The Dragon Reborn is a fantasy novel by
                   American writer Robert Jordan, the third in his series The
                   Wheel of Time.''',
                   'cover': get_image('WoT03_TheDragonReborn.jpg')
                   }
          },
         {'book': {'title': 'The Shadow Rising', 
                   'author': 'Robert Jordan', 
                   'publishdate': '1992-09-15',
                   'description': '''The Shadow Rising is a fantasy novel by
                   American author Robert Jordan, the fourth book in his series
                   The Wheel of Time.''',
                   'cover': get_image('WoT04_TheShadowRising.jpg')
                   }
          },
         {'book': {'title': 'The Fires of Heaven', 
                   'author': 'Robert Jordan', 
                   'publishdate': '1993-10-15',
                   'description': '''The Fires of Heaven is a fantasy novel by
                   American writer Robert Jordan, the fifth book in his series
                   The Wheel of Time.''',
                   'cover': get_image('WoT05_TheFiresOfHeaven.jpg')
                   }
          },
         {'book': {'title': 'Lord of Chaos', 
                   'author': 'Robert Jordan', 
                   'publishdate': '1994-10-15',
                   'description': '''Lord of Chaos is a fantasy novel by
                   American author Robert Jordan, the sixth book of his series
                   The Wheel of Time.''',
                   'cover': get_image('WoT06_LordOfChaos.jpg')
                   }
          },
         {'book': {'title': 'A Crown of Swords', 
                   'author': 'Robert Jordan', 
                   'publishdate': '1996-05-15',
                   'description': '''A Crown of Swords is a fantasy novel by
                   American author Robert Jordan, the seventh book of The Wheel
                   of Time.''',
                   'cover': get_image('WoT07_ACrownOfSwords.jpg')
                   }
          },
         {'book': {'title': 'The Path of Daggers', 
                   'author': 'Robert Jordan', 
                   'publishdate': '1998-10-20',
                   'description': '''The Path of Daggers is a fantasy novel by
                   American author Robert Jordan, the eighth book of his series
                   The Wheel of Time.''',
                   'cover': get_image('WoT08_ThePathOfDaggers.jpg')
                   }
          },
         {'book': {'title': 'Winter\'s Heart', 
                   'author': 'Robert Jordan', 
                   'publishdate': '2000-11-07',
                   'description': '''Winter\'s Heart a fantasy novel by American
                   author Robert Jordan, the ninth book of his series Wheel of
                   Time.''',
                   'cover': get_image('WoT09_WintersHeart.jpg')
                   }
          },
         {'book': {'title': 'Crossroads of Twilight', 
                   'author': 'Robert Jordan', 
                   'publishdate': '2003-01-07',
                   'description': '''Crossroads of Twilight is a fantasy novel
                   by American author Robert Jordan, the tenth book of his The
                   Wheel of Time series.''',
                   'cover': get_image('WoT10_CrossroadsOfTwilight.jpg')
                   }
          },
         {'book': {'title': 'Knife of Dreams', 
                   'author': 'Robert Jordan', 
                   'publishdate': '2005-10-11',
                   'description': '''Knife of Dreams is a fantasy novel by
                   American author Robert Jordan, the eleventh book in his
                   series The Wheel of Time.''',
                   'cover': get_image('WoT11_KnifeOfDreams.jpg')
                   }
          },
         {'book': {'title': 'The Gathering Storm', 
                   'author': 'Robert Jordan and Brandon Sanderson', 
                   'publishdate': '2009-10-27',
                   'description': '''The Gathering Storm is a fantasy novel by
                   American writers Robert Jordan and Brandon Sanderson, the
                   twelfth book in the series The Wheel of Time.''',
                   'cover': get_image('TheGatheringStormUSCover.jpg')
                   }
          },
         {'book': {'title': 'Towers of Midnight', 
                   'author': 'Robert Jordan and Brandon Sanderson', 
                   'publishdate': '2010-11-02',
                   'description': '''Towers of Midnight by Robert Jordan and
                   Brandon Sanderson, is the sequel to the novel The Gathering
                   Storm,[4] and the 13th book in the Wheel of Time series.
                   ''',
                   'cover': get_image('Towers_of_Midnight_hardcover.jpg')
                   }
          },
         {'book': {'title': 'A Memory of Light', 
                   'author': 'Robert Jordan and Brandon Sanderson', 
                   'publishdate': '2013-04-08',
                   'description': '''A Memory of Light is the 14th and final
                   book of the fantasy series The Wheel of Time, written by
                   American authors Robert Jordan and Brandon Sanderson.''',
                   'cover': get_image('A_Memory_of_Light_cover.jpg')
                   }
          }
]

def get_titles():
    response = requests.get(URL, headers=HEADERS)
    titles = [ book.get('title', None) for book in response.json()['books']]
    return titles

TITLES = get_titles()

for book in BOOKS:
    if book.get('book').get('title') not in TITLES:
        response = requests.post(URL, data=json.dumps(book), headers=HEADERS)
        print(response.text)
