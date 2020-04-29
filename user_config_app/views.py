from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EditUserForm, ResetPWForm


@login_required
def index(req):
    user = User.objects.get(username=req.user)
    if req.method == 'POST':
        form = EditUserForm(req.POST, instance=req.user)
        if form.is_valid():
            form.save()
            messages.success(req, "Breytingarnar hafa verið vistaðar!")
            return redirect('profile')
        else:
            print("something went wrong!")
    else:
        form = EditUserForm(initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            })
    return render(req, 'profile.html', {'form': form})


# @login_required
# def reset(req):
#     print("I'm gonna reset your pw!!!")
#     user = User.objects.get(username=req.user)
#     if req.method == 'POST':
#         form = ResetPWForm(user=req.user)
#         if form.is_valid():
#             old_pw = form.cleaned_data['old_password']
#             pw1 = form.cleaned_data['password1']
#             pw2 = form.cleaned_data['password2']
#             user = User.objects.get(username=req.user)
#             print("After: " + user.password)
#             print(user.check_password(old_pw))
#             if user.check_password(old_pw) and \
#                     pw1 == pw2:
#                 # user.set_password(pw1)
#                 form.save()
#                 messages.success(req, "Framkvæmdin tókst!")
#             else:
#                 messages.error(req, "Villa! Reyndu aftur")
#             return redirect('pw-reset')
#     else:
#         print("First: " + User.objects.get(username=req.user).password)
#         form = ResetPWForm(user=req.user)
#     return render(req, 'pw_reset.html', {'form': form})
