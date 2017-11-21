"""
Data Master will hold an instance for the class

-An instance of the Information Expert GRASP Principle
-Also uses an Interface Pattern
-Interface Pattern uses the Publisher Pattern to Spread it.
-Feeds information to the Initializer, which is a Pattern Instance of Singleton

"""
import person


class DataMaster:

    item_synonym = ['sword', 'sigil', 'dagger']
    person_object_synonym = person.personList
    setpiece_synonym = ['dragon', 'buildings', 'inn' ]
    dateable_synonym = ['date1', 'date 2', 'date 3']
    object_synonyms = [person_object_synonym]
    # LocationRegistry():
    #
    # ItemRegistry():
    #
    # PlaceRegistry():
    #
    # DateRegistry():
