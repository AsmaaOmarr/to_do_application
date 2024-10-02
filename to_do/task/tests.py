import pytest
from django.urls import reverse
from .models import Task

# This marks the test as using the database
@pytest.mark.django_db  
class TestTaskModel:

    @pytest.fixture
    def task(self):
        # Create an initial task for testing
        return Task.objects.create(title="Test Task")


    def test_add_task_invalid_input(self, client, task):  
        response = client.post(reverse('add_task'), {'title': ''})
        assert Task.objects.count() == 1 
        assert response.status_code == 200  
        
    def test_add_task_invalid_inputII(self, client, task):
        response = client.post(reverse('add_task'), {'title': '123456789123456789123456789123456789'})
        assert Task.objects.count() == 1  
        assert response.status_code == 200  
        
    def test_add_task_valid_input(self, client, task):  
        response = client.post(reverse('add_task'), {'title': 'New Task'})
        assert Task.objects.count() == 2 
        assert Task.objects.filter(title='New Task').exists()
        assert response.status_code == 302 

    
    def test_complete_task(self, client, task):
        task_id = task.id
        response = client.post(reverse('complete_task', args=[task_id]))
        task.refresh_from_db() 
        assert task.completed is True
        assert response.status_code == 302  

    def test_delete_task(self, client, task):
        task_id = task.id
        response = client.post(reverse('delete_task', args=[task_id]))
        assert Task.objects.count() == 0 
        assert response.status_code == 302

        