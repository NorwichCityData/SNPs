from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from allauth.account.forms import LoginForm, SignupForm
from bson import json_util
from . import mongo
from .file_handlers import handle_uploaded_file, parse_spreadsheet_from_mongo_record
from .mongo import file_record
from .forms import UploadFileForm
from settings import NOUNS
from . import scrape


def login(request):
    context = {
        'login_form': LoginForm()
    }
    return render(request, 'login.html', context)


@login_required
def index_view(request):
    docs = mongo.cursor_to_list(mongo.get_file_records_for_user(user_id=request.user.id))
    if docs:
        headers = docs[0].keys()
    else:
        headers = list()
    return render(request, 'index.html', {'headers': headers, 'records': docs})


@login_required
def batch_view(request):
    return render(request, 'batches.html', {})


@login_required
def snps_view(request):
    return render(request, 'snps.html', {})


@login_required
def upload_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # upload file and create mongo record
            mongo_id = handle_uploaded_file(form, user_id=request.user.id)

            # now parse spreadsheet
            parsed_data = parse_spreadsheet_from_mongo_record(mongo_id=mongo_id)

            # update record with parsed data
            file_record(task=NOUNS['PUT'], target_id=mongo_id, fields=parsed_data)

            return HttpResponseRedirect(reverse('index'))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


@login_required
def view_batch(request, batch_id):
    return render(request, 'batches.html', {'batch_id': batch_id})


@login_required
def get_samples_in_batch(request, batch_id):
    batch = mongo.get_samples_in_batch(batch_id)
    data = batch['snps']
    return HttpResponse(json_util.dumps({'data': data}))


@login_required
def get_snps_in_sample(request, batch_id, sample_name):
    snps = mongo.get_snps_in_sample(batch_id, sample_name)
    return HttpResponse(json_util.dumps({'snps': snps}))


@login_required
def get_snp_data(request):
    rs = request.GET.get('snp')
    variant = request.GET.get('variant')
    batch = request.GET.get('batch_id')
    sample = request.GET.get('sample')

    resp = scrape.snp(rs, variant)

    #if resp and not 'error' in resp:
    #    mongo.update_snp(batch, sample, rs, resp['trait'], resp['chromosome'], resp['position'])

    resp = json_util.dumps(resp)

    return HttpResponse(resp)
