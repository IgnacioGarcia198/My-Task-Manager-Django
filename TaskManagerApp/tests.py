from django.test import TestCase
from .models import Task
from django.utils import timezone
from django.core.exceptions import ValidationError

class TaskModelTests(TestCase):
    def test_default_values(self):
        task = Task.objects.create(title="Test Task", text="Test Description")
       
       
        self.assertEqual(task.is_done, False)
        self.assertAlmostEqual(task.creation_date, timezone.now(), delta=timezone.timedelta(seconds=1))
        self.assertIsNone(task.due_date)

    def test_string_representation(self):
        task = Task(title="Test Task")
        
        
        self.assertEqual(
            str(task), 
            """
task title: Test Task
task text: 
is done: False
"""
        )
    
    def test_marking_task_as_done(self):
        task = Task.objects.create(title="Test Task")
        
        
        task.is_done = True
        task.save()
        updated_task = Task.objects.get(id=task.id)
       
       
        self.assertTrue(updated_task.is_done)
    
    def test_task_due_date(self):
        future_date = timezone.now() + timezone.timedelta(days=10)
        
        
        task = Task.objects.create(title="Future Task", due_date=future_date)
        
        
        self.assertEqual(task.due_date, future_date)

    def test_create_and_update_task(self):
        task = Task.objects.create(title="Original Title")
        
        
        task.title = "Updated Title"
        task.save()
        updated_task = Task.objects.get(id=task.id)
        
        
        self.assertEqual(updated_task.title, "Updated Title")

    def test_order_by_due_date(self):
        Task.objects.create(title="Later task", is_done=False, due_date=timezone.now() + timezone.timedelta(days=5))
        Task.objects.create(title="Sooner Task", is_done=False, due_date=timezone.now() + timezone.timedelta(days=1))
        
        
        tasks_by_due_date = Task.objects.order_by("due_date")
        
        
        self.assertEqual(tasks_by_due_date.count(), 2)
        self.assertEqual(tasks_by_due_date.first().title, "Sooner Task")

    def test_delete_task(self):
        task = Task.objects.create(title="Task to be deleted")
        task_id = task.id
        
        
        task.delete()
        
        
        self.assertFalse(Task.objects.filter(id=task_id).exists())

    def test_invalid_due_date(self):
        with self.assertRaises(ValidationError):
            Task.objects.create(title="Task with invalid date", due_date="invalid-date")
