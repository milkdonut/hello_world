from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View

from TestModel.models import TestForm
from TestModel.models import Contact


class MyView(View):
    def get(self, request):
        test_form = TestForm
        list_all = Contact.objects.all()
        context = {'test_form': test_form,
                   'list_all': list_all}
        return render(request, 'index.html', context)

    def post(self, request):
        form = TestForm(request.POST)
        test_form = TestForm
        if form.is_valid():
            # <process form cleaned data>
            # return HttpResponseRedirect('/success/')
            form.save()
            list_all = Contact.objects.all()
            context = {'test_form': test_form, 'list_all': list_all}
            return render(request, 'index.html', context)
