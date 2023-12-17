from django.shortcuts import render, redirect, get_object_or_404
from .models import Wish
from .forms import WishForm
from .forms import WishSearchForm

def home(request):
    if request.method == 'POST':
        form = WishSearchForm(request.POST)
        if form.is_valid():
            wish_id = form.cleaned_data['wish_id']
            return redirect('view_wish', pk=wish_id)
    else:
        form = WishSearchForm()

    return render(request, 'card/home.html', {'form': form})

def card (request):
    return render(request, 'card/card.html')

def create_wish(request):
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():
            wish = form.save()
            return redirect('view_wish', pk=wish.id)
    else:
        form = WishForm()

    return render(request, 'card/create_wish.html', {'form': form})

def view_wish(request, pk):
    try:
        wish = get_object_or_404(Wish, id=pk)

        if request.method == 'POST':
            entered_password = request.POST.get('password')
            if entered_password == wish.password or entered_password == '':
                return render(request, 'card/view_wish.html', {'wish': wish, 'correct_password': True})
            else:
                return render(request, 'card/view_wish.html', {'wish': wish, 'wrong_password': True})

        return render(request, 'card/view_wish.html', {'wish': wish})

    except:
        return render(request, 'card/wish_not_found.html')