from django.shortcuts import render


'''Html views'''


''' Homeview'''
def home_view(request):
    return render(request,'home.html')

''' Register View'''
def register_view(request):
    return render(request,'register.html')

'''Login View'''
def login_view(request):
    return render(request,'login.html')



''' SurveyView'''
def survey_view(request):
    return render(request, 'survey.html')


''' QuestionsView'''
def questions_view(request):
    return render(request, 'questions.html')


''' QuestionView'''
def question_view(request):
    return render(request, 'question.html')


