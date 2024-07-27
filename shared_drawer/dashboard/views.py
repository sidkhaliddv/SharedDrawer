from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def index(request):
  context = {
    'items_count': request.user.item_set.count()
  }
  return render(request, 'dashboard/index.html', context)
