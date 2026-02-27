from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Note


def home(request):
    query = request.GET.get('q', '')
    notes = Note.objects.all()
    if query:
        notes = notes.filter(title__icontains=query) | notes.filter(content__icontains=query)
    return render(request, 'notes/home.html', {'notes': notes, 'query': query})


def about(request):
    return render(request, 'notes/about.html')


def help_page(request):
    return render(request, 'notes/help.html')


def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        if not title or not content:
            messages.error(request, 'Please fill in all fields.')
            return redirect('home')

        Note.objects.create(title=title, content=content)
        messages.success(request, f'Note "{title}" created successfully!')
        return redirect('home')

    return redirect('home')


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        if not title or not content:
            messages.error(request, 'Please fill in all fields.')
            return redirect('edit_note', pk=pk)

        note.title = title
        note.content = content
        note.save()
        messages.success(request, f'Note "{title}" updated successfully!')
        return redirect('home')

    return render(request, 'notes/edit_note.html', {'note': note})


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        title = note.title
        note.delete()
        messages.success(request, f'Note "{title}" deleted.')
    return redirect('home')
