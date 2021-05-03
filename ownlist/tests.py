from django.urls import resolve
from django.test import TestCase
from ownlist.views import home_page

from ownlist.models import Item, List

from django.http import HttpRequest
from django.template.loader import render_to_string


class MyMainPage(TestCase):
    
    def test_root_url_resolves_to_mainpage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    def test_only_saves_items_when_necessary(self): 
        self.client.get('/')        
        self.assertEqual(Item.objects.count(), 0)
      
class ListViewTest(TestCase):
 
    def test_uses_list_template(self):
        list_ = List.objects.create()        
        response = self.client.get(f'/ownlist/{list_.id}/')
        self.assertTemplateUsed(response, 'Details.html')
     
   
    def test_displays_all_list_items(self):        
        list_ = List.objects.create()        
        Item.objects.create(sFname='Summer', list=list_)        
        Item.objects.create(sFname='Athena', list=list_)
   
    def test_passes_correct_list_to_template(self):       
        other_list = List.objects.create()        
        correct_list = List.objects.create()        
        response = self.client.get(f'/ownlist/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)  
 
class NewListTest(TestCase):   

 
    def test_redirects_after_POST(self):        
        response = self.client.post('/ownlist/new', data={'fname': 'A new name','lname': 'new lastname','address':'A new address','jPlaces': 'A new Places','jNumber': 'A new Number','jDate': 'A new Date'})                     
        new_list = List.objects.first()        
        self.assertRedirects(response, f'/ownlist/{new_list.id}/')
       

       
class NewItemTest(TestCase):
    
    def test_can_save_a_POST_request_to_an_existing_list(self):       
        other_list = List.objects.create()        
        correct_list = List.objects.create()        
        self.client.post(f'/ownlist/{correct_list.id}/add_item', data={'fname': 'A new name','lname': 'new lastname','address':'A new address','jPlaces': 'A new Places','jNumber': 'A new Number','jDate': 'A new Date'})
              
        self.assertEqual(Item.objects.count(), 1)        
        new_item = Item.objects.first()        
        self.assertEqual(new_item.sFname, '')       
        self.assertEqual(new_item.list, correct_list)
      
    def test_redirects_to_list_view(self):        
        other_list = List.objects.create()        
        correct_list = List.objects.create()        
        response = self.client.post(f'/ownlist/{correct_list.id}/add_item',data={'fname': 'A new name','lname': 'new lastname','address':'A new address','jPlaces': 'A new Places','jNumber': 'A new Number','jDate': 'A new Date'})  
        self.assertRedirects(response, f'/ownlist/{correct_list.id}/')
           
class ORM(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()        
        list_.save()

        first_item = Item()        
        first_item.sFname = 'The first (ever) list item' 
        first_item.list = list_ 
        first_item.save()        
                       
        second_item = Item()      
        second_item.sFname = 'Item the second'
        second_item.list = list_         
        second_item.save()
               
               
        saved_list = List.objects.first()          
        self.assertEqual(saved_list, list_)
                         
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
               
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]             
        self.assertEqual(first_saved_item.sFname, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.sFname, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)


