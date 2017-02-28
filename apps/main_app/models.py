from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User
from django.db.models import When, F, Q,Case,Value,BooleanField,BigIntegerField
# Create your models here. 

class WishListManager(models.Manager):   
   
    def addItem(self, data, user_id):
        errors = []            
        if len(data['item_name']) == 0:
            errors.append("item name is empty")
        elif len(data['item_name']) < 4:
            errors.append("item name needs more 3 chars")
        
        if len(errors) == 0:
            this_user = User.objects.get(id=user_id)            
            wish = self.create(name=data['item_name'],user=this_user)            
            wish.wished.add(this_user) 
                       
            return {'status':True}
        else:
            return {'status':False,'errors':errors}
            
    def getwishList(self,user_id):
        print self.all().values()     
        return self.filter(wished__id=user_id)  

    def otherUserWishList(self,user_id):   
       return self.exclude(wished__id=user_id)
      
       
    def addItemTo(self, item_id, user_id):
        wish =  self.get(id=item_id)
        this_user = User.objects.get(id=user_id) 
        wish.wished.add(this_user)
        wish.save
        return  
        
    def remove(self, item_id, user_id):
        wish =  self.get(id=item_id)
        user = wish.user
        wish.wished.clear()
        wish.wished.add(user)         
        
        return  
        
    def delete(self, item_id, user_id):
        wish =  self.get(id=item_id, user__id=user_id)
        wish.delete()
        return
        
    def getWish(self, item_id):
        wish =  self.get(id=item_id)        
        return wish
    
class WishList(models.Model):
    name=models.CharField(max_length=100)  
    user=models.ForeignKey(User, related_name='added_by')
    wished=models.ManyToManyField(User, related_name='has_wishes')    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)    
    objects=WishListManager()