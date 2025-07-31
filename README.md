api-usuarios/
├── app/
│   ├── main.py                # Punto de entrada de la aplicación FastAPI
│   ├── models/
│   │   └── user.py            # Esquemas de datos con Pydantic
│   ├── routes/
│   │   └── user_routes.py     # Endpoints de la API
│   └── db/
│       └── mongo.py           # Conexión a MongoDB
├── .env                       # Variables de entorno (no versionado)
├── requirements.txt           # Dependencias de Python
├── docker-compose.yml         # Levanta la API y MongoDB en contenedores
└── README.md                  # Este archivo

1. Clona el Repositorio
git clone https://github.com/jpgb-hub/api_user.git
cd api_user

2. Crea un Entorno Virtual
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

3. Instala Las dependencias
pip install -r requirements.txt

4. Crea el archivo .env
pip install -r requirements.txt
   
5. Inicia Mongo localmente
Si tienes MongoDB instalado localmente, asegúrate de que esté corriendo.
  
6. Ejecuta la aplicación
uvicorn app.main:app --reload

🔐 Validaciones incluidas
Email válido con email-validator
Contraseña con mínimo de 8 caracteres
El sistema genera un UUID único para cada usuario

