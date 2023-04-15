import media
import fresh_tomatoes
#import openlink
ek_tha_tiger = media.Movie("Ek Tha Tiger",
                           "A Love story of Spy",
                           "file://C:\Users\Lenovo\Desktop\PythonPrograms\ekthatiger.jpg","https://www.youtube.com/watch?v=ePO5M5DE01I")
star_wars = media.Movie("Star Wars",
                           "The Last Jedi",
                           "file://C:\Users\Lenovo\Desktop\PythonPrograms\starwarsjpg",
                           "https://www.youtube.com/watch?v=Q0CbN8sfihY")

bahubali2 = media.Movie("Bahubali-2",
                           "The Beginning",
                           "file://C:\Users\Lenovo\Desktop\PythonPrograms\bahubali.jpg",
                           "https://www.youtube.com/watch?v=G62HrubdD6o")

print(ek_tha_tiger.storyline)
print(star_wars.storyline)
print(bahubali2.storyline)
#ek_tha_tiger.show_trailer()
movies = [ek_tha_tiger, star_wars, bahubali2]
web.open_movies_page(movies)
