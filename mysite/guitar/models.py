from django.db import models


class Chord(models.Model):
    EASY = 'EASY'
    HARD = 'HARD'
    MEDIUM = 'MEDIUM'
    CHORD_LEVEL = [
        (EASY, 'Easy'),
        (HARD, 'Hard'),
        (MEDIUM, 'Medium')
    ]
    level = models.CharField(max_length=6, choices=CHORD_LEVEL)
    name = models.CharField(max_length=15)
    chord_image = models.ImageField(upload_to='chords_pics')

    def __str__(self):
        return self.name
