from django.db import models

class Question(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    question_text = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255, null=True, blank=True)
    option_4 = models.CharField(max_length=255, null=True, blank=True)
    correct_option = models.IntegerField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)  # ✅ keep choices

    def __str__(self):
        return f"{self.level} - {self.question_text}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.IntegerField()
    is_correct = models.BooleanField()

    def __str__(self):
        return f"Answer for {self.question.question_text} - {'Correct' if self.is_correct else 'Incorrect'}"
