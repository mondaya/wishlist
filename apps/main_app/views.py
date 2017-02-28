from django.shortcuts import render ,redirect
from models import WishList
from django.contrib import messages

# Create your views here.
def index(request):
    
    try:
        context = {
                'first_name': request.session['user'],
                'login_id': request.session['user_id'],
                'status': request.session['user_status'], 
                'wish_list': WishList.objects.getwishList(request.session['user_id']),
                'other_wish_list':WishList.objects.otherUserWishList(request.session['user_id'])                
            }
        
        
        return render( request, 'main_app/index.html', context)
    except KeyError:
            return redirect('home:signup')
            
def create(request):
   
    try:
        context = {
                'first_name': request.session['user'],
                'status': request.session['user_status'],                             
            }
        
        
        return render( request, 'main_app/add.html', context)
    except KeyError:
            return redirect('home:signup')
def show(request, item_id):
   
    try:
        context = {
                'first_name': request.session['user'],
                'status': request.session['user_status'], 
                'post':WishList.objects.getWish(item_id)              
            }
        
        
        return render( request, 'main_app/show.html', context)
    except KeyError:
            return redirect('home:signup')


def add(request):
    
    if request.method == 'POST':
        try:
            context = {
                    'first_name': request.session['user'],
                    'status': request.session['user_status'],                             
                }
            rsp = WishList.objects.addItem(request.POST, request.session['user_id'])  
            print rsp            
            if rsp['status'] :
                return redirect('dashboard:home')
            else:
                for error in rsp['errors']:
                    messages.error(request, error)
                return render( request, 'main_app/add.html', context)
        except KeyError:
                return redirect('home:signup')
                
def addTo(request, item_id):
    
    if request.method == 'GET':
        try:
            context = {
                    'first_name': request.session['user'],
                    'status': request.session['user_status'],                             
                }
            rsp = WishList.objects.addItemTo(item_id, request.session['user_id'])  
            return redirect('dashboard:home')            
        except KeyError:
                return redirect('home:signup')
def delete(request, item_id):
    
    if request.method == 'POST':
        try:
            context = {
                    'first_name': request.session['user'],
                    'status': request.session['user_status'],                             
                }
            rsp = WishList.objects.delete(item_id, request.session['user_id'])  
            return redirect('dashboard:home')            
        except KeyError:
                return redirect('home:signup')
def remove(request, item_id):
    
    if request.method == 'POST':
        try:
            context = {
                    'first_name': request.session['user'],
                    'status': request.session['user_status'],                             
                }
            rsp = WishList.objects.remove(item_id, request.session['user_id'])  
            return redirect('dashboard:home')            
        except KeyError:
                return redirect('home:signup')