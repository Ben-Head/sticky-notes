from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages

def post_list(request):
    # Retrieve all posts from the database
    posts = Post.objects.all()
    # Render the list of posts using the post_list.html template
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # Retrieve a specific post from the database based on its primary key (pk)
    post = get_object_or_404(Post, pk=pk)
    # Render the detailed view of the post using the post_detail.html template
    return render(request, 'posts/post_detail.html', {'post': post})

@login_required
def my_posts(request):
    # Retrieve posts authored by the currently logged-in user
    posts = Post.objects.filter(author=request.user)
    # Render the list of the user's posts using the my_posts.html template
    return render(request, 'posts/my_posts.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the new post to the database
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    # Render the post creation form using the post_form.html template
    return render(request, 'posts/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    # Retrieve the post to be updated
    post = get_object_or_404(Post, pk=pk)
    # Check if the user is the author of the post or a superuser
    if post.author != request.user and not request.user.is_superuser:
        return redirect('post_list')
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # Save the updated post to the database
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    # Render the post update form using the post_form.html template
    return render(request, 'posts/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    # Retrieve the post to be deleted
    post = get_object_or_404(Post, pk=pk)
    # Check if the user is the author of the post or a superuser
    if post.author != request.user and not request.user.is_superuser:
        return redirect('post_list')
    if request.method == 'POST':
        # Delete the post from the database
        post.delete()
        return redirect('post_list')
    # Render the confirmation page for post deletion using the post_confirm_delete.html template
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # Log in the new user
            login(request, new_user)
            return redirect('post_list')
    else:
        form = UserRegistrationForm()
    # Render the user registration form using the register.html template
    return render(request, 'posts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log in the user
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    # Render the login form using the login.html template
    return render(request, 'posts/login.html', {'form': form})

def about(request):
    # Render the about page using the about.html template
    return render(request, 'about.html')

def privacy_policy(request):
    # Render the privacy policy page using the privacy-policy.html template
    return render(request, 'privacy-policy.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Send an email notification
        send_mail(
            f"Contact Form Submission from {name}",
            message,
            email,
            ['admin@stickynotes.com'],
            fail_silently=False,
        )
        
        # Display a success message and redirect back to the contact page
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly.')
        return redirect('contact')
    
    # Render the contact form using the contact.html template
    return render(request, 'contact.html')
