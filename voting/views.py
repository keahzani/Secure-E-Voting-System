from django.shortcuts import render, redirect, get_object_or_404
from .models import Vote
from elections.models import Election, Candidate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.decorators import voter_required
from django.utils import timezone
from .forms import VoteForm



@login_required
def cast_vote(request, election_id):
    election = get_object_or_404(Election, id=election_id)
    candidates = election.candidates.all()

    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        candidate = get_object_or_404(Candidate, id=candidate_id)

        # Check if already voted
        if Vote.objects.filter(voter=request.user, election=election).exists():
            messages.error(request, "You have already voted in this election.")
            return redirect('election_list')

        Vote.objects.create(voter=request.user, election=election, candidate=candidate)
        messages.success(request, "Your vote has been successfully cast!")
        return redirect('election_list')

    return render(request, 'voting/cast_vote.html', {'election': election, 'candidates': candidates})

@login_required
def election_results(request, election_id):
    election = get_object_or_404(Election, id=election_id)
    candidates = election.candidates.all()

    results = {}
    for candidate in candidates:
        votes = Vote.objects.filter(candidate=candidate).count()
        results[candidate.name] = votes

    return render(request, 'voting/election_results.html', {'election': election, 'results': results})

@voter_required
def cast_vote(request):
    return render(request, 'voting/cast_vote.html')

@login_required
def vote_view(request, election_id):
    print("✅ vote_view was reached.")
    print("User:", request.user.username)
    print("Has profile:", hasattr(request.user, 'profile'))
    if hasattr(request.user, 'profile'):
        print("Role:", request.user.profile.role)
    
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'voter':
        messages.error(request, "You are not authorized to vote.")
        return redirect('home')
    
    election = get_object_or_404(Election, pk=election_id)

    if not election.start_date <= timezone.now() <= election.end_date:
        messages.error(request, "Voting is closed for this election.")
        return redirect('home')

    if Vote.objects.filter(voter=request.user, election=election).exists():
        messages.warning(request, "You have already voted in this election.")
        return redirect('home')

    if request.method == 'POST':
        form = VoteForm(request.POST, election=election)
        if form.is_valid():
            selected_candidate = form.cleaned_data['candidate']

            # Store vote without encryption for now
            Vote.objects.create(
                voter=request.user,
                election=election,
                candidate=selected_candidate,
                encrypted_data=str(selected_candidate.id),  # plain storage
            )

            messages.success(request, "Your vote has been submitted.")
            return redirect('home')
    else:
        form = VoteForm(election=election)

    return render(request, 'voting/vote.html', {'form': form, 'election': election})

@login_required
def results_view(request, election_id):
    election = get_object_or_404(Election, pk=election_id)

     # Prevent viewing if election hasn't ended yet
    if timezone.now() < election.end_date:
        return HttpResponseForbidden("Results will be available after the election ends.")

    # Ensure results are only visible after the election ends
    if timezone.now() < election.end_date:
        messages.error(request, "Results are not available yet.")
        return redirect('home')

    # Count votes per candidate
    results = Vote.objects.filter(election=election) \
        .values('candidate__name') \
        .annotate(vote_count=Count('candidate')) \
        .order_by('-vote_count')

    context = {
        'election': election,
        'results': results
    }
    return render(request, 'voting/results.html', context)

