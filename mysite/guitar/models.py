from django.db import models


class Chord(models.Model):
    EASY = 'EASY'
    MEDIUM = 'MEDIUM'
    HARD = 'HARD'
    CHORD_LEVEL = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard')
    ]
    level = models.CharField(max_length=6, choices=CHORD_LEVEL)
    name = models.CharField(max_length=15)
    chord_image = models.ImageField(upload_to='chords_pics')

    def __str__(self):
        return self.name
