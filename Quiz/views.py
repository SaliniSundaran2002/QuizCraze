from django.shortcuts import render
from .models import Question

def home(request):
    context = {
        'background': 'linear-gradient(135deg, #6e7dff, #3e5ef5)'  # Example background
    }
    return render(request, 'Quiz/home.html', context)
def quiz(request, level, level_number):
    level_map = {
        'beginner': 1,
        'intermediate': 2,
        'advanced': 3
    }

    start = (level_number - 1) * 5
    end = level_number * 5
    questions = Question.objects.filter(level=level)[start:end]

    # Background logic...
    background = ""
    if level == 'beginner':
        background = "url('path_to_beginner_bg')"
    elif level == 'intermediate':
        background = "url('path_to_intermediate_bg')"
    elif level == 'advanced':
        background = "url('path_to_advanced_bg')"

    return render(request, 'Quiz/quiz.html', {
        'questions': questions,
        'background': background,
        'level': level,
        'level_number': level_number,
    })


def result(request, level, level_number):
    if request.method == 'POST':
        correct_answers = []

        # Get all questions for the specific level and order them
        questions = Question.objects.filter(level=level).order_by('id')

        # Get the first and last question in the entire queryset before slicing
        first_question = questions.first()
        last_question = questions.last()

        # Pagination logic (5 questions per level)
        start = (level_number - 1) * 5
        end = level_number * 5
        questions = questions[start:end]  # Slice the queryset after pagination

        score = 0
        total = len(questions)

        # Check the answers for each question
        for i, question in enumerate(questions):
            user_answer = request.POST.get(f'q{i}')
            if user_answer and int(user_answer) == question.correct_option:
                score += 1
            correct_answers.append({
                'question': question.question_text,
                'correct_answer': question.correct_option
            })

        # Logic to get the next question ID
        # Calculate the next question ID based on the last question in the entire level's queryset
        next_question_id = None
        if last_question:
            next_level_number = level_number + 1 if score == total and level_number < 3 else None


        return render(request, 'Quiz/result.html', {
            'score': score,
            'total': total,
            'correct_answers': correct_answers,
            'level': level,
            'level_number': level_number,
            'next_level_number': next_level_number,
    })


    return render(request, 'Quiz/result.html', {'score': 0, 'total': 0})
