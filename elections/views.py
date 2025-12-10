from django.shortcuts import render
from .models import Election
from users.decorators import admin_required, election_officer_required
from users.decorators import admin_or_officer_required

def election_list(request):
    elections = Election.objects.all()
    return render(request, 'elections/election_list.html', {'elections': elections})

@admin_required
def create_election(request):
    return render(request, 'elections/create_election.html')

@election_officer_required
def manage_candidates(request):
    return render(request, 'elections/manage_candidates.html')

@admin_or_officer_required
def election_results(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    if election.end_time < timezone.now():
        results = Vote.objects.filter(election=election) \
            .values('candidate__name') \
            .annotate(vote_count=Count('candidate'))
        return render(request, 'elections/results.html', {'election': election, 'results': results})
    else:
        return HttpResponseForbidden("Results cannot be viewed until the election ends.")
