from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.
def index_page(request):
    
    # new_worker = Worker(name='Иван', second_name='Маейрн', salary=70000)
    # new_worker.save()
    
    Worker.objects.get(id=5).delete()
    
    all_workers = Worker.objects.all()
    
    print(all_workers)
    
    workers_filtred = Worker.objects.filter(salary=45000)
    print(workers_filtred)
    
    for i in all_workers:
        print(f"Фамилия: {i.second_name}, Имя: {i.name}, Зарплата: {i.salary}, ID: {i.id}")
    
    return render(request, 'index.html')

