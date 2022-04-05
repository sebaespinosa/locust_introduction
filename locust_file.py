from random import random
from json import JSONDecodeError
from locust import HttpUser, task, between

class QuickStartUser(HttpUser):

    def __init__(self, parent):
        super(QuickStartUser, self).__init__(parent)
        self.token = ""

    wait_time = between(1, 5)
    # method makes it easy to introduce delays after each task execution. If no wait_time is specified, the next task will be executed as soon as one finishes

    # Simple page request task
    #@tag('tag1') si en el comando de inicio agrego "--tag tag1" solo se ejecutará esta tarea
    @task
    def index_page(self):
        self.client.get("/")
    
    @task
    def page_manzana(self):
        self.client.get("/frutas/manzanas/manzana-fuji-kilogramo.html")
    
#    # Para caso con inicio de sesión
#    # Puedo agregar un override del método on_start para que cuando se cree la clase se logee
#    def on_start(self):
#        with self.client.get(url="/login") as response:
#            self.token = response.json()["token"]
#    
#    @task
#    def page_for_logged_user(self):
#        self.client.get(url="/logged_page", headers={"authorization": self.token})
#    
#    # Para probar endpoint que recibe parámetros a través de la URL
#    @task
#    def page_with_url_params(self):
#        user_id = str(random.randint(0,3))
#        self.client.get(url="/users/" + user_id,
#                        headers={"authorization": self.token},
#                        name="Users")   # El campo name, es para agrupar en el reporte todas las solicitudes a /users/ que llevan diferente id
#
#    # PAGE Post
#    @task
#    def page_post(self):
#        response = self.client.post("/login", {"username":"testuser", "password":"secret"})
#        print("Response status code:", response.status_code)
#        print("Response text:", response.text)
#        response = self.client.get("/my-profile")
#        
#        # Puedo revisar la respuesta y marcar como success o failure según su contenido
#        with self.client.get("/", catch_response=True) as response:
#            if response.text != "Success":
#                response.failure("Got wrong response")
#            elif response.elapsed.total_seconds() > 0.5:
#                response.failure("Request took too long")
#        with self.client.get("/does_not_exist/", catch_response=True) as response:
#            if response.status_code == 404:
#                response.success()
#    

#    # Test de API Request
#    @task
#    def call_and_validate_REST_API(self):
#        with self.client.post("/", json={"foo": 42, "bar": None}, catch_response=True) as response:
#            try:
#                if response.json()["greeting"] != "hello":
#                    response.failure("Did not get expected value in greeting")
#            except JSONDecodeError:
#                response.failure("Response could not be decoded as JSON")
#            except KeyError:
#                response.failure("Response did not contain expected key 'greeting'")
