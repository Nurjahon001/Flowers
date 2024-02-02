from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import FlowerReviewForm
from .models import Flowers,FlowerReview
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

class FlowerList(LoginRequiredMixin,View):
    def get(self,request):
        flowers=Flowers.objects.order_by('create_at')
        search_query=request.GET.get('q')
        if search_query:
            flowers=flowers.filter(name_f__icontains=search_query)
        # context={
        #     'books':books
        # }

        paginator = Paginator(flowers, 2)  # Show 10 books per page
        page = request.GET.get('page')
        try:
            flowers = paginator.page(page)
        except PageNotAnInteger:
            flowers = paginator.page(1)
        except EmptyPage:
            flowers = paginator.page(paginator.num_pages)

        return render(request,'flower/flower_list.html',{'flowers':flowers})


# class FlowerDetailView(LoginRequiredMixin,View):
#     def get(self,request,pk):
#         # book = get_object_or_404(Books, pk=pk)
#         flower=Flowers.objects.get(pk=pk)
#         # book_review=BookReview.objects.all()
#         context = {
#             'flower': flower,
#             # 'book_review':book_review
#         }
#         return render(request,'flower/flower_detail.html',context=context)

class FlowerDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        flower = get_object_or_404(Flowers, pk=pk)
        reviews = FlowerReview.objects.filter(flower=flower)

        context = {
            'flower': flower,
            'reviews': reviews,
            'form': FlowerReviewForm(),  # Create an instance of the review form
        }

        return render(request, 'flower/flower_detail.html', context=context)

    def post(self, request, pk):
        flower = get_object_or_404(Flowers, pk=pk)
        form = FlowerReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.flower = flower
            review.save()
            return redirect('flowers:flower-detail', pk=pk)
        else:
            reviews = FlowerReview.objects.filter(flower=flower)
            context = {
                'flower': flower,
                'reviews': reviews,
                'form': form,
            }
            return render(request, 'flower/flower_detail.html', context=context)