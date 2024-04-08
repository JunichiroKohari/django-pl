# python-pl

### run server
python manage.py runserver 0.0.0.0:8000

### call api example
- insert
curl -X POST -H "Content-Type: application/json" http://localhost:8000/api/insert -d '{"name": "test1", "category": "tech", "title": "test", "price": 3000, "readAt": "2024-04-08", "isPublic": true, "isFavorite": true}'
- list
curl -X POST -H "Content-Type: application/json" http://localhost:8000/api/read