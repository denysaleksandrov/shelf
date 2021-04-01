#!/usr/bin/env python3
import os
import json
import string
import base64
import requests

IP = os.getenv('APP_IP', '127.0.0.1')
PORT = os.getenv('APP_PORT', '8010')
URL = "http://{ip}:{port}/api/bookshelf?format=json".format(ip=IP, port=PORT)

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
          },
         {'book': {'title': 'The Dark Tower: The Gunslinger',
                   'author': 'Stephen King',
                   'publishdate': '1982-06-10',
                   'description': '''The Gunslinger is a novel by American
                   author Stephen King, the first volume in the Dark Tower
                   series he describes as his magnum opus.''',
                   'cover': get_image('The_Gunslinger.jpg')
                   }
         
          },
         {'book': {'title': 'The Dark Tower II: The Drawing of the Three',
                   'author': 'Stephen King',
                   'publishdate': '1983-05-01',
                   'description': '''The Drawing of the Three is a fantasy novel
                   by American writer Stephen King, the second book in The Dark
                   Tower series, published by Grant in 1987.''',
                   'cover': get_image('The_Drawing_of_the_Three.jpg')
                   }
         
          },
         {'book': {'title': 'The Dark Tower III: The Waste Lands',
                   'author': 'Stephen King',
                   'publishdate': '1991-08-01',
                   'description': '''The Waste Lands (subtitled "Redemption") is
                   a fantasy novel by American writer Stephen King, the third
                   book of The Dark Tower series.''',
                   'cover': get_image('The_Waste_Lands.jpg')
                   }
         
          },
         {'book': {'title': 'The Dark Tower IV: Wizard and Glass',
                   'author': 'Stephen King',
                   'publishdate': '1997-11-04',
                   'description': '''Wizard and Glass is a fantasy novel by
                   American writer Stephen King, the fourth book in The Dark
                   Tower series, published in 1997. Subtitled "Regard", it
                   placed fourth in the annual Locus Poll for best fantasy
                   novel.''',
                   'cover': get_image('Wizard_and_Glass.jpg')
                   }
         
          },
         {'book': {'title': 'The Dark Tower V: Wolves of the Calla',
                   'author': 'Stephen King',
                   'publishdate': '2003-11-04',
                   'description': '''Wolves of the Calla is the fifth novel in
                   Stephen King's The Dark Tower series. This book continues the
                   story of Roland Deschain, Eddie Dean, Susannah Dean, Jake
                   Chambers, and Oy as they make their way toward the Dark
                   Tower.''',
                   'cover': get_image('Wolvescalla.jpg')
                   }
         
          },
         {'book': {'title': 'The Dark Tower VI: Song of Susannah',
                   'author': 'Stephen King',
                   'publishdate': '2004-07-08',
                   'description': '''Song of Susannah is a fantasy novel by
                   American writer Stephen King, the sixth in his Dark Tower
                   series.''',
                   'cover': get_image('Song_of_Susannah.jpg')
                   }
         
          },
         {'book': {'title': 'The Dark Tower VII: The Dark Tower',
                   'author': 'Stephen King',
                   'publishdate': '2004-09-21',
                   'description': '''The Dark Tower is the seventh novel in
                   Stephen King's Dark Tower series, published by Grant on
                   September 21, 2004 (King's birthday), and illustrated by
                   Michael Whelan. It has four subtitles: REPRODUCTION,
                   REVELATION, REDEMPTION, and RESUMPTION – all but the second
                   of these having been used as subtitles for previous novels in
                   the series.''',
                   'cover': get_image('Thedarktower7.jpg')
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
