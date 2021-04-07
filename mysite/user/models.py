from django.db import models



BEGINNER = 'BEG'
    INTERMEDIATE = 'INT'
    ADVANCED = 'ADV'
    NEW_PLAYER = 'NEW'
    GUITAR_PLAYING_LEVEL = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
        (NEW_PLAYER, 'New Player')
    ]
