from django.shortcuts import render, redirect
from .models import UserScore
from .forms import UserScoreForm

# Create your views here.

def leaderboard(request):
    users = UserScore.objects.all()
    return render(request, 'leaderboard.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = UserScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leaderboard')
    else:
        form = UserScoreForm()
    return render(request, 'add_user.html', {'form': form})

def delete_user(request, user_id):
    user = UserScore.objects.get(id=user_id)
    user.delete()
    return redirect('leaderboard')
